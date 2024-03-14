import { Link } from '@chakra-ui/react'
import { Link as RouterLink } from '@tanstack/react-router'

export function LoginLink() {
  return (
    <Link as={RouterLink} to="/login" color="blue.500">
      Sign In
    </Link>
  )
}
