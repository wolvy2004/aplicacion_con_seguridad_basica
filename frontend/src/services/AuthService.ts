import { instance as axios } from '@/plugins/axios'
import { type AuthUSer } from '@/interfaces/AuthUser'

class AuthService {
  static async login(auth: AuthUSer) {
    const user = {
      username: auth.username,
      password: auth.password,
    }
    const response = await axios
      .post('/auth/login', user)
      .then((response) => {
        console.log(response.data)
        return response
      })
      .catch((error) => {
        return error
      })
    return response
  }
  static async register(user: AuthUSer) {
    const newUser = {
      username: user.username,
      password: user.password,
      email: user.email,
      rol: user.rol?.id || 1,
    }
    const response = await axios.post('/usuarios/', newUser).catch((error) => {
      alert(error.response.data.mensaje)
    })
    return response
  }
}
export default AuthService
