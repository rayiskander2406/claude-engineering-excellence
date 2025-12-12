# Vue.js Patterns

> EdTech-compliant patterns for Vue.js development

---

## Authentication & Protected Routes

### Pattern: Navigation Guard for Protected Routes

```typescript
// router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/LoginView.vue'),
      meta: { requiresAuth: false }
    },
    {
      path: '/students/:id',
      name: 'student-detail',
      component: () => import('@/views/StudentDetailView.vue'),
      meta: {
        requiresAuth: true,
        requiredRoles: ['teacher', 'admin']
      }
    },
    {
      path: '/unauthorized',
      name: 'unauthorized',
      component: () => import('@/views/UnauthorizedView.vue')
    }
  ]
})

router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()

  // Check if route requires authentication
  if (to.meta.requiresAuth !== false) {
    if (!authStore.isAuthenticated) {
      // Save intended destination for redirect after login
      return next({
        name: 'login',
        query: { redirect: to.fullPath }
      })
    }

    // Check roles
    const requiredRoles = to.meta.requiredRoles as string[] | undefined
    if (requiredRoles?.length) {
      const hasRequiredRole = requiredRoles.some(role =>
        authStore.user?.roles?.includes(role)
      )
      if (!hasRequiredRole) {
        return next({ name: 'unauthorized' })
      }
    }

    // Check permissions
    const requiredPermissions = to.meta.requiredPermissions as string[] | undefined
    if (requiredPermissions?.length) {
      const hasPermissions = requiredPermissions.every(permission =>
        authStore.user?.permissions?.includes(permission)
      )
      if (!hasPermissions) {
        return next({ name: 'unauthorized' })
      }
    }
  }

  next()
})

export default router
```

---

## Data Fetching

### Pattern: Secure Data Fetching with Composables

```typescript
// composables/useStudent.ts
import { ref, computed } from 'vue'
import { useQuery, useMutation, useQueryClient } from '@tanstack/vue-query'
import { api } from '@/lib/api'
import { useToast } from '@/composables/useToast'

interface Student {
  id: string
  firstName: string
  lastName: string
  email: string
  gradeLevel: number
  // Note: Sensitive fields should NOT be in this type
  // ssn, disciplinaryRecords, etc. - handled server-side only
}

export function useStudent(studentId: Ref<string> | string) {
  const id = computed(() => typeof studentId === 'string' ? studentId : studentId.value)

  return useQuery({
    queryKey: ['student', id],
    queryFn: async () => {
      const response = await api.get<Student>(`/students/${id.value}`)
      return response.data
    },
    // Don't retry on 403/404 - user doesn't have access
    retry: (failureCount, error: any) => {
      if (error?.response?.status === 403 || error?.response?.status === 404) {
        return false
      }
      return failureCount < 3
    },
    // Don't cache student data for too long (PII)
    staleTime: 1000 * 60 * 5, // 5 minutes
    gcTime: 1000 * 60 * 10, // 10 minutes
  })
}

export function useUpdateStudent() {
  const queryClient = useQueryClient()
  const toast = useToast()

  return useMutation({
    mutationFn: async ({ id, data }: { id: string; data: Partial<Student> }) => {
      const response = await api.patch(`/students/${id}`, data)
      return response.data
    },
    onSuccess: (data, variables) => {
      // Invalidate and refetch
      queryClient.invalidateQueries({ queryKey: ['student', variables.id] })
      queryClient.invalidateQueries({ queryKey: ['students'] })
      toast.success('Student updated successfully')
    },
    onError: (error: any) => {
      // Never show raw error to user - might contain PII
      console.error('Update failed:', error)
      // Show generic message
      toast.error('Failed to update student. Please try again.')
    },
  })
}
```

---

## Forms

### Pattern: Secure Form with Validation (VeeValidate + Zod)

