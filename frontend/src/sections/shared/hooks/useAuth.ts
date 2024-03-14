import { useQuery } from 'react-query'
import { useNavigate } from '@tanstack/react-router'

import { UserOut, UsersService } from '../../../client'

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
