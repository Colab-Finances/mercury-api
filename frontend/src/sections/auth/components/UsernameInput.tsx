import { FormControl, FormErrorMessage, Input } from '@chakra-ui/react'
import { UseFormRegister } from 'react-hook-form'

export function UsernameInput({
  register,
  error,
}: {
  register: UseFormRegister<any>
  error?: { message: string }
}) {
  return (
    <FormControl id="username" isInvalid={!!error}>
      <label htmlFor="username">Email</label>
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
      {error && <FormErrorMessage>{error.message}</FormErrorMessage>}
    </FormControl>
  )
}