```vue
<!-- components/students/StudentForm.vue -->
<script setup lang="ts">
import { useForm } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/zod'
import { z } from 'zod'
import { useToast } from '@/composables/useToast'

const props = defineProps<{
  initialData?: Partial<StudentFormData>
}>()

const emit = defineEmits<{
  submit: [data: StudentFormData]
}>()

const toast = useToast()

const studentSchema = toTypedSchema(
  z.object({
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
  })
)

type StudentFormData = z.infer<typeof studentSchema>

const { handleSubmit, errors, isSubmitting, defineField } = useForm({
  validationSchema: studentSchema,
  initialValues: props.initialData,
})

const [firstName, firstNameAttrs] = defineField('firstName')
const [lastName, lastNameAttrs] = defineField('lastName')
const [email, emailAttrs] = defineField('email')
const [gradeLevel, gradeLevelAttrs] = defineField('gradeLevel')

const onSubmit = handleSubmit(async (values) => {
  try {
    emit('submit', values)
  } catch (error) {
    // Generic error message - don't expose details
    toast.error('Failed to save. Please try again.')
  }
})
</script>

<template>
  <form @submit="onSubmit">
    <div>
      <label for="firstName">First Name</label>
      <input
        id="firstName"
        v-model="firstName"
        v-bind="firstNameAttrs"
        :aria-invalid="!!errors.firstName"
        :aria-describedby="errors.firstName ? 'firstName-error' : undefined"
      />
      <span v-if="errors.firstName" id="firstName-error" role="alert">
        {{ errors.firstName }}
      </span>
    </div>

    <div>
      <label for="lastName">Last Name</label>
      <input
        id="lastName"
        v-model="lastName"
        v-bind="lastNameAttrs"
        :aria-invalid="!!errors.lastName"
      />
      <span v-if="errors.lastName" role="alert">
        {{ errors.lastName }}
      </span>
    </div>

    <div>
      <label for="email">Email</label>
      <input
        id="email"
        type="email"
        v-model="email"
        v-bind="emailAttrs"
        :aria-invalid="!!errors.email"
      />
      <span v-if="errors.email" role="alert">
        {{ errors.email }}
      </span>
    </div>

    <div>
      <label for="gradeLevel">Grade Level</label>
      <select
        id="gradeLevel"
        v-model.number="gradeLevel"
        v-bind="gradeLevelAttrs"
        :aria-invalid="!!errors.gradeLevel"
      >
        <option :value="-1">Pre-K</option>
        <option :value="0">Kindergarten</option>
        <option v-for="grade in 12" :key="grade" :value="grade">
          Grade {{ grade }}
        </option>
      </select>
      <span v-if="errors.gradeLevel" role="alert">
        {{ errors.gradeLevel }}
      </span>
    </div>

    <button type="submit" :disabled="isSubmitting">
      {{ isSubmitting ? 'Saving...' : 'Save' }}
    </button>
  </form>
</template>
```

---

## Error Handling

### Pattern: Error Boundary Component

```vue
<!-- components/ErrorBoundary.vue -->
<script setup lang="ts">
import { ref, onErrorCaptured, provide } from 'vue'
import { errorReportingService } from '@/lib/errorReporting'

const props = defineProps<{
  fallback?: Component
}>()

const hasError = ref(false)
const errorId = ref<string>()

onErrorCaptured((error, instance, info) => {
  hasError.value = true
  errorId.value = crypto.randomUUID()

  // Log to error tracking service (Sentry, etc.)
  // NEVER include user data or PII in error reports
  errorReportingService.captureException(error, {
    componentInfo: info,
    errorId: errorId.value,
    // DO NOT include: user email, student names, etc.
  })

  // Prevent error from propagating
  return false
})

function reset() {
  hasError.value = false
  errorId.value = undefined
}

// Provide reset function to child components
provide('resetError', reset)
</script>

<template>
  <slot v-if="!hasError" />
  <component v-else-if="fallback" :is="fallback" :error-id="errorId" @reset="reset" />
  <div v-else role="alert" class="error-fallback">
    <h2>Something went wrong</h2>
    <p>
      We've been notified and are working on it.
      <template v-if="errorId">
        Reference: {{ errorId }}
      </template>
    </p>
    <button @click="reset">Try again</button>
  </div>
</template>
```

---

## State Management

### Pattern: Secure Auth Store with Pinia

```typescript
// stores/auth.ts
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useQueryClient } from '@tanstack/vue-query'
import router from '@/router'

interface User {
  id: string
  email: string
  roles: string[]
  permissions: string[]
  schoolId: string
}

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null)
  const accessToken = ref<string | null>(null)

  const isAuthenticated = computed(() => !!user.value && !!accessToken.value)

  function setAuth(userData: User, token: string) {
    user.value = userData
    accessToken.value = token
  }

  function logout() {
    // Clear all sensitive data
    user.value = null
    accessToken.value = null

    // Clear any cached student data
    const queryClient = useQueryClient()
    queryClient.clear()

    // Redirect to login
    router.push('/login')
  }

  function hasRole(role: string): boolean {
    return user.value?.roles?.includes(role) ?? false
  }

  function hasPermission(permission: string): boolean {
    return user.value?.permissions?.includes(permission) ?? false
  }

  function canAccessSchool(schoolId: string): boolean {
    if (hasRole('admin')) return true
    return user.value?.schoolId === schoolId
  }

  return {
    user,
    accessToken,
    isAuthenticated,
    setAuth,
    logout,
    hasRole,
    hasPermission,
    canAccessSchool,
  }
}, {
  persist: {
    // Only persist non-sensitive data
    pick: ['isAuthenticated'],
    // Don't persist the full user object or token in localStorage
  }
})
```

---

## Displaying Student Data

### Pattern: Safe Data Display

