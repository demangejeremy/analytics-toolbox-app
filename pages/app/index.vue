<template>
  <v-container>
    <h1>Bonjour Linguiste 👋</h1>
    <p class="mt-4">Bienvenue sur l'application Text Analytics Toolbox.</p>
    <p>
      L'application vous permets de gérer vos corpus, de lancer des
      pré-traitements et des analyses de celles-ci dans le cloud ! (et le tout
      sans avoir de connaissances particulières en programmation, eh oui)
    </p>
  </v-container>
</template>

<script>
export default {
  layout: "app",
  middleware: "auth"
};
</script>
