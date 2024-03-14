import { useQuery } from 'react-query'
import { useNavigate } from '@tanstack/react-router'

import { UserOut, UsersService } from '../../../client'
import { login } from '../../../modules/auth/application/login/login'
import { AuthRepository } from '../../../modules/auth/domain/AuthRepository'
import { AuthBasic } from '../../../modules/auth/application/login/AuthBasic'

const isLoggedIn = () => {
  return localStorage.getItem('access_token') !== null
}

const useAuth = () => {
  const navigate = useNavigate()
  const { data: user, isLoading } = useQuery<UserOut | null, Error>(
    'currentUser',
    UsersService.readUserMe,
    {
      enabled: isLoggedIn(),
    },
  )

  const logout = () => {
    localStorage.removeItem('access_token')
    navigate({ to: '/login' })
  }

  return { logout, user, isLoading }
}

export { isLoggedIn }
export default useAuth

export function useLogin(repository: AuthRepository) {
  return async function (data: AuthBasic) {
    await login(repository)(data)
  }
}