```vue
<!-- components/students/StudentCard.vue -->
<script setup lang="ts">
interface Student {
  id: string
  firstName: string
  lastName: string
  gradeLevel: number
  photoUrl?: string
}

const props = defineProps<{
  student: Student
  showPhoto?: boolean  // Explicit opt-in for photos
}>()

function formatGradeLevel(level: number): string {
  if (level === -1) return 'Pre-K'
  if (level === 0) return 'Kindergarten'
  return `Grade ${level}`
}
</script>

<template>
  <div class="student-card">
    <!-- Only show photo if explicitly enabled -->
    <img
      v-if="showPhoto && student.photoUrl"
      :src="student.photoUrl"
      alt=""
      loading="lazy"
    />

    <h3>
      <!-- Display name - already filtered by authorization -->
      {{ student.firstName }} {{ student.lastName }}
    </h3>

    <p>{{ formatGradeLevel(student.gradeLevel) }}</p>

    <!-- Never display sensitive info in cards -->
    <!-- No: SSN, email, address, disciplinary records -->
  </div>
</template>
```

---

## API Client

### Pattern: Secure API Configuration

```typescript
// lib/api.ts
import axios from 'axios'
import { useAuthStore } from '@/stores/auth'
import router from '@/router'

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  withCredentials: true,  // For cookies
  headers: {
    'Content-Type': 'application/json',
  },
})

// Add auth token
api.interceptors.request.use((config) => {
  const authStore = useAuthStore()
  if (authStore.accessToken) {
    config.headers.Authorization = `Bearer ${authStore.accessToken}`
  }
  return config
})

// Handle auth errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expired or invalid
      const authStore = useAuthStore()
      authStore.logout()
    }

    // NEVER log response data - might contain PII
    console.error('API Error:', {
      status: error.response?.status,
      url: error.config?.url,
      method: error.config?.method,
      // DO NOT log: error.response.data, error.config.data
    })

    return Promise.reject(error)
  }
)
```

---

## Directives

### Pattern: Permission Directive

```typescript
// directives/permission.ts
import type { Directive } from 'vue'
import { useAuthStore } from '@/stores/auth'

export const vPermission: Directive<HTMLElement, string | string[]> = {
  mounted(el, binding) {
    const authStore = useAuthStore()
    const permissions = Array.isArray(binding.value)
      ? binding.value
      : [binding.value]

    const hasPermission = permissions.some(p => authStore.hasPermission(p))

    if (!hasPermission) {
      el.parentNode?.removeChild(el)
    }
  }
}

export const vRole: Directive<HTMLElement, string | string[]> = {
  mounted(el, binding) {
    const authStore = useAuthStore()
    const roles = Array.isArray(binding.value)
      ? binding.value
      : [binding.value]

    const hasRole = roles.some(r => authStore.hasRole(r))

    if (!hasRole) {
      el.parentNode?.removeChild(el)
    }
  }
}

// Usage in components:
// <button v-permission="'edit:students'">Edit</button>
// <button v-role="['teacher', 'admin']">Manage</button>
```

---

## Testing

### Pattern: Testing with Mock Data

```typescript
// tests/utils/mockData.ts
// Use fake data that looks realistic but is not real PII
export const mockStudent = {
  id: 'stu_test_123',
  firstName: 'Test',
  lastName: 'Student',
  email: 'test.student@example.com',  // example.com is safe
  gradeLevel: 5,
}

export const mockUser = {
  id: 'usr_test_123',
  email: 'teacher@example.com',
  roles: ['teacher'],
  permissions: ['read:students', 'edit:students'],
  schoolId: 'sch_test_123',
}

// tests/components/StudentCard.spec.ts
import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import StudentCard from '@/components/students/StudentCard.vue'
import { mockStudent } from '../utils/mockData'

describe('StudentCard', () => {
  it('displays student name', () => {
    const wrapper = mount(StudentCard, {
      props: { student: mockStudent }
    })
    expect(wrapper.text()).toContain('Test Student')
  })

  it('does not display photo by default', () => {
    const wrapper = mount(StudentCard, {
      props: {
        student: { ...mockStudent, photoUrl: '/photo.jpg' }
      }
    })
    expect(wrapper.find('img').exists()).toBe(false)
  })

  it('displays photo when explicitly enabled', () => {
    const wrapper = mount(StudentCard, {
      props: {
        student: { ...mockStudent, photoUrl: '/photo.jpg' },
        showPhoto: true
      }
    })
    expect(wrapper.find('img').exists()).toBe(true)
  })

  it('formats grade levels correctly', () => {
    const wrapper = mount(StudentCard, {
      props: { student: { ...mockStudent, gradeLevel: -1 } }
    })
    expect(wrapper.text()).toContain('Pre-K')
  })
})
```

---

## Quick Reference

| Task | Pattern |
|------|---------|
| Protect routes | `beforeEach` guard with role/permission checks |
| Fetch data | `useQuery` composable with retry logic |
| Handle forms | `vee-validate` + `zod` validation |
| Display errors | Generic messages, log to error service |
| Store auth state | Pinia with minimal persistence |
| Make API calls | Axios with interceptors |
| Control access | `v-permission` and `v-role` directives |
| Show student data | Only display what's needed, opt-in for sensitive |
| Test | Use fake data from `mockData.ts` |

---

*"Simple patterns, secure by default."*
