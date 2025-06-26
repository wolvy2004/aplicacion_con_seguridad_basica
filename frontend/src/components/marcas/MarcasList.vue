<template>
  <main>
    <nav>
      <h2>lista de marcas</h2>
      <router-link
        v-if="isAdmin"
        :to="{ name: 'marcas_create' }"
        :style="{ background: 'green', BorderRadius: '5px', padding: '0.5rem', LineHeight: '35px' }"
        ><Icon icon="mdi:plus-circle-outline" width="20" height="20" /> Crear Marca</router-link
      >
    </nav>

    <table>
      <thead>
        <tr>
          <th>id</th>
          <th>descripcion</th>
          <th>acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="marca in marcas" :key="marca.id">
          <td class="col_id">{{ marca.id }}</td>
          <td class="col_des">{{ marca.descripcion }}</td>
          <td class="col_actions">
            <router-link
              v-if="isAdmin"
              :to="{ name: 'marcas_edit', params: { id: marca.id } }"
              :style="{
                background: 'green',
                padding: '0.5rem',
                color: 'white',
                margin: '0.5rem',
                BorderRadius: '5px',
              }"
              ><Icon icon="mdi:edit" width="20" height="20"
            /></router-link>
            <router-link
              :to="{ name: 'marcas_show', params: { id: marca.id } }"
              :style="{
                background: 'blue',
                padding: '0.5rem',
                color: 'white',
                margin: '0.5rem',
                BorderRadius: '5px',
              }"
              ><Icon icon="mdi:show" width="20" height="20"
            /></router-link>
            <button
              v-if="isAdmin"
              @click.prevent="eliminar(marca.id as number)"
              :style="{
                background: 'red',
                padding: '0.25rem',
                color: 'white',
                margin: '0.5rem',
                borderRadius: '5px',
                border: 'none',
              }"
            >
              <Icon icon="mdi:trash" width="20" height="20" />
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </main>
</template>

<script setup lang="ts">
import useMarcasStore from '../../stores/marcas'
import useAuthStore from '@/stores/auth'
import { toRefs, onMounted, computed } from 'vue'

import { Icon } from '@iconify/vue'
const { userAuth } = useAuthStore()
const { marcas } = toRefs(useMarcasStore())
const { getAll, destroy } = useMarcasStore()

const isAdmin = computed(() => {
  return userAuth.rol?.nombre.toLowerCase() == 'admin'
})
onMounted(async () => {
  await getAll()
})

async function eliminar(id: number) {
  if (confirm('desea eliminar el registro numero ' + id + '?')) {
    if (confirm('esta seguro?')) {
      await destroy(id)
      // actualizo las marcas cuando ejecuto este metodo
      await getAll()
    }
  }
}
</script>

<style scoped>
.col_id {
  text-align: center;
  width: 100px;
}
.col_actions {
  width: 200px;
}
main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
table {
  width: 80%;
}
thead th {
  border-bottom: 1px solid rgb(41, 41, 41);
}
</style>
