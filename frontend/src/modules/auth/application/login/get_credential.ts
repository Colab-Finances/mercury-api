import { AuthRepository } from '../../domain/AuthRepository'

export function getCredentials(repository: AuthRepository) {
  const credentials = repository.getFromCache()
  // TODO: If credentials are not found, throw an error
  return credentials
}
