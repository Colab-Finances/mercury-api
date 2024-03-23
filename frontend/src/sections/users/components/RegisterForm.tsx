import { Center, Container } from '@chakra-ui/react'
import { AuthImage } from './AuthImage'
import { PasswordInput } from './PasswordInput'
import { EmailInput } from './EmailInput'
import { NameInput } from './NameInput'
import { LastNameInput } from './LastNameInput'
import { PronounInput } from './PronounInput'
import { LoginLink } from './LoginLink'
import { AlertError } from '../../shared/components/AlertError'
import { MainButton } from '../../shared/components/MainButton'
import { useRegisterForm } from '../hooks/useRegisterForm'
import { UserRepository } from '../../../modules/users/domain/UserRepository'

export function RegisterForm({ repository }: { repository: UserRepository }) {
  const { register, submitForm, errors, isSubmitting } =
    useRegisterForm(repository)
  return (
    <Container
      as="form"
      h="100vh"
      maxW="sm"
      alignItems="stretch"
      justifyContent="center"
      gap={4}
      centerContent
      onSubmit={submitForm}
    >
      <AuthImage />
      <NameInput register={register} />
      <LastNameInput register={register} />
      <EmailInput
        register={register}
        error={errors.email as { message: string } | undefined}
      />
      <PasswordInput register={register} />
      <PronounInput register={register} />
      <AlertError error={errors.root as { message: string } | undefined} />
      <Center>
        <LoginLink />
      </Center>
      <MainButton isLoading={isSubmitting}>Register</MainButton>
    </Container>
  )
}
