import { Image } from '@chakra-ui/react'
import Logo from '../../../assets/images/fastapi-logo.svg'

export function AuthImage() {
  return (
    <Image
      src={Logo}
      alt="FastAPI logo"
      height="auto"
      maxW="2xs"
      alignSelf="center"
      mb={4}
    />
  )
}
