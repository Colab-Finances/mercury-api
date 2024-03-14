import { Link } from '@chakra-ui/react'
import { Link as RouterLink } from '@tanstack/react-router'

export function RegisterLink() {
  return (
    <Link as={RouterLink} to="/register" color="blue.500">
      Sign Up
    </Link>
  )
}
