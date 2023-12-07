// Composables
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/Home.vue'
import Users from '@/views/UsersView.vue'
import Applications from '@/views/ApplicationsView.vue'
import Roles from '@/views/RolesView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
  },
  {
    path: '/users',
    name: 'Users',
    component: Users,
  },
  {
    path: '/applications',
    name: 'Applications',
    component: Applications,
  },
  {
    path: '/roles',
    name: 'Roles',
    component: Roles,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
