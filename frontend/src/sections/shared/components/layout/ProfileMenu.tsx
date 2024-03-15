import React from 'react'
import {
  Box,
  IconButton,
  Menu,
  MenuButton,
  MenuItem,
  MenuList,
} from '@chakra-ui/react'
import { FaUserAstronaut } from 'react-icons/fa'
import { FiLogOut, FiUser } from 'react-icons/fi'

import { Link } from '@tanstack/react-router'
import { MercuryAuthRepository } from '../../../../modules/auth/infrastructure/MercuryAuthRepository'
import { useLogOut } from '../../../auth/hooks/useLoginForm'

const repository = new MercuryAuthRepository()

const ProfileMenu: React.FC = () => {
  const { onClick } = useLogOut(repository)

  return (
    <>
      <Box
        display={{ base: 'none', md: 'block' }}
        position="fixed"
        top={4}
        right={4}
      >
        <Menu>
          <MenuButton
            as={IconButton}
            aria-label="Options"
            icon={<FaUserAstronaut color="white" fontSize="18px" />}
            bg="ui.main"
            isRound
          />
          <MenuList>
            <MenuItem icon={<FiUser fontSize="18px" />} as={Link} to="settings">
              My profile
            </MenuItem>
            <MenuItem
              icon={<FiLogOut fontSize="18px" />}
              onClick={onClick}
              color="ui.danger"
              fontWeight="bold"
            >
              Log out
            </MenuItem>
          </MenuList>
        </Menu>
      </Box>
    </>
  )
}

export default ProfileMenu
