import {
  Button,
  Center,
  Container,
  FormControl,
  FormErrorMessage,
  Icon,
  Image,
  Input,
  InputGroup,
  InputRightElement,
  Link,
  useBoolean,
} from '@chakra-ui/react'
import { ViewIcon, ViewOffIcon } from '@chakra-ui/icons'
import { Link as RouterLink } from '@tanstack/react-router'
import Logo from '../../../assets/images/fastapi-logo.svg'
import { useLoginForm } from '../hooks/useLoginForm'
import { AuthRepository } from '../../../modules/auth/domain/AuthRepository'

export function LoginForm(repository: AuthRepository) {
  const [show, setShow] = useBoolean()
  const { register, submitForm, errors, isSubmitting } =
    useLoginForm(repository)

  return (
    <>
      <Container
        as="form"
        onSubmit={submitForm}
        h="100vh"
        maxW="sm"
        alignItems="stretch"
        justifyContent="center"
        gap={4}
        centerContent
      >
        <Image
          src={Logo}
          alt="FastAPI logo"
          height="auto"
          maxW="2xs"
          alignSelf="center"
          mb={4}
        />
        <FormControl id="username" isInvalid={!!errors.username}>
          <Input
            id="username"
            {...register('username', {
              pattern: {
                value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i,
                message: 'Invalid email address',
              },
              // onChange: (e) => console.log(e), # TODO: Use with VO
            })}
            placeholder="Email"
            type="email"
          />
          {errors.username && (
            <FormErrorMessage>{errors.username.message}</FormErrorMessage>
          )}
        </FormControl>
        <FormControl id="password" isInvalid={false}>
          <InputGroup>
            <Input
              {...register('password')}
              type={show ? 'text' : 'password'}
              placeholder="Password"
            />
            <InputRightElement
              color="gray.400"
              _hover={{
                cursor: 'pointer',
              }}
            >
              <Icon
                onClick={setShow.toggle}
                aria-label={show ? 'Hide password' : 'Show password'}
              >
                {show ? <ViewOffIcon /> : <ViewIcon />}
              </Icon>
            </InputRightElement>
          </InputGroup>
          <FormErrorMessage>Invalid Credentials</FormErrorMessage>
        </FormControl>
        <Center>
          <Link as={RouterLink} to="/recover-password" color="blue.500">
            Forgot password?
          </Link>
        </Center>
        <Button
          bg="ui.main"
          color="white"
          _hover={{ opacity: 0.8 }}
          type="submit"
          isLoading={isSubmitting}
        >
          Log In
        </Button>
      </Container>
    </>
  )
}
