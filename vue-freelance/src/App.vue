<template>
  <div id="app">
    <header class="bg-dark">
      <b-navbar class="w-75 mx-auto" type="dark" variant="dark">
        <b-navbar-brand>Naive freelance</b-navbar-brand>
        <b-navbar-nav>
          <b-nav-item href="#">Главная</b-nav-item>
          <b-nav-item href="#">Заказы</b-nav-item>
          <b-nav-item href="#">Услуги</b-nav-item>
          <b-nav-item href="#">О нас</b-nav-item>
        </b-navbar-nav>
      </b-navbar>
    </header>
    <div class="container-fluid my-5">
      <router-view />
    </div>
    <footer>
      <b-jumbotron bg-variant="dark" text-variant="white">
        <div class="w-75 mx-auto">
          <div class="row">
            <div class="col-4 text-left">© Naive freelance, 2020</div>
            <div class="col-4 text-center">Контакты</div>
            <div class="col-4 text-right">О нас</div>
          </div>
        </div>
      </b-jumbotron>
    </footer>
  </div>
</template>
<script>
export default {
  name: 'App',
};

</script>
<style>
.navbar,
.navbar-brand {
  font-size: 16pt;
}

footer {
  font-size: 20pt;
}

</style>
