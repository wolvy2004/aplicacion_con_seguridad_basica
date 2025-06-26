import type { Rol } from './Rol'

export interface AuthUSer {
  username: string
  password?: string
  email?: string
  jwt?: string
  rol?: Rol
}
