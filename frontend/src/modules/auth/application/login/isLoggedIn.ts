import { AuthRepository } from '../../domain/AuthRepository'

export function isLoggedIn(repository: AuthRepository) {
  const credentials = repository.getFromCache()
  return credentials !== null
}
