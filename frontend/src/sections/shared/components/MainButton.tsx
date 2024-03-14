import { Button } from '@chakra-ui/react'

export function MainButton({
  children,
  isLoading,
}: {
  children: string
  isLoading: boolean
}) {
  return (
    <Button
      bg="ui.main"
      color="white"
      _hover={{ opacity: 0.8 }}
      type="submit"
      isLoading={isLoading}
    >
      {children}
    </Button>
  )
}
