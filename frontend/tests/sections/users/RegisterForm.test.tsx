import { UserRepository } from '../../../src/modules/users/domain/UserRepository'
import { mock } from 'jest-mock-extended'
import { UserFactory } from '../../modules/users/domain/UserFactory'
import { screen, waitFor } from '@testing-library/react'
import { RegisterForm } from '../../../src/sections/users/components/RegisterForm'
import React from 'react'
import userEvent from '@testing-library/user-event'
import { renderWithContext } from '../router'
import { anyUuid } from '../../modules/matchers/uuidMatcher'
const mockRepository = mock<UserRepository>()

describe('UserRegisterForm', () => {
  it('register a new user when form is submitted', async () => {
    const newUser = UserFactory.build({ pronoun: 'she' })
    await renderWithContext(() => <RegisterForm repository={mockRepository} />)

    const name = screen.getByRole('textbox', { name: /First Name/i })
    await userEvent.type(name, newUser.name)

    const lastName = screen.getByLabelText(/Last Name/i)
    await userEvent.type(lastName, newUser.lastName)

    const email = screen.getByLabelText(/Email/i)
    await userEvent.type(email, newUser.email)

    const password = screen.getByLabelText(/^Password$/i)
    await userEvent.type(password, newUser.password)

    const she = screen.getByLabelText(/She/i)
    await userEvent.click(she)

    const submitButton = await screen.findByRole('button', {
      name: /Register/i,
    })
    await userEvent.click(submitButton)

    await waitFor(() => {
      expect(mockRepository.register).toHaveBeenCalledWith({
        ...newUser,
        id: anyUuid,
      })
    })
  })
})
