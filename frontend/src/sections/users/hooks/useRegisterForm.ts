import { SubmitHandler, useForm } from 'react-hook-form'
import { UserRepository } from '../../../modules/users/domain/UserRepository'
import { DomainError } from '../../../modules/shared/errors/DomainError'
import {
  RegisterData,
  register as registerUser,
} from '../../../modules/users/application/register'
import { useNavigate } from '@tanstack/react-router'
export function useRegisterForm(repository: UserRepository) {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    setError,
  } = useForm<RegisterData>({
    mode: 'onBlur',
    criteriaMode: 'all',
  })
  const navigate = useNavigate()

  const onSubmit: SubmitHandler<RegisterData> = async (data) => {
    try {
      await registerUser(repository)(data)
      navigate({ to: '/' })
    } catch (err) {
      const message =
        err instanceof DomainError ? err.message : 'Unexpected Error'
      setError('root', { message: message })
    }
  }

  return {
    register,
    submitForm: handleSubmit(onSubmit),
    errors,
    isSubmitting,
  }
}
