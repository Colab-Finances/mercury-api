import { Link } from '@chakra-ui/react'
import { Link as RouterLink } from '@tanstack/react-router'

export function ForgotPasswordLink() {
  return (
    <Link as={RouterLink} to="/recover-password" color="blue.500">
      Forgot password?
    </Link>
  )
}
