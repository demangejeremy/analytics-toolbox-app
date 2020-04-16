<template>
  <p>Déconnexion en cours...</p>
</template>

<script>
import { mapMutations } from "vuex";
import { mapState } from "vuex";

export default {
  layout: "app",
  middleware: "auth",
  mounted() {
    this.$cookies.set("loginDev", "no", {
      path: "/",
      maxAge: 60 * 60 * 24 * 7
    });
    this.$nuxt.$router.replace({ path: "/connexion" });
  }
};
</script>
