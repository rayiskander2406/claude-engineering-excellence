# React Patterns

> EdTech-compliant patterns for React development

---

## Authentication & Protected Routes

### Pattern: Protected Route Component

```tsx
// components/auth/ProtectedRoute.tsx
import { Navigate, useLocation } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';

interface ProtectedRouteProps {
  children: React.ReactNode;
  requiredRoles?: string[];
  requiredPermissions?: string[];
}

export function ProtectedRoute({
  children,
  requiredRoles = [],
  requiredPermissions = []
}: ProtectedRouteProps) {
  const { user, isLoading, isAuthenticated } = useAuth();
  const location = useLocation();

  if (isLoading) {
    return <LoadingSpinner />;
  }

  if (!isAuthenticated) {
    // Save intended destination for redirect after login
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  // Check roles
  if (requiredRoles.length > 0) {
    const hasRequiredRole = requiredRoles.some(role =>
      user?.roles?.includes(role)
    );
    if (!hasRequiredRole) {
      return <Navigate to="/unauthorized" replace />;
    }
  }

  // Check permissions (for fine-grained access)
  if (requiredPermissions.length > 0) {
    const hasPermissions = requiredPermissions.every(permission =>
      user?.permissions?.includes(permission)
    );
    if (!hasPermissions) {
      return <Navigate to="/unauthorized" replace />;
    }
  }

  return <>{children}</>;
}

// Usage
<Route
  path="/students/:id"
  element={
    <ProtectedRoute requiredRoles={['teacher', 'admin']}>
      <StudentDetailPage />
    </ProtectedRoute>
  }
/>
```

---

## Data Fetching

### Pattern: Secure Data Fetching with React Query

```tsx
// hooks/useStudent.ts
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { api } from '@/lib/api';

interface Student {
  id: string;
  firstName: string;
  lastName: string;
  email: string;
  gradeLevel: number;
  // Note: Sensitive fields should NOT be in this type
  // ssn, disciplinaryRecords, etc. - handled server-side only
}

export function useStudent(studentId: string) {
  return useQuery({
    queryKey: ['student', studentId],
    queryFn: async () => {
      const response = await api.get<Student>(`/students/${studentId}`);
      return response.data;
    },
    // Don't retry on 403/404 - user doesn't have access
    retry: (failureCount, error: any) => {
      if (error?.response?.status === 403 || error?.response?.status === 404) {
        return false;
      }
      return failureCount < 3;
    },
    // Don't cache student data for too long (PII)
    staleTime: 1000 * 60 * 5, // 5 minutes
    gcTime: 1000 * 60 * 10, // 10 minutes
  });
}

export function useUpdateStudent() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async ({ id, data }: { id: string; data: Partial<Student> }) => {
      const response = await api.patch(`/students/${id}`, data);
      return response.data;
    },
    onSuccess: (data, variables) => {
      // Invalidate and refetch
      queryClient.invalidateQueries({ queryKey: ['student', variables.id] });
      queryClient.invalidateQueries({ queryKey: ['students'] });
    },
    onError: (error: any) => {
      // Never show raw error to user - might contain PII
      console.error('Update failed:', error);
      // Show generic message
      toast.error('Failed to update student. Please try again.');
    },
  });
}
```

---

## Forms

### Pattern: Secure Form with Validation

```tsx
// components/students/StudentForm.tsx
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

const studentSchema = z.object({
  firstName: z
    .string()
    .min(1, 'First name is required')
    .max(100, 'First name too long')
    .regex(/^[a-zA-Z\s\-']+$/, 'Invalid characters in name'),
  lastName: z
    .string()
    .min(1, 'Last name is required')
    .max(100, 'Last name too long'),
  email: z
    .string()
    .email('Invalid email address'),
  gradeLevel: z
    .number()
    .min(-1, 'Invalid grade level')  // -1 = Pre-K
    .max(12, 'Invalid grade level'),
});

type StudentFormData = z.infer<typeof studentSchema>;

export function StudentForm({ onSubmit, initialData }: StudentFormProps) {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<StudentFormData>({
    resolver: zodResolver(studentSchema),
    defaultValues: initialData,
  });

  const handleFormSubmit = async (data: StudentFormData) => {
    try {
      await onSubmit(data);
    } catch (error) {
      // Generic error message - don't expose details
      toast.error('Failed to save. Please try again.');
    }
  };

  return (
    <form onSubmit={handleSubmit(handleFormSubmit)}>
      <div>
        <label htmlFor="firstName">First Name</label>
        <input
          id="firstName"
          {...register('firstName')}
          aria-invalid={!!errors.firstName}
          aria-describedby={errors.firstName ? 'firstName-error' : undefined}
        />
        {errors.firstName && (
          <span id="firstName-error" role="alert">
            {errors.firstName.message}
          </span>
        )}
      </div>

      {/* ... other fields ... */}

      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Saving...' : 'Save'}
      </button>
    </form>
  );
}
```

---

## Error Handling

### Pattern: Error Boundary with Safe Messages

