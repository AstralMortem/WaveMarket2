import { createRouter, createWebHistory } from 'vue-router'
import index from '../views/index.vue'
import Login from '../views/Login.vue'
import DefaultLayout from "@/layouts/DefaultLayout.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: index,
      meta: {
        layout: DefaultLayout
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    }
  ]
})

export default router
