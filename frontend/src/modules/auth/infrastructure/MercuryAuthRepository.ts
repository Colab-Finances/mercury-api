import { AuthBasic } from '../application/login/AuthBasic'
import { AuthRepository } from '../domain/AuthRepository'
import { AuthCredential } from '../domain/AuthCredential'

export class MercuryAuthRepository implements AuthRepository {
  ACCESS_TOKEN_KEY = 'b28c94fb-178f-4b6c-ad45-5ee8e85829b2'
  API_URL = 'http://localhost:8080'

  async get(data: AuthBasic): Promise<AuthCredential | null> {
    const response = await fetch(`${this.API_URL}/api/v1/sign-in`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    })
    if (!response.ok) return null

    const json = await response.json()
    return { accessToken: json.access_token, expiresAt: json.expires_at }
  }

  save(data: AuthCredential): void {
    localStorage.setItem(this.ACCESS_TOKEN_KEY, JSON.stringify(data))
  }

  getFromCache(): AuthCredential | null {
    const item = localStorage.getItem(this.ACCESS_TOKEN_KEY)
    if (item === null) return item
    return JSON.parse(item)
  }

  remove(): void {
    localStorage.removeItem(this.ACCESS_TOKEN_KEY)
  }
}
