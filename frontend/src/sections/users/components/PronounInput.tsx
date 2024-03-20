import {
  FormControl,
  FormErrorMessage,
  Radio,
  RadioGroup,
  Stack,
} from '@chakra-ui/react'
import { UseFormRegister } from 'react-hook-form'
import { Pronoun } from '../../../modules/users/domain/User'

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
          {Object.values(Pronoun).map((pronoun) => (
            <Radio {...register('pronoun')} key={pronoun} value={pronoun}>
              {pronoun}
            </Radio>
          ))}
        </Stack>
      </RadioGroup>
      {error && <FormErrorMessage>{error.message}</FormErrorMessage>}
    </FormControl>
  )
}
