export const enum Pronoun {
  He = 'he',
  She = 'she',
}

export type User = {
  id: string
  name: string
  lastName: string
  email: string
  password: string
  pronoun: string
}
