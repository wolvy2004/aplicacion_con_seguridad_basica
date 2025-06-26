import { defineStore } from 'pinia'
import { type AuthUSer } from '@/interfaces/AuthUser'
import AuthService from '@/services/AuthService'
import { ref } from 'vue'

const useAuthStore = defineStore(
  'auth',
  () => {
    const userAuth = ref<AuthUSer>({
      username: '',
      email: '',
      jwt: '',
      rol: { nombre: '' },
    })
    const isAuthenticate = ref(false)

    async function login(authUser: AuthUSer) {
      const response = await AuthService.login(authUser)

      if (response.message) {
        return { mensaje: 'error conectando con el servidor', status_code: 500 }
      }
      if (response.data.status_code === 200) {
        userAuth.value = {
          username: response.data.username,
          email: response.data.email,
          jwt: response.data.jwt,
          rol: response.data.rol,
        }
        isAuthenticate.value = true
        console.log(userAuth.value)
        return { mensaje: 'todo correcto', status_code: response.data.status_code }
      } else {
        userAuth.value = {
          username: '',
          password: '',
          rol: { nombre: '' },
        }

        return {
          mensaje: 'error en credenciales, acceso denegado',
          status_code: 401,
        }
      }
    }
    async function registerUser(user: AuthUSer) {
      const response = await AuthService.register(user)
      return response
    }
    function logout() {
      userAuth.value = {
        username: '',
        password: '',
        email: '',
        jwt: '',
        rol: { nombre: '' },
      }
      isAuthenticate.value = false
    }
    return { userAuth, isAuthenticate, login, logout, registerUser }
  },
  {
    persist: true,
  },
)

export default useAuthStore
