import Vue from 'vue'
import Router from 'vue-router'
import Test from '@/components/Test'
import Result from '@/components/Result'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },{
      path: '/test',
      name: 'test',
      component: Test
    },
    {
      path: '/result',
      name: 'result',
      component: Result,
      props: true
    }
  ]
})
