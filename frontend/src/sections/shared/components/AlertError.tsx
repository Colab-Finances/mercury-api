import { Alert, AlertIcon, AlertTitle } from '@chakra-ui/react'

export function AlertError({ error }: { error?: { message: string } }) {
  return (
    <>
      {!!error && (
        <Alert status="error">
          <AlertIcon />
          <AlertTitle>{error.message}</AlertTitle>
        </Alert>
      )}
    </>
  )
}