```tsx
// components/ErrorBoundary.tsx
import { Component, ErrorInfo, ReactNode } from 'react';

interface Props {
  children: ReactNode;
  fallback?: ReactNode;
}

interface State {
  hasError: boolean;
  errorId?: string;
}

export class ErrorBoundary extends Component<Props, State> {
  state: State = { hasError: false };

  static getDerivedStateFromError(_: Error): State {
    return { hasError: true, errorId: crypto.randomUUID() };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    // Log to error tracking service (Sentry, etc.)
    // NEVER include user data or PII in error reports
    errorReportingService.captureException(error, {
      componentStack: errorInfo.componentStack,
      errorId: this.state.errorId,
      // DO NOT include: user email, student names, etc.
    });
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback || (
        <div role="alert">
          <h2>Something went wrong</h2>
          <p>
            We've been notified and are working on it.
            {this.state.errorId && (
              <> Reference: {this.state.errorId}</>
            )}
          </p>
          <button onClick={() => window.location.reload()}>
            Reload page
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}
```

---

## State Management

### Pattern: Secure Auth State

```tsx
// stores/authStore.ts
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface User {
  id: string;
  email: string;
  roles: string[];
  permissions: string[];
  schoolId: string;
}

interface AuthState {
  user: User | null;
  accessToken: string | null;
  isAuthenticated: boolean;
  setAuth: (user: User, token: string) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      user: null,
      accessToken: null,
      isAuthenticated: false,

      setAuth: (user, token) => set({
        user,
        accessToken: token,
        isAuthenticated: true,
      }),

      logout: () => {
        // Clear all sensitive data
        set({
          user: null,
          accessToken: null,
          isAuthenticated: false,
        });
        // Clear any cached student data
        queryClient.clear();
        // Redirect to login
        window.location.href = '/login';
      },
    }),
    {
      name: 'auth-storage',
      // Only persist non-sensitive data
      partialize: (state) => ({
        // Don't persist the full user object or token
        isAuthenticated: state.isAuthenticated,
      }),
    }
  )
);
```

---

## Displaying Student Data

### Pattern: Safe Data Display

```tsx
// components/students/StudentCard.tsx
interface StudentCardProps {
  student: {
    id: string;
    firstName: string;
    lastName: string;
    gradeLevel: number;
    // photoUrl might be sensitive
    photoUrl?: string;
  };
  showPhoto?: boolean;  // Explicit opt-in for photos
}

export function StudentCard({ student, showPhoto = false }: StudentCardProps) {
  return (
    <div className="student-card">
      {/* Only show photo if explicitly enabled */}
      {showPhoto && student.photoUrl && (
        <img
          src={student.photoUrl}
          alt=""  // Empty alt - name is displayed separately
          loading="lazy"
        />
      )}

      <h3>
        {/* Display name - already filtered by authorization */}
        {student.firstName} {student.lastName}
      </h3>

      <p>Grade: {formatGradeLevel(student.gradeLevel)}</p>

      {/* Never display sensitive info in cards */}
      {/* No: SSN, email, address, disciplinary records */}
    </div>
  );
}

function formatGradeLevel(level: number): string {
  if (level === -1) return 'Pre-K';
  if (level === 0) return 'Kindergarten';
  return `Grade ${level}`;
}
```

---

## API Client

### Pattern: Secure API Configuration

```tsx
// lib/api.ts
import axios from 'axios';
import { useAuthStore } from '@/stores/authStore';

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  withCredentials: true,  // For cookies
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add auth token
api.interceptors.request.use((config) => {
  const token = useAuthStore.getState().accessToken;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle auth errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expired or invalid
      useAuthStore.getState().logout();
    }

    // NEVER log response data - might contain PII
    console.error('API Error:', {
      status: error.response?.status,
      url: error.config?.url,
      method: error.config?.method,
      // DO NOT log: error.response.data, error.config.data
    });

    return Promise.reject(error);
  }
);
```

---

## Testing

### Pattern: Testing with Mock Data

```tsx
// tests/utils/mockData.ts
// Use fake data that looks realistic but is not real PII
export const mockStudent = {
  id: 'stu_test_123',
  firstName: 'Test',
  lastName: 'Student',
  email: 'test.student@example.com',  // example.com is safe
  gradeLevel: 5,
};

// tests/StudentCard.test.tsx
import { render, screen } from '@testing-library/react';
import { StudentCard } from '@/components/students/StudentCard';
import { mockStudent } from './utils/mockData';

describe('StudentCard', () => {
  it('displays student name', () => {
    render(<StudentCard student={mockStudent} />);
    expect(screen.getByText('Test Student')).toBeInTheDocument();
  });

  it('does not display photo by default', () => {
    render(<StudentCard student={{ ...mockStudent, photoUrl: '/photo.jpg' }} />);
    expect(screen.queryByRole('img')).not.toBeInTheDocument();
  });

  it('displays photo when explicitly enabled', () => {
    render(
      <StudentCard
        student={{ ...mockStudent, photoUrl: '/photo.jpg' }}
        showPhoto
      />
    );
    expect(screen.getByRole('img')).toBeInTheDocument();
  });
});
```

---

## Quick Reference

| Task | Pattern |
|------|---------|
| Protect routes | `<ProtectedRoute requiredRoles={['teacher']}>` |
| Fetch data | `useQuery` with retry logic for 403/404 |
| Handle forms | `react-hook-form` + `zod` validation |
| Display errors | Generic messages, log details to service |
| Store auth state | `zustand` with minimal persistence |
| Make API calls | Axios with interceptors for auth |
| Show student data | Only display what's needed, opt-in for sensitive |
| Test | Use fake data from `mockData.ts` |

---

*"The safest PII is the PII you never fetch."*
