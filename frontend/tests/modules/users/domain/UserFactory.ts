import { faker } from '@faker-js/faker'
import { Factory } from 'fishery'
import { Pronoun, User } from '../../../../src/modules/users/domain/User'

const sample = <T>(arr: T[]): T => arr[Math.floor(Math.random() * arr.length)]

export const UserFactory = Factory.define<User>(() => ({
  id: faker.string.uuid(),
  name: faker.person.firstName(),
  lastName: faker.person.lastName(),
  email: faker.internet.email(),
  password: faker.internet.password(),
  pronoun: sample(Object.values(Pronoun)),
}))
