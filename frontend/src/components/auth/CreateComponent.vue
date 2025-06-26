<template>
  <div class="container">
    <h3>Registro de Usuarios</h3>
    <form @submit.prevent="registrarUsuario()">
      <div class="input">
        <label for="">ingrese nombre de usuario</label>
        <input type="text" v-model="userAuth.username" />
      </div>
      <div class="input">
        <label for="">ingrese email</label>
        <input type="text" v-model="userAuth.email" />
      </div>
      <div class="input">
        <label for="">selecciona un rol</label>
        <select v-model="userAuth.rol">
          <option value="0" default="true">selecciona un rol</option>
          <option v-for="rol in Roles" :key="rol.id" :value="rol">{{ rol.nombre }}</option>
        </select>
      </div>
      <div class="input">
        <label for="">ingrese su contraseña</label>
        <input type="password" v-model="userAuth.password" />
      </div>

      <button>Registrarse</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import useAuthStore from '@/stores/auth'

import useRolesStore from '@/stores/marcas copy'
import { toRefs, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
const { Roles } = toRefs(useRolesStore())
const { getAll } = useRolesStore()
const { registerUser } = useAuthStore()
const userAuth = ref({
  username: '',
  password: '',
  email: '',
  rol: { nombre: '' },
})

const route = useRouter()
const registrarUsuario = async () => {
  if (
    !userAuth.value.username ||
    !userAuth.value.password ||
    !userAuth.value.rol ||
    !userAuth.value.email
  ) {
    alert('debe completar todos los campos')
  } else {
    const respuesta = await registerUser(userAuth.value)
    console.log(respuesta)
    if (respuesta && respuesta.status == 201) {
      alert(respuesta.data.mensaje)
      setTimeout(() => {}, 500)
      route.push({ name: 'login' })
    }
  }
}
onMounted(async () => {
  await getAll()
})
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
select {
  color: #8f8f8f;
  outline: none;
  border: none;
  padding: 0.5rem;
  background-color: #2f2f2f;
}
option:checked {
  color: red;
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
