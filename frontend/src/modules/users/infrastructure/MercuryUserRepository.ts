import { DomainError } from '../../shared/errors/DomainError'
import { RegisterData } from '../application/register'
import { UserRepository } from '../domain/UserRepository'

export class MercuryUserRepository implements UserRepository {
  ACCESS_TOKEN_KEY = 'b28c94fb-178f-4b6c-ad45-5ee8e85829b2'
  API_URL = 'http://localhost:8080'

  async register(data: RegisterData): Promise<void | DomainError> {
    const response = await fetch(`${this.API_URL}/api/v1/sign-up`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ ...data, last_name: data.lastName }),
    })
    if (!response.ok) throw new DomainError('API Error')

    const json = await response.json()
    console.log(json)
  }
}
