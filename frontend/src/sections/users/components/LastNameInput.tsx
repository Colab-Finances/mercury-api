import { FormControl, FormErrorMessage, Input } from '@chakra-ui/react'
import { UseFormRegister } from 'react-hook-form'

export function LastNameInput({
  register,
  error,
}: {
  register: UseFormRegister<any>
  error?: { message: string }
}) {
  return (
    <FormControl id="last_name" isInvalid={!!error}>
      <label htmlFor="last_name">Last Name</label>
      <Input
        id="last_name"
        {...register('last_name')}
        placeholder="Last Name"
        type="text"
      />
      {error && <FormErrorMessage>{error.message}</FormErrorMessage>}
    </FormControl>
  )
}
