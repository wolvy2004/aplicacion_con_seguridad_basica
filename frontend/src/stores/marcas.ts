import type { Marca } from '@/interfaces/Marca'
import { defineStore } from 'pinia'
import ApiService from '@/services/ApiService'
import { ref } from 'vue'

const useMarcasStore = defineStore('marcas', () => {
  const marcas = ref<Array<Marca>>([])
  const marca = ref<Marca>({
    id: 0,
    descripcion: '',
  })
  const url = 'marcas/'

  function findMarca(id: number) {
    const find_marca = marcas.value.find((m) => {
      return m.id == id
    })
    if (find_marca) {
      marca.value = find_marca
    }
  }
  async function getAll() {
    const data = await ApiService.getAll(url)
    if (data) {
      marcas.value = data
    }
  }

  async function getOne(id: number) {
    const data = await ApiService.getOne(url, id)
    if (data) {
      marca.value = data
    }
  }
  async function create(marca: Marca) {
    const response = await ApiService.create(url, marca)
    if (response) {
      return response
    }
  }
  async function update(marca: Marca) {
    if (marca.id) {
      const data = await ApiService.update(url, marca.id, marca)
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
  return { marcas, marca, getAll, getOne, create, destroy, update, findMarca }
})

export default useMarcasStore
