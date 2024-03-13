import { SubmitHandler, useForm } from 'react-hook-form'
import { AuthBasic } from '../../../modules/auth/application/login/AuthBasic'
import { useLogin } from '../../shared/hooks/useAuth'
import { AuthRepository } from '../../../modules/auth/domain/AuthRepository'

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
      username: 'jgmc3012@gmail.com',
      password: 'Super312!',
    },
  })

  const onSubmit: SubmitHandler<AuthBasic> = async (data) => {
    try {
      await useLogin(repository)(data)
    } catch (err) {
      setError('username', { message: 'An Error on API' })
    }
  }
  return {
    register,
    submitForm: handleSubmit(onSubmit),
    errors,
    isSubmitting,
  }
}
