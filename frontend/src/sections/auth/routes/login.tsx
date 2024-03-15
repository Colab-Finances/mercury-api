import { createFileRoute, redirect } from '@tanstack/react-router'
import { LoginForm } from '../components/LoginForm'
import { MercuryAuthRepository } from '../../../modules/auth/infrastructure/MercuryAuthRepository'
import { isLoggedIn } from '../../../modules/auth/application/login/isLoggedIn'

const repository = new MercuryAuthRepository()

export const Route = createFileRoute('/login')({
  component: Login,
  beforeLoad: async () => {
    if (isLoggedIn(repository)) {
      throw redirect({
        to: '/',
      })
    }
  },
})

function Login() {
  return LoginForm(repository)
}

export default Login
