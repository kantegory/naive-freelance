<template>
  <div class="w-50 border rounded p-3 mx-auto">
    <b-form @submit="register">
      <div class="form-group">
        <label for="username">Логин:</label>
        <b-input v-model="username" type="text" id="username" placeholder="Логин..."></b-input>
      </div>
      <div class="form-group">
        <label for="phone">Номер телефона:</label>
        <b-input v-model="phone" type="text" id="phone" placeholder="+7 (921) 123 45 67"></b-input>
      </div>
      <div class="form-group">
        <label for="customerOrExecutor">Вы заказчик или исполнитель?</label>
        <b-select v-model="customerOrExecutor" :options="customerOrExecutorOptions" type="customerOrExecutor" id="customerOrExecutor">
        </b-select>
      </div>
      <div class="form-group">
        <label for="password">Пароль:</label>
        <b-input v-model="password" type="password" id="password" placeholder="Пароль..."></b-input>
      </div>
      <div class="form-group">
        <label for="repeatPassword">Повторите пароль:</label>
        <b-input v-model="repeatPassword" type="password" id="repeatPassword" placeholder="Повторите пароль..."></b-input>
      </div>
      <b-button variant="primary" type="submit">Регистрация</b-button>
      <p class="mt-3">Уже есть аккаунт? <router-link to="/auth/signin">Вход</router-link>
      </p>
    </b-form>
  </div>
</template>
<script>
export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      password: "",
      repeatPassword: "",
      phone: "",
      customerOrExecutor: "",
      customerOrExecutorOptions: [
        { text: 'Выберите...', value: '', disabled: true, selected: true },
        { text: 'Заказчик', value: 'customer' },
        { text: 'Исполнитель', value: 'executor' }
      ]
    };
  },
  methods: {
    register(event) {
      event.preventDefault();

      // логика регистрации
      this.axios
        .post(`http://localhost:8000/api/auth/users/`, { headers: {'Content-type': 'application/json'}, 'username': this.username, 'password': this.password })
        .then(response => { console.log(response); this.$router.push('/auth/signin') })
        .catch(err => { console.error(err);
          this.err = err })
    }
  }
};

</script>
<style>
</style>
