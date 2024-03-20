import { UserRepository } from '../domain/UserRepository'
import { User } from '../domain/User'
import { v4 as uuidv4 } from 'uuid'
export type RegisterData = {
  name: string
  lastName: string
  email: string
  password: string
  pronoun: string
}

export function register(repository: UserRepository) {
  return async function (data: RegisterData): Promise<User> {
    const user = { ...data, id: uuidv4() }
    await repository.register(user)
    return user
  }
}
