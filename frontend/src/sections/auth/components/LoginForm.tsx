import {
  Alert,
  AlertIcon,
  AlertTitle,
  Button,
  Center,
  Container,
} from '@chakra-ui/react'
import { useLoginForm } from '../hooks/useLoginForm'
import { AuthRepository } from '../../../modules/auth/domain/AuthRepository'
import { AuthImage } from './AuthImage'
import { PasswordInput } from './PasswordInput'
import { UsernameInput } from './UsernameInput'
import { ForgotPasswordLink } from './ForgotPassworkLink'

export function LoginForm(repository: AuthRepository) {
  const { register, submitForm, errors, isSubmitting } =
    useLoginForm(repository)

  return (
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
      <AuthImage />
      <UsernameInput
        register={register}
        error={errors.username as { message: string } | undefined}
      />
      <PasswordInput register={register} />
      {!!errors.root && (
        <Alert status="error">
          <AlertIcon />
          <AlertTitle>{errors.root.message}</AlertTitle>
        </Alert>
      )}
      <Center>
        <ForgotPasswordLink />
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
  )
}
