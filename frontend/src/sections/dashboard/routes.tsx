import { Box, Container, Text } from '@chakra-ui/react'
import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/')({
  component: Dashboard,
})

function Dashboard() {
  return (
    <>
      <Container maxW="full">
        <Box pt={12} m={4}>
          <Text fontSize="2xl">Hi 👋🏼</Text>
          <Text>Welcome bak, nice t see you again!</Text>
        </Box>
      </Container>
    </>
  )
}

export default Dashboard
