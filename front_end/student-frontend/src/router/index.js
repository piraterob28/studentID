import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/student-list',
    name: 'student-list',
    component: () => import('../views/Students.vue')
  },
  {
    path: '/housing',
    name: 'housing',
    component: () => import('../views/Housing.vue')
  },
  {
    path: '/departments',
    name: 'departments',
    component: () => import('../views/Departments.vue')
  },
  {
    path: '/Student-add',
    name: 'Student-add',
    component: () => import('../views/Student-add.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
}

)
export default router
