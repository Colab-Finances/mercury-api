import { SubmitHandler, useForm } from 'react-hook-form'
import { AuthBasic } from '../../../modules/auth/application/login/AuthBasic'
import { AuthRepository } from '../../../modules/auth/domain/AuthRepository'
import { InvalidCredentials } from '../../../modules/auth/domain/errors/InvalidCredentials'
import { login } from '../../../modules/auth/application/login/login'
import { useNavigate } from '@tanstack/react-router'
import { logOut } from '../../../modules/auth/application/login/logOut'

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
      username: '',
      password: '',
    },
  })
  const navigate = useNavigate()
  const onSubmit: SubmitHandler<AuthBasic> = async (data) => {
    try {
      await login(repository)(data)
      navigate({ to: '/' })
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

export function useLogOut(repository: AuthRepository) {
  const navigate = useNavigate()

  const onClick = () => {
    logOut(repository)
    navigate({ to: '/login' })
  }

  return { onClick }
}
