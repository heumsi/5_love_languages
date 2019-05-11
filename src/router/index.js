import Vue from 'vue'
import Router from 'vue-router'
import Test from '@/components/Test'
import Result from '@/components/Result'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
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
