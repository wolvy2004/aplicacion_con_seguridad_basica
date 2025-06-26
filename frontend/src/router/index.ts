import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import marcas_routes from './marcas_routes'
import useAuthStore from '@/stores/auth'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      requiereAuth: false,
    },
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/components/auth/LoginComponent.vue'),
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/components/auth/CreateComponent.vue'),
  },
  ...marcas_routes,
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  const { isAuthenticate, userAuth } = useAuthStore()

  // Si la ruta requiere autenticación y no está autenticado
  if (to.meta.requiereAuth && !isAuthenticate) {
    return next({ name: 'login' })
  }

  // Si la ruta tiene una restricción de rol y el rol no coincide
  if (to.meta.rol && userAuth?.rol?.nombre?.toLowerCase() !== to.meta.rol) {
    if (from.name) {
      console.log('Rol no permitido, volviendo a la página anterior')
      return next({ name: from.name })
    } else {
      // Si no hay página anterior, redirigimos al home por seguridad
      console.log('Rol no permitido, no hay página anterior, redirigiendo al home')
      return next({ name: 'home' })
    }
  }

  next() // Permite la navegación
})

export default router
