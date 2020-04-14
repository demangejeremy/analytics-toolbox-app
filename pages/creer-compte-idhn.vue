<template>
  <v-layout column justify-center align-center>
    <v-flex xs12 sm8 md6>
      <div class="text-center mt-12">
        <h1>Text Analytics Toolbox</h1>
        <h3>
          Des analyses de textes simplifiées et générées en quelques secondes
          dans le cloud
        </h3>
      </div>
      <v-card class="mt-12">
        <v-card-title class="headline d-flex justify-center pt-4">
          🎉 Text Analytics Toolbox x IDHN 🎉
        </v-card-title>
        <v-card-text>
          <p>
            Doctorant de l'IDHN ? Créez votre compte maintenant pour accéder à
            cette application en libre accès pour le temps de vos recherches.
          </p>
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="prenom"
              autocomplete="kjds!k"
              :counter="15"
              :rules="prenomRules"
              label="Prénom"
              required
            ></v-text-field>

            <v-text-field
              v-model="name"
              autocomplete="njd!k"
              :counter="30"
              :rules="nameRules"
              label="Nom"
              required
            ></v-text-field>

            <v-text-field
              v-model="email"
              autocomplete="m!k"
              :rules="emailRules"
              label="E-mail"
              required
            ></v-text-field>

            <v-checkbox
              v-model="checkbox"
              :rules="[
                v =>
                  !!v || 'Vous devez accepter les conditions pour poursuivre.'
              ]"
              label="J'accepte que les données ci-dessus soient traitées par Jérémy DEMANGE ou par l'équipe du laboratoire IDHN."
              required
            ></v-checkbox>
          </v-form>
          <v-btn
            :disabled="!valid"
            @click="validate"
            block
            class="mt-8 mb-4"
            color="secondary"
            dark
            >Je crée mon compte maintenant</v-btn
          >
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    valid: true,
    name: "",
    nameRules: [
      v => !!v || "Votre nom",
      v =>
        (v && v.length <= 30) || "Le nom doit être inférieur à 30 caractères."
    ],
    prenom: "",
    prenomRules: [
      v => !!v || "Votre prénom",
      v =>
        (v && v.length <= 15) ||
        "Le prénom doit être inférieur à 15 caractères."
    ],
    email: "",
    emailRules: [
      v => !!v || "Le champs e-mail est requis.",
      v => /.+@.+\..+/.test(v) || "L'adresse e-mail doit être valide."
    ],
    checkbox: false
  }),

  methods: {
    validate() {
      if (this.$refs.form.validate()) {
        // Création du formulaire
        let formData = new FormData();
        formData.append("prenom", this.prenom);
        formData.append("nom", this.name);
        formData.append("email", this.email);
        // Appel avec axios
        axios
          .post("/api/idhn_create_account", formData)
          .then(response => {
            alert(response.data.message);
          })
          .catch(error => {
            console.log(error);
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
