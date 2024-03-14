import { SubmitHandler, useForm } from 'react-hook-form'
import { UserRepository } from '../../../modules/users/domain/UserRepository'
import { DomainError } from '../../../modules/shared/errors/DomainError'
import {
  RegisterData,
  register as registerUser,
} from '../../../modules/users/application/register'
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

  const onSubmit: SubmitHandler<RegisterData> = async (data) => {
    try {
      await registerUser(repository)(data)
    } catch (err) {
      if (err instanceof DomainError) {
        setError('root', { message: err.message })
        return
      }
      setError('root', { message: 'Unexpected Error' })
    }
  }

  return {
    register,
    submitForm: handleSubmit(onSubmit),
    errors,
    isSubmitting,
  }
}
