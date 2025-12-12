# Java/Spring Boot Patterns

> EdTech-compliant patterns for Java development

---

## Authentication & Authorization

### Pattern: Secure Endpoint with Student Data Access

```java
@RestController
@RequestMapping("/api/students")
@PreAuthorize("hasRole('TEACHER') or hasRole('ADMIN')")
public class StudentController {

    @Autowired
    private AuditService auditService;

    @GetMapping("/{studentId}")
    @AuditLog(dataType = "STUDENT_PII", action = "READ")
    public ResponseEntity<StudentDTO> getStudent(
            @PathVariable String studentId,
            @AuthenticationPrincipal UserDetails user) {

        // Verify user can access THIS specific student
        if (!authorizationService.canAccessStudent(user, studentId)) {
            auditService.logUnauthorizedAccess(user, studentId);
            throw new ForbiddenException("Access denied");
        }

        Student student = studentService.findById(studentId);
        return ResponseEntity.ok(toDTO(student)); // Never return entity directly
    }
}
```

**Why:** Defense in depth - role check + specific resource authorization + audit logging.

---

## Data Access

### Pattern: Parameterized Queries (MANDATORY)

```java
// GOOD - Parameterized query
@Query("SELECT s FROM Student s WHERE s.email = :email")
Optional<Student> findByEmail(@Param("email") String email);

// GOOD - JPA method naming
Optional<Student> findByEmailAndSchoolId(String email, Long schoolId);

// BAD - NEVER concatenate user input
@Query("SELECT s FROM Student s WHERE s.email = '" + email + "'")  // SQL INJECTION!
```

### Pattern: Repository with Tenant Isolation

```java
@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {

    // Always filter by school/district - prevents cross-tenant access
    @Query("SELECT s FROM Student s WHERE s.id = :id AND s.school.id = :schoolId")
    Optional<Student> findByIdAndSchoolId(
        @Param("id") Long id,
        @Param("schoolId") Long schoolId
    );

    // For admins: explicit method name shows it's all schools
    @PreAuthorize("hasRole('SUPER_ADMIN')")
    List<Student> findAllAcrossSchools();
}
```

**Why:** Tenant isolation prevents IDOR (Insecure Direct Object Reference) attacks.

---

## Logging

### Pattern: Safe Logging (No PII)

```java
@Service
@Slf4j
public class StudentService {

    public Student processEnrollment(EnrollmentRequest request) {
        // GOOD - Log action, not PII
        log.info("Processing enrollment for school: {}, grade: {}",
            request.getSchoolId(), request.getGrade());

        // BAD - NEVER log student PII
        // log.info("Enrolling student: {}", request.getStudentName());  // FERPA violation!
        // log.info("Student email: {}", request.getEmail());  // PII leak!

        // If you must reference a student, use masked ID
        log.debug("Processing student reference: {}",
            maskStudentId(request.getStudentId()));

        return enrollStudent(request);
    }

    private String maskStudentId(String id) {
        if (id == null || id.length() < 4) return "***";
        return "***" + id.substring(id.length() - 4);
    }
}
```

---

## DTOs and Data Transfer

### Pattern: Never Expose Entities

```java
// Entity - internal only
@Entity
@Table(name = "students")
public class Student {
    @Id
    private Long id;

    @Column(name = "ssn", columnDefinition = "bytea")
    @Encrypted
    private String ssn;  // Sensitive!

    private String firstName;
    private String lastName;
    private String email;
    private LocalDate dateOfBirth;

    @OneToMany
    private List<Grade> grades;  // Potentially large

    @OneToMany
    private List<DisciplinaryRecord> disciplinaryRecords;  // Very sensitive
}

// DTO - what the API returns
public record StudentDTO(
    Long id,
    String firstName,
    String lastName,
    String email,
    // Note: NO ssn, NO disciplinaryRecords, NO full grade history
    int gradeLevel
) {
    public static StudentDTO fromEntity(Student student) {
        return new StudentDTO(
            student.getId(),
            student.getFirstName(),
            student.getLastName(),
            student.getEmail(),
            student.getCurrentGradeLevel()
        );
    }
}
```

**Why:** DTOs control exactly what data leaves your service. Entities may have sensitive fields.

---

## Error Handling

