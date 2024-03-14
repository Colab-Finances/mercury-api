import { DomainError } from '../../../shared/errors/DomainError'

export class InvalidCredentials extends DomainError {
  constructor() {
    super('Invalid credentials')
  }
}
