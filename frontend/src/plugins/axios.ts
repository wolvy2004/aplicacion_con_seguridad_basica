import axios from 'axios'
import type { InternalAxiosRequestConfig } from 'axios'
import useAuthStore from '@/stores/auth'

export const instance = axios.create({
  baseURL: 'http://localhost:5000/api_v1/',
  timeout: 1000,
})

// para que no haya una importancion ciclica vamos a utilizar
// interceptores para que cuando se envie use el jwt,
// use otra manera de acceder al atributo
instance.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    const store = useAuthStore()
    if (config.headers && store.userAuth) {
      config.headers.Authorization = 'Bearer ' + store.userAuth.jwt
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  },
)
