import { AuthBasic } from '../application/login/AuthBasic'
import { AuthCredential } from './AuthCredential'

export interface AuthRepository {
  get(data: AuthBasic): Promise<AuthCredential | null>
  save(data: AuthCredential): void
  getFromCache(): AuthCredential | null
  remove(): void
}