### Pattern: Safe Error Responses

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(StudentNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(StudentNotFoundException ex) {
        // GOOD - Generic message
        return ResponseEntity.status(404)
            .body(new ErrorResponse("Resource not found", "NOT_FOUND"));

        // BAD - Leaks information
        // return ResponseEntity.status(404)
        //     .body(new ErrorResponse("Student john.doe@school.com not found"));
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<ErrorResponse> handleGeneric(Exception ex) {
        // Log the real error internally
        log.error("Unexpected error", ex);

        // Return generic message to user
        return ResponseEntity.status(500)
            .body(new ErrorResponse(
                "An unexpected error occurred. Please contact support.",
                "INTERNAL_ERROR"
            ));

        // BAD - Leaks stack trace, database info, etc.
        // return ResponseEntity.status(500).body(ex.getMessage());
    }
}
```

---

## Validation

### Pattern: Input Validation

```java
public record CreateStudentRequest(
    @NotBlank(message = "First name is required")
    @Size(max = 100, message = "First name too long")
    @Pattern(regexp = "^[a-zA-Z\\s\\-']+$", message = "Invalid characters in name")
    String firstName,

    @NotBlank(message = "Last name is required")
    @Size(max = 100, message = "Last name too long")
    String lastName,

    @NotBlank(message = "Email is required")
    @Email(message = "Invalid email format")
    String email,

    @NotNull(message = "Grade level is required")
    @Min(value = -1, message = "Invalid grade level")  // -1 = Pre-K
    @Max(value = 12, message = "Invalid grade level")
    Integer gradeLevel,

    @NotNull(message = "School ID is required")
    Long schoolId
) {}

@PostMapping
public ResponseEntity<StudentDTO> createStudent(
        @Valid @RequestBody CreateStudentRequest request,
        @AuthenticationPrincipal UserDetails user) {
    // Validation happens automatically via @Valid
    // Additional business validation
    if (!authorizationService.canCreateStudentInSchool(user, request.schoolId())) {
        throw new ForbiddenException("Cannot create students in this school");
    }
    // ...
}
```

---

## Encryption

### Pattern: Field-Level Encryption

```java
@Entity
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // Encrypted at rest using AES-256
    @Convert(converter = EncryptedStringConverter.class)
    @Column(columnDefinition = "bytea")
    private String ssn;

    @Convert(converter = EncryptedStringConverter.class)
    @Column(columnDefinition = "bytea")
    private String medicalInfo;

    // Not encrypted - not PII
    private Integer gradeLevel;
}

@Converter
public class EncryptedStringConverter implements AttributeConverter<String, byte[]> {

    @Autowired
    private EncryptionService encryptionService;

    @Override
    public byte[] convertToDatabaseColumn(String attribute) {
        return encryptionService.encrypt(attribute);
    }

    @Override
    public String convertToEntityAttribute(byte[] dbData) {
        return encryptionService.decrypt(dbData);
    }
}
```

---

## Audit Logging

### Pattern: Audit Trail for Student Data

```java
@Aspect
@Component
@Slf4j
public class AuditAspect {

    @Autowired
    private AuditRepository auditRepository;

    @Around("@annotation(auditLog)")
    public Object audit(ProceedingJoinPoint joinPoint, AuditLog auditLog) throws Throwable {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        String userId = auth != null ? auth.getName() : "anonymous";

        AuditEntry entry = AuditEntry.builder()
            .userId(userId)
            .action(auditLog.action())
            .dataType(auditLog.dataType())
            .timestamp(Instant.now())
            .method(joinPoint.getSignature().getName())
            .success(false)
            .build();

        try {
            Object result = joinPoint.proceed();
            entry.setSuccess(true);
            return result;
        } catch (Exception e) {
            entry.setErrorMessage(e.getClass().getSimpleName());
            throw e;
        } finally {
            auditRepository.save(entry);  // Always save audit, even on failure
        }
    }
}

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface AuditLog {
    String dataType();
    String action() default "ACCESS";
}
```

---

## Testing

### Pattern: Security Tests

```java
@SpringBootTest
@AutoConfigureMockMvc
class StudentControllerSecurityTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    void shouldRejectUnauthenticated() throws Exception {
        mockMvc.perform(get("/api/students/1"))
            .andExpect(status().isUnauthorized());
    }

    @Test
    @WithMockUser(roles = "TEACHER")
    void shouldRejectCrossSchoolAccess() throws Exception {
        // Teacher from school 1 trying to access student from school 2
        mockMvc.perform(get("/api/students/999"))  // Student in different school
            .andExpect(status().isForbidden());
    }

    @Test
    void shouldPreventSqlInjection() throws Exception {
        mockMvc.perform(get("/api/students")
                .param("search", "'; DROP TABLE students; --"))
            .andExpect(status().isBadRequest());  // Rejected by validation
    }

    @Test
    @WithMockUser(roles = "TEACHER")
    void shouldNotLeakPiiInErrors() throws Exception {
        MvcResult result = mockMvc.perform(get("/api/students/99999"))
            .andExpect(status().isNotFound())
            .andReturn();

        String response = result.getResponse().getContentAsString();
        assertThat(response).doesNotContain("@");  // No email
        assertThat(response).doesNotContain("student");  // Generic message
    }
}
```

---

## Quick Reference

| Task | Pattern |
|------|---------|
| Authenticate | `@PreAuthorize` + `@AuthenticationPrincipal` |
| Authorize specific resource | `authorizationService.canAccess(user, resourceId)` |
| Query with tenant isolation | `findByIdAndSchoolId(id, schoolId)` |
| Log safely | Never log PII, use masked IDs |
| Return data | Use DTOs, never entities |
| Handle errors | Generic messages to users, detailed logs internally |
| Encrypt sensitive data | `@Convert(converter = EncryptedStringConverter.class)` |
| Audit access | `@AuditLog(dataType = "STUDENT_PII")` |

---

*"Security is not a feature, it's a requirement."*
