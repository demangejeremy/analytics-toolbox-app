<template>
  <div>
    <v-dialog v-model="affichageWindows" persistent max-width="600px">
      <v-card outlined>
        <v-card-title>
          <span class="headline"><b>Ajouter un nouveau dossier</b></span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="12">
                <v-text-field
                  label="Nom du dossier"
                  autocomplete="mnjuio"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="12">
                <v-text-field
                  label="Description du dossier"
                  autocomplete="adp"
                  hint="Décrivez l'objectif de vos recherches dans ce dossier."
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="affichageWindows = false"
            >Fermer</v-btn
          >
          <v-btn color="blue darken-1" text @click="affichageWindows = false"
            >Créer</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-container>
      <h1>Bonjour Linguiste 👋</h1>
      <p class="mt-4">Bienvenue sur l'application Text Analytics Toolbox.</p>
      <p>
        L'application vous permets de gérer vos corpus, de lancer des
        pré-traitements et des analyses de celles-ci dans le cloud.
      </p>
      <hr class="mt-6" />
    </v-container>
    <v-container>
      <v-row>
        <v-col class="d-flex justify-start" cols="6">
          <h2>Mes dossiers</h2>
        </v-col>
        <v-col class="d-flex justify-end" cols="6">
          <v-btn class="ma-0" tile outlined color="white" @click="addFolder">
            <v-icon left>mdi-plus</v-icon> Ajouter un dossier
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
  data: () => ({
    affichageWindows: false
  }),
  head() {
    return {
      titleTemplate: "Bienvenue - Text Analytics Toolbox"
    };
  },
  layout: "app",
  middleware: "auth",
  methods: {
    addFolder() {
      this.affichageWindows = true;
    }
  }
};
</script>
