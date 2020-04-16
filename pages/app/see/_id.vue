<template>
  <div>
    <v-container>
      <h1>Dossier</h1>
      <h3>{{ id }}</h3>
      <hr class="mt-6" />
    </v-container>
    <v-container>
      <v-row>
        <v-col class="d-flex justify-start" cols="6">
          <h2>Mes corpus</h2>
        </v-col>
        <v-col class="d-flex justify-end" cols="6">
          <v-btn class="ma-0" tile outlined color="white" @click="addFolder">
            <v-icon left>mdi-plus</v-icon> Ajouter un corpus
          </v-btn>
        </v-col>
      </v-row>
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
              <v-btn
                color="orange"
                to="app/see/tweets-politiques-2020"
                nuxt
                text
              >
                Voir le dossier
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-container class="mt-5">
      <v-row>
        <v-col class="d-flex justify-start" cols="6">
          <h2>Mes analyses</h2>
        </v-col>
        <v-col class="d-flex justify-end" cols="6">
          <v-btn class="ma-0" tile outlined color="white" @click="addFolder">
            <v-icon left>mdi-plus</v-icon> Ajouter une analyse
          </v-btn>
        </v-col>
      </v-row>
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
              <v-btn
                color="orange"
                to="app/see/tweets-politiques-2020"
                nuxt
                text
              >
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
  layout: "app",
  middleware: "auth",

  data: () => ({
    id: ""
  }),

  created() {
    this.test();
  },

  methods: {
    test() {
      this.id = this.$route.params.id;
    }
  }
};
</script>
