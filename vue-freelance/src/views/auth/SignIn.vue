<template>
  <div class="w-25 mx-auto border p-3 rounded">
      <sign-in-form />
  </div>
</template>
<script>
import SignInForm from '@/components/auth/SignInForm.vue'

export default {
  name: "SignIn",

  components: { SignInForm }
}
</script>
