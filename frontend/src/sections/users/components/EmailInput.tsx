import { FormControl, FormErrorMessage, Input } from '@chakra-ui/react'
import { UseFormRegister } from 'react-hook-form'

export function EmailInput({
  register,
  error,
}: {
  register: UseFormRegister<any>
  error?: { message: string }
}) {
  return (
    <FormControl id="email" isInvalid={!!error}>
      <Input
        id="email"
        {...register('email', {
          pattern: {
            value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i,
            message: 'Invalid email address',
          },
          // onChange: (e) => console.log(e), # TODO: Use with VO
        })}
        placeholder="Email"
        type="email"
      />
      {error && <FormErrorMessage>{error.message}</FormErrorMessage>}
    </FormControl>
  )
}
