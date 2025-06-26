<template>
  <div class="container">
    <h3>Ingreso</h3>
    <form @submit.prevent="loguearse()">
      <div class="input">
        <label for="">ingrese nombre de usuario</label>
        <input type="text" v-model="userAuth.username" />
      </div>
      <div class="input">
        <label for="">ingrese su contraseña</label>
        <input type="password" v-model="userAuth.password" />
      </div>

      <button>login</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import useAuthStore from '@/stores/auth'
import { useRouter } from 'vue-router'
import { ref } from 'vue'

const { login } = useAuthStore()
const userAuth = ref({
  username: '',
  password: '',
})

const route = useRouter()

const loguearse = async () => {
  if (!userAuth.value.username || !userAuth.value.password) {
    alert('debe completar todos los campos')
  } else {
    const respuesta = await login(userAuth.value)
    console.log(respuesta)

    if (respuesta.status_code === 200) {
      route.push({ name: 'home' })
    } else {
      alert(respuesta.mensaje)
    }
  }
}
</script>

<style scoped>
.container {
  background: linear-gradient(#232323, #2c2c2c);
  width: 400px;
  height: 100%;
  margin: 0 auto;
  padding: 2rem;
  display: flex;
  flex-direction: column;
}
h3 {
  text-align: center;
  width: 100%;
  color: greenyellow;
  text-transform: uppercase;
  border-bottom: 2px solid greenyellow;
}
form {
  margin: 0 auto;
  display: flex;
  flex-direction: column;
}
.input {
  width: 300px;
  display: flex;
  flex-direction: column;
  margin: 1rem;
  input {
    color: #7b7979;
    outline: none;
    border: none;
    height: 30px;
    padding: 1rem;
    background-color: #2f2f2f;
  }
}
button {
  width: 50%;
  margin: 0 auto;
  height: 40px;
  background-color: green;
  border: none;
  color: greenyellow;
  border-radius: 10px;
}
</style>
