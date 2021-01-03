import Vue from 'vue';
import Router from 'vue-router';
import SignIn from '@/views/auth/SignIn';
import SignUp from '@/views/auth/SignUp';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [{
      path: '/auth/signin',
      name: 'SignIn',
      component: SignIn,
    },
    {
      path: '/auth/signup',
      name: 'SignUp',
      component: SignUp,
    },
  ],
});
