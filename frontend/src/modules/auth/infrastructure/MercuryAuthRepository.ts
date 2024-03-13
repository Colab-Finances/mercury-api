import { AuthBasic } from '../application/login/AuthBasic'
import { AuthRepository } from '../domain/AuthRepository'
import { AuthCredential } from '../domain/AuthCredential'

export class MercuryAuthRepository implements AuthRepository {
  async get(data: AuthBasic): Promise<AuthCredential> {
    return Promise.resolve({
      token: 'token',
      expires_at: new Date(),
    })
  }

  async save(data: AuthCredential): Promise<void> {
    return Promise.resolve()
  }
}
