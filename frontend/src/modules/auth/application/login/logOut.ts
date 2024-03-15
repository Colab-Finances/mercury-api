import { AuthRepository } from '../../domain/AuthRepository'

export function logOut(repository: AuthRepository) {
  repository.remove()
}
