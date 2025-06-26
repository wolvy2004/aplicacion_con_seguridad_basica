<template>
  <h4>Marcas</h4>
  <RouterView />
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'

const route = useRouter()

onMounted(() => {
  route.push({ name: 'marcas_list' })
})
</script>

<style scoped></style>
