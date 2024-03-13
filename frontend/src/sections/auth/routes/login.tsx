import { createFileRoute, redirect } from '@tanstack/react-router'

import { isLoggedIn } from '../../shared/hooks/useAuth'

export const Route = createFileRoute('/login')({
  component: Login,
  beforeLoad: async () => {
    if (isLoggedIn()) {
      throw redirect({
        to: '/',
      })
    }
  },
})

import { LoginForm } from '../components/LoginForm'
import { MercuryAuthRepository } from '../../../modules/auth/infrastructure/MercuryAuthRepository'

function Login() {
  const repository = new MercuryAuthRepository()
  return LoginForm(repository)
}

export default Login
