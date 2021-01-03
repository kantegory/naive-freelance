<template>
  <b-form @submit="login">
    <div class="form-group">
      <label for="username">Логин:</label>
      <b-input v-model="form.username" type="text" id="username" placeholder="Логин..."></b-input>
    </div>
    <div class="form-group">
      <label for="password">Пароль:</label>
      <b-input v-model="form.password" type="password" id="password" placeholder="Пароль..."></b-input>
    </div>
    <b-button variant="primary" type="submit">Войти</b-button>
    <p class="mt-3">Ещё не зарегистрированы? <router-link to="/auth/signup">Регистрация</router-link>
    </p>
  </b-form>
</template>
<script>
export default {
  name: "SignInForm",
  data() {
    return {
      form: {
        username: "",
        password: ""
      }
    };
  },
  methods: {
    login(event) {
      event.preventDefault();

      // логика авторизации
      this.axios
        .post(`http://localhost:8080/api/auth/token/`, this.form,
        { headers: { 'Content-type': 'application/json' }})
        .then(response => { this.setLogined(response.data.token) })
        .catch(err => { console.error(err) })
    },
    setLogined(token) {

      // сохраняем токен
      console.log(token);
      localStorage.setItem('token', token);
    }
  }
};

</script>
