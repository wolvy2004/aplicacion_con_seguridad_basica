const marcas_routes = [
  {
    path: '/marcas',
    name: 'marcas',
    redirect: () => {
      return { path: '/marcas' }
    },

    children: [
      {
        path: '',
        name: 'marcas_list',
        component: () => import('../components/marcas/MarcasList.vue'),
        meta: {
          requiereAuth: true,
        },
      },
      {
        path: ':id/show',
        name: 'marcas_show',
        component: () => import('../components/marcas/MarcasShow.vue'),
        meta: {
          requiereAuth: true,
        },
      },
      {
        path: 'create',
        name: 'marcas_create',
        component: () => import('../components/marcas/MarcasCreate.vue'),
        meta: {
          rol: 'admin',
          requiereAuth: true,
        },
      },
      {
        path: ':id/edit',
        name: 'marcas_edit',
        component: () => import('../components/marcas/MarcasUpdate.vue'),
        meta: {
          rol: 'admin',
          requiereAuth: true,
        },
      },
    ],
  },
]
export default marcas_routes
