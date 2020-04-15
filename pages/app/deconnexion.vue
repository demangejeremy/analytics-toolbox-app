<template>
  <p>Déconnexion en cours...</p>
</template>

<script>
import { mapMutations } from "vuex";

export default {
  layout: "app",
  middleware: "auth",
  mounted: () => {
    this.$store.commit("connect/no");
    this.$nuxt.$router.replace({ path: "/connexion" });
  }
};
</script>
