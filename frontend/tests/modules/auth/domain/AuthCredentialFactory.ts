import { faker } from '@faker-js/faker'
import { Factory } from 'fishery'
import { AuthCredential } from '../../../../src/modules/auth/domain/AuthCredential'

export const AuthCredentialFactory = Factory.define<AuthCredential>(() => ({
  accessToken: faker.string.uuid(),
  expiresAt: faker.date.recent(),
}))
