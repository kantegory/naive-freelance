import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { BootstrapVue } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from '@/router/index'
import Vuelidate from 'vuelidate'

Vue.config.productionTip = false

// Vue.use section ...
Vue.use(VueAxios, axios)
Vue.use(BootstrapVue)
Vue.use(router)
Vue.use(Vuelidate)

new Vue({
  render: h => h(App),
  router,
  axios
}).$mount('#app')
