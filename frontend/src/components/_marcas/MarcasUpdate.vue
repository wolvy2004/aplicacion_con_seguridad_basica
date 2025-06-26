<template>
  <main>
    <h2>editar marca</h2>
    <form @submit.prevent="crear">
      <label for="">Nombre de la marca</label>
      <input type="text" v-model="marca.descripcion" />
      <button>enviar</button>
    </form>
  </main>
</template>

<script setup lang="ts">
import useMarcasStore from '@/stores/marcas'
import { useRoute } from 'vue-router'
import { toRefs, onMounted } from 'vue'

const route = useRoute()
const { update, findMarca } = useMarcasStore()
const { marca } = toRefs(useMarcasStore())

onMounted(async () => {
  if (route.params.id) {
    findMarca(parseInt(route.params.id as string))
  }
})

const crear = () => {
  if (marca.value.descripcion) {
    update(marca.value)
  } else {
    alert('el nombre no debe estar vacio')
  }
}
</script>
