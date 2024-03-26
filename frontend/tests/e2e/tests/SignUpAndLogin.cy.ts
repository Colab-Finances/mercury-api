import { UserFactory } from '../../modules/users/domain/UserFactory'

describe('SignUp', () => {
  it('Sign up and login', () => {
    const newUser = UserFactory.build()
    cy.visit('/register')
    cy.findByRole('textbox', { name: /First Name/i }).type(newUser.name)
    cy.findByLabelText(/Last Name/i).type(newUser.lastName)
    cy.findByLabelText(/Email/i).type(newUser.email)
    cy.findByLabelText(/^Password$/i).type(newUser.password)
    cy.findByLabelText(new RegExp(`^${newUser.pronoun}$`, 'i')).click({
      force: true,
    })

    cy.findByRole('button', { name: /Register/i }).click()

    cy.location('pathname').should('eq', '/login')

    cy.findByLabelText(/Email/i).type(newUser.email)
    cy.findByLabelText(/^Password$/i).type(newUser.password)
    cy.findByRole('button', { name: /Login/i }).click()

    cy.location('pathname').should('eq', '/')
  })

  it('Show error when user already exists', () => {
    const newUser = UserFactory.build()
    cy.visit('/register')
    cy.findByRole('textbox', { name: /First Name/i }).type(newUser.name)
    cy.findByLabelText(/Last Name/i).type(newUser.lastName)
    cy.findByLabelText(/Email/i).type(newUser.email)
    cy.findByLabelText(/^Password$/i).type(newUser.password)
    cy.findByLabelText(new RegExp(`^${newUser.pronoun}$`, 'i')).click({
      force: true,
    })
    cy.findByRole('button', { name: /Register/i }).click()
    cy.visit('/register')

    cy.findByRole('textbox', { name: /First Name/i }).type(newUser.name)
    cy.findByLabelText(/Last Name/i).type(newUser.lastName)
    cy.findByLabelText(/Email/i).type(newUser.email)
    cy.findByLabelText(/^Password$/i).type(newUser.password)
    cy.findByLabelText(new RegExp(`^${newUser.pronoun}$`, 'i')).click({
      force: true,
    })

    cy.findByRole('button', { name: /Register/i }).click()
    cy.location('pathname').should('eq', '/register')

    const errorMessage = cy.findByText('User already exists')
    errorMessage.should('exist')
  })
})
