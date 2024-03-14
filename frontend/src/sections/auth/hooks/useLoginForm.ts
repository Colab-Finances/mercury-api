import { SubmitHandler, useForm } from 'react-hook-form'
import { AuthBasic } from '../../../modules/auth/application/login/AuthBasic'
import { useLogin } from '../../shared/hooks/useAuth'
import { AuthRepository } from '../../../modules/auth/domain/AuthRepository'
import { InvalidCredentials } from '../../../modules/auth/domain/errors/InvalidCredentials'

export function useLoginForm(repository: AuthRepository) {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    setError,
  } = useForm<AuthBasic>({
    mode: 'onBlur',
    criteriaMode: 'all',
    defaultValues: {
      username: 'test@test.test',
      password: 'Test123',
    },
  })

  const onSubmit: SubmitHandler<AuthBasic> = async (data) => {
    try {
      await useLogin(repository)(data)
    } catch (err) {
      if (err instanceof InvalidCredentials) {
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
