<template>
  <div>
    <v-container>
      <h1>Bonjour Linguiste 👋</h1>
      <p class="mt-4">Bienvenue sur l'application Text Analytics Toolbox.</p>
      <p>
        L'application vous permets de gérer vos corpus, de lancer des
        pré-traitements et des analyses de celles-ci dans le cloud ! (et le tout
        sans avoir de connaissances particulières en programmation, eh oui)
      </p>
      <hr class="mt-6" />
    </v-container>
    <v-container>
      <h2>Mes dossiers</h2>
      <v-row class="mt-8 d-flex justify-start">
        <v-col class="d-flex justify-start" cols="4">
          <v-card class="mx-auto" max-width="400">
            <v-img
              class="white--text align-end"
              height="200px"
              src="/img/tweets-politiques-test.jpg"
              gradient="to bottom left, rgba(100,115,201,.33), rgba(25,32,72,.7)"
            >
              <v-card-title>Tweets politiques 2020</v-card-title>
            </v-img>

            <v-card-text class="text--primary">
              <p>
                Ce dossier est un dossier de test pour vous expliquer le
                fonctionnement de l'application. Il est impossible de supprimer
                ce dossier de votre liste.
              </p>
            </v-card-text>

            <v-card-actions>
              <v-btn color="orange" text>
                Voir le dossier
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  head() {
    return {
      titleTemplate: "Bienvenue - Text Analytics Toolbox"
    };
  },
  layout: "app",
  middleware: "auth"
};
</script>
