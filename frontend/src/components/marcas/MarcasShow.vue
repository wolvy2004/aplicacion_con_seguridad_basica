<template>
  <div>
    <h3>Detalle de la marca</h3>
    <h3>nombre : {{ marca.descripcion }}</h3>
    <h5>id: {{ marca.id }}</h5>

    <RouterLink :to="{ name: 'marcas_list' }">volver</RouterLink>
  </div>
</template>

<script setup lang="ts">
import { toRefs, onMounted } from 'vue'
import useMarcaStore from '../../stores/marcas'
import { useRoute } from 'vue-router'

const route = useRoute()
const { marca, marcas } = toRefs(useMarcaStore())

onMounted(() => {
  const id = route.params.id
  console.log(id)
  marca.value = marcas.value.find((marca) => marca.id == parseInt(id as string)) ?? {
    descripcion: '',
  }
})
</script>

<style scoped></style>
