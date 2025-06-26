import type { Rol } from '@/interfaces/Rol'
import { defineStore } from 'pinia'
import ApiService from '@/services/ApiService'
import { ref } from 'vue'

const useRolesStore = defineStore('Roles', () => {
  const Roles = ref<Array<Rol>>([])
  const Rol = ref<Rol>({
    id: 0,
    nombre: '',
  })
  const url = 'roles/'

  function findRol(id: number) {
    const find_Rol = Roles.value.find((m) => {
      return m.id == id
    })
    if (find_Rol) {
      Rol.value = find_Rol
    }
  }
  async function getAll() {
    const data = await ApiService.getAll(url)
    if (data) {
      Roles.value = data
    }
  }

  async function getOne(id: number) {
    const data = await ApiService.getOne(url, id)
    if (data) {
      Rol.value = data
    }
  }
  async function create(Rol: Rol) {
    const response = await ApiService.create(url, Rol)
    if (response) {
      return response
    }
  }
  async function update(Rol: Rol) {
    if (Rol.id) {
      const data = await ApiService.update(url, Rol.id, Rol)
      if (data) {
        return data
      }
    }
  }
  async function destroy(id: number) {
    const data = await ApiService.destroy(url, id)
    if (data) {
      return data
    }
  }
  return { Roles, Rol, getAll, getOne, create, destroy, update, findRol }
})

export default useRolesStore
