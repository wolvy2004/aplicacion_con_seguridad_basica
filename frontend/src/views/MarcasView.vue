<template>
  <h4>Modulo Marcas</h4>

  <!-- renderizado del modulo Marcas, lista, create, update, mostrar una en particular-->
  <RouterView />
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'

const route = useRouter()

onMounted(() => {
  //console.log('componente montado')
  route.push({ name: 'marcas_list' })
})
</script>

<style scoped></style>
