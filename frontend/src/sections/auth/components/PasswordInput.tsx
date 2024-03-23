import {
  FormControl,
  Icon,
  Input,
  InputGroup,
  InputRightElement,
  useBoolean,
} from '@chakra-ui/react'
import { ViewIcon, ViewOffIcon } from '@chakra-ui/icons'
import { UseFormRegister } from 'react-hook-form'

export function PasswordInput({
  register,
}: {
  register: UseFormRegister<any>
}) {
  const [show, setShow] = useBoolean()

  return (
    <FormControl id="password">
      <label htmlFor="password">Password</label>
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
    </FormControl>
  )
}
