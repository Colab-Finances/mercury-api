import { AuthBasic } from '../application/login/AuthBasic'
import { AuthCredential } from './AuthCredential'

export interface AuthRepository {
  get(data: AuthBasic): Promise<AuthCredential>
  save(data: AuthCredential): Promise<void>
}
