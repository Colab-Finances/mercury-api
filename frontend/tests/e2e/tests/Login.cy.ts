import { UserFactory } from '../../modules/users/domain/UserFactory'

describe('Login', () => {
  it('Invalid Credentials', () => {
    const newUser = UserFactory.build()
    cy.visit('/login')

    cy.findByLabelText(/Email/i).type(newUser.email)
    cy.findByLabelText(/^Password$/i).type(newUser.password)
    cy.findByRole('button', { name: /Login/i }).click()

    cy.location('pathname').should('eq', '/login')
    cy.findByText('Invalid credentials').should('exist')
  })
})
