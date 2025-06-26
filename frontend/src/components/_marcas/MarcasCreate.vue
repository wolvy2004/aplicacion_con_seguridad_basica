<template>
  <main>
    <h2>crear nueva marca</h2>
    <form @submit.prevent="crear">
      <label for="">Nombre de la marca</label>
      <input type="text" v-model="marca.descripcion" />
      <button>enviar</button>
    </form>
  </main>
</template>

<script setup lang="ts">
import { type Marca } from '@/interfaces/Marca'
import marcas_routes from '@/router/marcas_routes'
import useMarcasStore from '@/stores/marcas'
import { ref } from 'vue'

const marca = ref<Marca>({
  descripcion: '',
})
interface resp {
  mensaje?: string
}
const { create } = useMarcasStore()
const crear = async () => {
  if (marca.value.descripcion) {
    const response: resp | undefined = await create(marca.value)
    marca.value.descripcion = ''
    if (response) alert(response.mensaje)
    console.log(response)
  } else {
    alert('el nombre no debe estar vacio')
  }
}
</script>
