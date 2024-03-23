import { Center, Container } from '@chakra-ui/react'
import { useLoginForm } from '../hooks/useLoginForm'
import { AuthRepository } from '../../../modules/auth/domain/AuthRepository'
import { AppImageXL } from '../../shared/components/AppImageXL'
import { PasswordInput } from './PasswordInput'
import { UsernameInput } from './UsernameInput'
import { ForgotPasswordLink } from './ForgotPassworkLink'
import { RegisterLink } from './RegisterLink'
import { AlertError } from '../../shared/components/AlertError'
import { MainButton } from '../../shared/components/MainButton'

export function LoginForm({ repository }: { repository: AuthRepository }) {
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
      <AppImageXL />
      <UsernameInput
        register={register}
        error={errors.username as { message: string } | undefined}
      />
      <PasswordInput register={register} />
      <AlertError error={errors.root as { message: string } | undefined} />
      <Center>
        <ForgotPasswordLink />
      </Center>
      <Center>
        <RegisterLink />
      </Center>
      <MainButton isLoading={isSubmitting}>Login</MainButton>
    </Container>
  )
}
