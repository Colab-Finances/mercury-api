import { createFileRoute, redirect } from '@tanstack/react-router'

import { isLoggedIn } from '../../shared/hooks/useAuth'
import { RegisterForm } from '../components/RegisterForm'
import { MercuryUserRepository } from '../../../modules/users/infrastructure/MercuryUserRepository'

export const Route = createFileRoute('/register')({
  component: Register,
  beforeLoad: async () => {
    if (isLoggedIn()) {
      throw redirect({
        to: '/',
      })
    }
  },
})

function Register() {
  const repository = new MercuryUserRepository()
  return RegisterForm({ repository })
}

export default Register
