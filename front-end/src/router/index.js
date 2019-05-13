import Vue from 'vue'
import Router from 'vue-router'
import Test from '@/components/Test'
import Result from '@/components/Result'
import Home from '@/components/Home'
import Survey from '@/components/Survey'

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
    },{
      path: '/survey',
      name: 'survey',
      component: Survey,
      props: true
    },{
      path: '/result',
      name: 'result',
      component: Result,
      props: true
    }
  ]
})
