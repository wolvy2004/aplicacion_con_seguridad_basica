<template>
  <main>
    <RouterLink :to="{ name: 'marcas_create' }">crear nueva marca</RouterLink>
    <table>
      <tr>
        <th>id</th>
        <th>Marca</th>
        <th>Acciones</th>
      </tr>
      <tr v-for="marca in marcas" :key="marca.id">
        <td>{{ marca.id }}</td>
        <td>{{ marca.descripcion }}</td>
        <td>
          <router-link :to="{ name: 'marcas_edit', params: { id: marca.id } }">editar</router-link>
          <button @click="eliminar(marca.id as number)">borrar</button>
          <router-link :to="{ name: 'marcas_show', params: { id: marca.id } }">ver</router-link>
        </td>
      </tr>
    </table>
  </main>
</template>
<script setup lang="ts">
import useMarcasStore from '@/stores/marcas'
import { toRefs, onMounted } from 'vue'

const { marcas } = toRefs(useMarcasStore())
const { destroy, getAll } = useMarcasStore()
onMounted(async () => {
  await getAll()
})

const eliminar = async (id: number) => {
  const response = await destroy(id)
  await getAll()
  console.log(response)
}
</script>
<style scoped>
table {
  width: 80%;
  color: red;
}
</style>
