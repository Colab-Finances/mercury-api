import { FormControl, FormErrorMessage, Input } from '@chakra-ui/react'
import { UseFormRegister } from 'react-hook-form'

export function NameInput({
  register,
  error,
}: {
  register: UseFormRegister<any>
  error?: { message: string }
}) {
  return (
    <FormControl id="name" isInvalid={!!error}>
      <Input id="name" {...register('name')} placeholder="Name" type="text" />
      {error && <FormErrorMessage>{error.message}</FormErrorMessage>}
    </FormControl>
  )
}
