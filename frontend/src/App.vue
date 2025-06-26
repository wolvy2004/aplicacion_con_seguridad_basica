<template>
  <header>
    <h1><span class="text-greenyellow">Tecno</span>Store</h1>

    <nav>
      <RouterLink :to="{ name: 'home' }">HOME</RouterLink>
      <div v-if="isAuthenticate">
        <RouterLink :to="{ name: 'marcas' }">MARCAS</RouterLink>
        <button
          @click="closeSession"
          :style="{ background: 'none', border: 'none', color: 'greenyellow' }"
        >
          <Icon icon="mdi:logout" width="22px" height="22px" />
        </button>
      </div>
      <div v-else>
        <RouterLink :to="{ name: 'login' }">login</RouterLink>
        <RouterLink :to="{ name: 'register' }">registrarse</RouterLink>
      </div>
    </nav>
  </header>

  <main class="container">
    <RouterView />
  </main>
</template>

<script lang="ts" setup>
import useAuthStore from './stores/auth'
import { Icon } from '@iconify/vue'
import { useRouter } from 'vue-router'
import { toRefs } from 'vue'

const route = useRouter()
const { isAuthenticate } = toRefs(useAuthStore())
const { logout } = useAuthStore()

const closeSession = () => {
  logout()
  route.push({ name: 'login' })
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
header {
  display: flex;
  justify-content: space-between;
  padding: 1rem;
  height: 80px;
  background: rgb(50, 50, 50);
}
.text-greenyellow {
  color: greenyellow;
  font-weight: 900;
  font-size: 2rem;
  margin: 1rem;
}

nav {
  display: flex;
  gap: 1rem;
  justify-content: center;
  align-items: center;
}
</style>
