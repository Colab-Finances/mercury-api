import {
  FormControl,
  FormErrorMessage,
  Radio,
  RadioGroup,
  Stack,
} from '@chakra-ui/react'
import { UseFormRegister } from 'react-hook-form'

export function PronounInput({
  register,
  error,
}: {
  register: UseFormRegister<any>
  error?: { message: string }
}) {
  return (
    <FormControl id="pronoun" isInvalid={!!error}>
      <RadioGroup>
        <Stack direction="row">
          <Radio {...register('pronoun')} value="he">
            He
          </Radio>
          <Radio {...register('pronoun')} value="she">
            She
          </Radio>
        </Stack>
      </RadioGroup>
      {error && <FormErrorMessage>{error.message}</FormErrorMessage>}
    </FormControl>
  )
}
