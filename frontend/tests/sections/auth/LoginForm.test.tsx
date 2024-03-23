import { AuthRepository } from '../../../src/modules/auth/domain/AuthRepository'
import { mock } from 'jest-mock-extended'
import { UserFactory } from '../../modules/users/domain/UserFactory'
import { screen, waitFor } from '@testing-library/react'
import { LoginForm } from '../../../src/sections/auth/components/LoginForm'
import React from 'react'
import userEvent from '@testing-library/user-event'
import { renderWithContext } from '../router'
import { AuthCredentialFactory } from '../../modules/auth/domain/AuthCredentialFactory'

const mockRepository = mock<AuthRepository>()

describe('LoginForm', () => {
  it('sign in a user when form is submitted', async () => {
    const newUser = UserFactory.build({ pronoun: 'she' })
    const credential = AuthCredentialFactory.build()
    mockRepository.get.mockReturnValue(Promise.resolve(credential))
    await renderWithContext(() => <LoginForm repository={mockRepository} />)

    const email = screen.getByLabelText(/Email/i)
    await userEvent.type(email, newUser.email)

    const password = screen.getByLabelText(/^Password$/i)
    await userEvent.type(password, newUser.password)

    const submitButton = await screen.findByRole('button', {
      name: /Login/i,
    })

    await userEvent.click(submitButton)
    await waitFor(() => {
      expect(mockRepository.get).toHaveBeenCalledWith({
        username: newUser.email,
        password: newUser.password,
      })
      expect(mockRepository.save).toHaveBeenCalledWith(credential)
    })
  })
})
