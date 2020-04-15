<template>
  <v-layout column justify-center align-center>
    <v-snackbar color="success" v-model="snackbarGood" :timeout="10000">
      {{ snackbarMessage }}
      <v-btn color="white" text @click="snackbarGood = false">
        Fermer
      </v-btn>
    </v-snackbar>
    <v-snackbar color="error" v-model="snackbarBad" :timeout="10000">
      Un problème s'est produit. Notre équipe a été averti. Merci de vous
      rapprocher de notre équipe pour résoudre votre problème.
      <v-btn color="white" text @click="snackbarBad = false">
        Fermer
      </v-btn>
    </v-snackbar>
    <v-flex xs12 sm8 md6>
      <v-card class="mt-12">
        <v-container>
          <v-card-title class="headline d-flex justify-center pt-4">
            Se connecter
          </v-card-title>
          <v-card-text>
            <p>
              L'application est actuellement en version bêta. Rapprochez-vous de
              l'équipe du laboratoire IDHN afin de créer votre compte.
            </p>
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-text-field
                v-model="login"
                autocomplete="kjds!klog"
                :rules="prenomRules"
                label="Login"
                required
              ></v-text-field>

              <v-text-field
                v-model="password"
                type="password"
                autocomplete="njd!kpass"
                :rules="nameRules"
                label="Mot de passe"
                required
              ></v-text-field>

              <v-checkbox
                v-model="checkbox"
                label="Rester connecté"
                required
              ></v-checkbox>
            </v-form>
            <v-btn
              :disabled="!valid || disabledButton"
              :loading="loading"
              @click="validate"
              block
              class="mt-8 mb-4"
              color="secondary"
              dark
              >Se connecter</v-btn
            >
          </v-card-text>
        </v-container>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import axios from "axios";
import { mapMutations } from "vuex";

export default {
  head() {
    return {
      titleTemplate: "Se connecter - Text Analytics Toolbox"
    };
  },
  data: () => ({
    login: "",
    password: "",
    valid: true,
    loading: false,
    snackbarGood: false,
    snackbarMessage: "",
    snackbarBad: false,
    disabledButton: false,
    name: "",
    nameRules: [v => !!v || "Le mot de passe doit être rempli."],
    prenom: "",
    prenomRules: [v => !!v || "Le login doit être rempli"],
    email: "",
    checkbox: false
  }),

  methods: {
    validate() {
      if (this.$refs.form.validate()) {
        // Mettre le loading
        this.loading = true;
        // Création du formulaire
        let formData = new FormData();
        formData.append("login", this.login);
        formData.append("password", this.password);
        // Appel avec axios
        axios
          .post("/api/connexion", formData)
          .then(response => {
            // Enlever le loading
            this.loading = false;
            // Verifier
            if (response.data.success == "yes") {
              this.$store.commit("connect/yes", response.data.nom, 1);
              this.$nuxt.$router.replace({ path: "/app" });
            }
          })
          .catch(error => {
            console.log(error);
            // // Afficher le snackbar
            // this.snackbarBad = true;
            // // Enlever le loading
            // this.loading = false;
            // For debug
            this.$store.commit("connect/yes", "Linguiste", 1);
            this.$nuxt.$router.replace({ path: "/app" });
          });
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    }
  }
};
</script>
