import { UserRepository } from '../../../src/modules/users/domain/UserRepository'
import { mock } from 'jest-mock-extended'
import { UserFactory } from '../../modules/users/domain/UserFactory'
import { screen } from '@testing-library/react'
import { RegisterForm } from '../../../src/sections/users/components/RegisterForm'
import React from 'react'
import userEvent from '@testing-library/user-event'
import { renderWithContext } from '../router'

const mockRepository = mock<UserRepository>()

describe('UserRegisterForm', () => {
  it('register a new user when form is submitted', async () => {
    const newUser = UserFactory.build()
    await renderWithContext(() => <RegisterForm repository={mockRepository} />)

    const name = screen.getByLabelText(/First Name/i)
    userEvent.type(name, newUser.name)

    const lastName = screen.getByLabelText(/Last Name/i)
    userEvent.type(lastName, newUser.lastName)

    const email = screen.getByLabelText(/Email/i)
    userEvent.type(email, newUser.email)

    const password = screen.getByLabelText(/^Password$/i)
    userEvent.type(password, newUser.password)

    const she = screen.getByLabelText(/She/i)
    userEvent.click(she)

    const submitButton = await screen.findByRole('button', {
      name: /Register/i,
    })
    userEvent.click(submitButton)
  })
})
