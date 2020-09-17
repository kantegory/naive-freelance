<template>
  <div class="w-25 mx-auto border p-3 rounded">
    <b-form @submit="login">
      <div class="form-group">
        <label for="username">Логин:</label>
        <b-input v-model="username" type="text" id="username" placeholder="Логин..."></b-input>
      </div>
      <div class="form-group">
        <label for="password">Пароль:</label>
        <b-input v-model="password" type="password" id="password" placeholder="Пароль..."></b-input>
      </div>
      <b-button variant="primary" type="submit">Войти</b-button>
      <p class="mt-3">Ещё не зарегистрированы? <router-link to="/auth/signup">Регистрация</router-link>
      </p>
    </b-form>
  </div>
</template>
<script>
export default {
  name: "SignIn",
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    login(event) {
      event.preventDefault();

      // логика авторизации
      this.axios
        .post(`http://localhost:8000/api/auth/token/`, { headers: { 'Content-type': 'application/json' }, 'username': this.username, 'password': this.password })
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
<style>
</style>
