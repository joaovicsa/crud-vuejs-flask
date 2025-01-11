import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/homeview',
      name: 'home',
      component: () => import('@/layouts/default/Default.vue'),
      children: [
        {
          path: '',
          name: 'Home',
          component: () => import('../views/HomeView.vue'),
        },
      ],
    },
    {
      path: '/UsersView',

      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      children: [
        {
          path: '',
          name: 'Users',
          component: () => import('../views/UserView.vue'),
        },
      ],
      component: () => import('@/layouts/default/Default.vue'),
    },
  ],
})

export default router
