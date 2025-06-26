<template>
  <div class="form-container">
    <h3>Nueva Marca</h3>
    <form @submit.prevent="crear">
      <div class="input">
        <label for="">nombre de la marca</label>
        <input type="text" name="" v-model="marca.descripcion" />
      </div>
      <div class="botonera">
        <RouterLink :to="{ name: 'marcas_list' }">volver</RouterLink>
        <button>guardar</button>
      </div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { toRefs } from 'vue'
import useMarcaStore from '../../stores/marcas'

const { marca } = toRefs(useMarcaStore())
marca.value = {
  descripcion: '',
}
const { create } = useMarcaStore()

const crear = async () => {
  if (!marca.value.descripcion) {
    alert('por favor complete el nombre')
  } else {
    const response = await create(marca.value)
    console.log(response)
    marca.value.descripcion = ''

    if (response) {
      alert(response.mensaje)
    }
  }
}
</script>

<style scoped>
.form-container {
  margin: 0 auto;
  background: linear-gradient(#333, #222);
  width: 600px;
  height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
h1,
h2,
h3 {
  color: greenyellow;
  border-bottom: greenyellow 2px solid;
  width: 90%;
  text-align: center;
  margin-bottom: 2rem;
}

.input {
  width: 500px;
  display: flex;
  flex-direction: column;
  input {
    color: #ccc;
    background-color: #5555;
    border: none;
    height: 40px;
    padding: 1rem;
  }
}
button {
  background-color: green;
  border: none;
  padding: 0.5rem;
  margin: 1rem;
  text-transform: uppercase;
  color: white;
  border-radius: 5px;
  width: 50%;
}
a {
  text-align: center;
  padding: 0.25rem;
  background-color: rgb(209, 132, 45);
  border: none;
  margin: 1rem;
  text-transform: uppercase;
  color: white;
  border-radius: 5px;
  width: 50%;
}
.botonera {
  display: flex;
  align-items: center;
}
</style>
