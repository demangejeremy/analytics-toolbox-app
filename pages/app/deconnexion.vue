<template>
  <p>Déconnexion en cours...</p>
</template>

<script>
import { mapMutations } from "vuex";
import { mapState } from "vuex";

export default {
  layout: "app",
  mounted() {
    this.$store.commit("connect/no");
    this.$cookies.remove("loginDev", {
      path: "/"
    });
    this.$cookies.remove("sess", {
      path: "/"
    });
    this.$nuxt.$router.replace({ path: "/connexion" });
  }
};
</script>
