import { DomainError } from '../../shared/errors/DomainError'
import { User } from './User'

export interface UserRepository {
  register(user: User): Promise<void | DomainError>
}
