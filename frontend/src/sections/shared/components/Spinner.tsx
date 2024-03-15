import { Flex, Spinner as SpinnerUi } from '@chakra-ui/react'

export function Spinner() {
  return (
    <Flex justify="center" align="center" height="100vh" width="full">
      <SpinnerUi size="xl" color="ui.main" />
    </Flex>
  )
}
