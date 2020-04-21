<template>
  <div>
    <v-dialog v-model="affichageWindows" persistent max-width="600px">
      <v-card outlined>
        <v-card-title>
          <span class="headline"><b>Ajouter un nouveau dossier</b></span>
        </v-card-title>
        <v-card-text>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-container>
              <v-row>
                <v-col cols="12" sm="12">
                  <v-file-input
                    :rules="rulesImg"
                    accept="image/png, image/jpeg, image/bmp"
                    placeholder="Choisissez une image d'illustration"
                    prepend-icon="mdi-camera"
                    label="Image d'illustration"
                  ></v-file-input>
                </v-col>
                <v-col cols="12" sm="12">
                  <v-text-field
                    :rules="nomRules"
                    v-model="nom"
                    label="Nom du dossier"
                    autocomplete="mnjuio"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="12">
                  <v-text-field
                    :rules="descRules"
                    v-model="description"
                    label="Description du dossier"
                    autocomplete="adp"
                    hint="Décrivez l'objectif de vos recherches dans ce dossier."
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="affichageWindows = false"
            >Fermer</v-btn
          >
          <v-btn
            color="blue darken-1"
            text
            :disabled="btnDisabled"
            @click="validate"
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
      <div v-if="loadingDossiers">
        <h4>Les dossiers sont en cours de chargement...</h4>
      </div>
      <div v-else>
        <v-row class="mt-8 d-flex justify-start">
          <v-col
            class="d-flex justify-start"
            cols="4"
            v-for="c in dossiers"
            :key="c.id"
          >
            <v-card class="mx-auto" max-width="400">
              <v-img
                class="white--text align-end"
                height="200px"
                src="/img/tweets-politiques-test.jpg"
                gradient="to bottom left, rgba(100,115,201,.33), rgba(25,32,72,.7)"
              >
                <v-card-title>{{ c.nom }}</v-card-title>
              </v-img>

              <v-card-text class="text--primary">
                <p>
                  {{ c.description }}
                </p>
              </v-card-text>

              <v-card-actions>
                <v-btn color="orange" :to="myLink + c.lien" nuxt text>
                  Voir le dossier
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </div>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    // Rules
    myLink: "app/see/",
    loadingDossiers: true,
    dossiers: [],
    rulesImg: [
      value =>
        !value || value.size < 2000000 || "L'image doit être inférieure à 2MB."
    ],
    nom: "",
    btnDisabled: false,
    nomRules: [v => !!v || "Le nom du dossier doit être complété."],
    description: "",
    descRules: [v => !!v || "La description doit être remplie."],
    loading: false,
    affichageWindows: false,
    valid: true
  }),
  head() {
    return {
      titleTemplate: "Bienvenue - Text Analytics Toolbox"
    };
  },
  layout: "app",
  middleware: "auth",
  mounted() {
    this.getFolder();
  },

  methods: {
    getFolder() {
      let formData = new FormData();
      formData.append("user", "Linguiste");
      // Appel avec axios
      axios
        .post("/api/get_dossier", formData)
        .then(response => {
          // Enlever le loading
          console.log(response);
          this.dossiers = response.data.content;
          this.loadingDossiers = false;
        })
        .catch(error => {
          console.log(error);
        });
    },
    addFolder() {
      this.affichageWindows = true;
    },
    validate() {
      if (this.$refs.form.validate()) {
        // Mettre le loading
        this.btnDisabled = true;
        this.loading = true;
        // Création du formulaire
        let formData = new FormData();
        formData.append("user", "Linguiste");
        formData.append("nom", this.nom);
        formData.append("description", this.description);
        // Appel avec axios
        axios
          .post("/api/create_dossier", formData)
          .then(response => {
            // Enlever le loading
            this.loading = false;
            // Verifier
            if (response.data.success == "yes") {
              alert(response.data.message);
              document.location.reload(true);
            } else {
              alert(response.data.message);
              this.btnDisabled = false;
            }
          })
          .catch(error => {
            console.log(error);
            // Afficher le snackbar
            this.snackbarBad = true;
            // Enlever le loading
            this.loading = false;
            // For debug
            // this.$store.commit("connect/yes", "Linguiste", 1);
            // this.$nuxt.$router.replace({ path: "/app" });
          });
      }
    }
  }
};
</script>
