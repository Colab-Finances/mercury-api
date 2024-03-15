import { Outlet, createFileRoute, redirect } from '@tanstack/react-router'

import Sidebar from '../components/layout/Sidebar'
import UserMenu from '../components/layout/UserMenu'
import { MercuryAuthRepository } from '../../../modules/auth/infrastructure/MercuryAuthRepository'
import { isLoggedIn } from '../../../modules/auth/application/login/isLoggedIn'
import { Flex } from '@chakra-ui/react'

const repository = new MercuryAuthRepository()

export const Route = createFileRoute('/_layout')({
  component: Layout,
  beforeLoad: async () => {
    if (!isLoggedIn(repository)) {
      throw redirect({
        to: '/login',
      })
    }
  },
})

function Layout() {
  return (
    <Flex maxW="large" h="auto" position="relative">
      <Sidebar />
      <Outlet />
      <UserMenu />
    </Flex>
  )
}

export default Layout
