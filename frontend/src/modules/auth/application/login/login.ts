import { AuthRepository } from '../../domain/AuthRepository'
import { AuthBasic } from './AuthBasic'

export function login(repository: AuthRepository) {
  return async function (data: AuthBasic): Promise<void> {
    const auth_token = await repository.get(data)
    await repository.save(auth_token)
  }
}
