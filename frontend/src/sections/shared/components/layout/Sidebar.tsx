import React from 'react'
import { Box, Flex, Image, Text, useColorModeValue } from '@chakra-ui/react'

import Logo from '../../../../assets/images/fastapi-logo.svg'
import SidebarItems from './SidebarItems'

const Sidebar: React.FC = () => {
  const bgColor = useColorModeValue('ui.white', 'ui.dark')
  const textColor = useColorModeValue('ui.dark', 'ui.white')
  const secBgColor = useColorModeValue('ui.secondary', 'ui.darkSlate')

  return (
    <>
      <Box
        bg={bgColor}
        p={3}
        h="100vh"
        position="sticky"
        top="0"
        display={{ base: 'none', md: 'flex' }}
      >
        <Flex
          flexDir="column"
          justify="space-between"
          bg={secBgColor}
          p={4}
          borderRadius={12}
        >
          <Box>
            <Image src={Logo} alt="Logo" w="180px" maxW="2xs" p={6} />
            <SidebarItems />
          </Box>
          <Text
            color={textColor}
            noOfLines={2}
            fontSize="sm"
            p={2}
            maxW="180px"
          >
            Logged in as: Pedro Perez
          </Text>
        </Flex>
      </Box>
    </>
  )
}

export default Sidebar
