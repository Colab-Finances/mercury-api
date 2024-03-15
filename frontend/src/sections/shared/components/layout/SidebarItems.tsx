import React from 'react'
import { Box, Flex, Icon, Text, useColorModeValue } from '@chakra-ui/react'
import { FiHome } from 'react-icons/fi'
import { MdCategory } from 'react-icons/md'
import { TbMoneybag } from 'react-icons/tb'
import { Link } from '@tanstack/react-router'

const items = [
  { icon: FiHome, title: 'Dashboard', path: '/' },
  { icon: TbMoneybag, title: 'Budgets', path: '/budgets' },
  { icon: MdCategory, title: 'Categories/Tags', path: '/categories' },
]

interface SidebarItemsProps {
  onClose?: () => void
}

const SidebarItems: React.FC<SidebarItemsProps> = ({ onClose }) => {
  const textColor = useColorModeValue('ui.main', 'ui.white')
  const bgActive = useColorModeValue('#E2E8F0', '#4A5568')

  const listItems = items.map((item) => (
    <Flex
      as={Link}
      to={item.path}
      w="100%"
      p={2}
      key={item.title}
      activeProps={{
        style: {
          background: bgActive,
          borderRadius: '12px',
        },
      }}
      color={textColor}
      onClick={onClose}
    >
      <Icon as={item.icon} alignSelf="center" />
      <Text ml={2}>{item.title}</Text>
    </Flex>
  ))

  return (
    <>
      <Box>{listItems}</Box>
    </>
  )
}

export default SidebarItems
