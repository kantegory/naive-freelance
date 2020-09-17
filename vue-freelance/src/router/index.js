import Vue from 'vue';
import Router from 'vue-router';
import SignIn from '@/components/auth/SignIn';
import SignUp from '@/components/auth/SignUp';

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
