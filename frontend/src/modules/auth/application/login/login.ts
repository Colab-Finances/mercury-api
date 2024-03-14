import { AuthRepository } from '../../domain/AuthRepository'
import { InvalidCredentials } from '../../domain/errors/InvalidCredentials'
import { AuthBasic } from './AuthBasic'

export function login(repository: AuthRepository) {
  return async function (data: AuthBasic): Promise<void> {
    const auth_token = await repository.get(data)
    if (auth_token === null) throw new InvalidCredentials()
    await repository.save(auth_token)
  }
}
