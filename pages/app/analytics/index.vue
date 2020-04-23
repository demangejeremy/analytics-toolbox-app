<template>
  <div>
    <v-dialog v-model="createAnalytics" persistent max-width="600px">
      <v-card outlined>
        <v-card-title>
          <span class="headline"><b>Ajouter une analyse</b></span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-form ref="form" v-model="validAnalytics" lazy-validation>
              <v-row>
                <v-col cols="12" sm="12">
                  <v-file-input
                    accept=".py,.js"
                    placeholder="Choisissez un fichier de script Python"
                    prepend-icon="mdi-file"
                    label="Fichier Python"
                    v-model="file"
                  ></v-file-input>
                </v-col>
                <v-col cols="12" sm="12">
                  <v-select
                    :items="['Scraping', 'Pré-traitement', 'Analyse']"
                    v-model="typeAnalytics"
                    label="Type d'analyse"
                  ></v-select>
                </v-col>
                <v-col cols="12" sm="12">
                  <v-text-field
                    label="Nom de l'analyse"
                    autocomplete="mnjuio"
                    v-model="nomAnalytics"
                    :counter="30"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="12">
                  <v-text-field
                    label="Description de l'analyse"
                    autocomplete="adp"
                    v-model="descAnalytics"
                    hint="Décrivez très brièvement ce que l'on peut faire avec ce script."
                    :counter="90"
                  ></v-text-field>
                  <v-alert v-if="loading" type="warning" class="mt-5">
                    Le fichier est en cours d'importation. Merci de patienter.
                  </v-alert>
                </v-col>
              </v-row>
            </v-form>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="createAnalytics = false"
            >Fermer</v-btn
          >
          <v-btn color="blue darken-1" :disabled="!validAnalytics" text
            >Créer</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-container>
      <h1>👨🏻‍💻 Analyses</h1>
      <p class="mt-4">
        Vous retrouvez ici une liste d'analyse que vous pourrez utiliser pour
        analyser vos corpus.
      </p>
      <hr class="mt-6" />
    </v-container>
    <v-container>
      <v-row>
        <v-col class="d-flex justify-start" cols="6">
          <h2>Analyses disponibles</h2>
        </v-col>
        <v-col class="d-flex justify-end" cols="6">
          <v-btn class="ma-0" tile outlined color="white" @click="addAnalytics">
            <v-icon left>mdi-plus</v-icon> Ajouter une analyse
          </v-btn>
        </v-col>
      </v-row>
      <v-row class="mt-8 d-flex justify-start">
        <template>
          <v-data-table
            :headers="headers"
            :items="analyses"
            sort-by="calories"
            class="elevation-1"
          >
            <template v-slot:item.actions="{ item }">
              <v-icon small class="ml-1" @click="seeLink(item)">
                mdi-eye
              </v-icon>
            </template>
            <template v-slot:no-data>
              <v-btn color="primary" @click="initialize">Reset</v-btn>
            </template>
          </v-data-table>
        </template>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  head() {
    return {
      titleTemplate: "Liste des analyses - Text Analytics Toolbox"
    };
  },
  layout: "app",
  middleware: "auth",
  data: () => ({
    // Modals
    createAnalytics: false,
    file: null,
    validAnalytics: false,
    typeAnalytics: null,
    loading: false,
    descAnalytics: null,
    nomAnalytics: null,
    typeAnalytics: null,
    // Autre
    dialog: false,
    headers: [
      {
        text: "Nom de l'analyse",
        align: "start",
        sortable: true,
        value: "name"
      },
      { text: "Type", value: "type" },
      { text: "Description courte", value: "description", sortable: false },
      { text: "Voir", value: "actions", sortable: false }
    ],
    analyses: [],
    editedIndex: -1,
    editedItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0
    },
    defaultItem: {
      name: "",
      calories: 0,
      fat: 0,
      carbs: 0,
      protein: 0
    }
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    }
  },

  watch: {
    dialog(val) {
      val || this.close();
    }
  },

  created() {
    this.initialize();
  },

  methods: {
    addAnalytics() {
      this.createAnalytics = true;
    },
    seeLink(item) {
      window.open(item.link, "_blank");
    },
    initialize() {
      this.analyses = [
        // {
        //   name: "Lemmatisation (bêta)",
        //   type: "Pré-traitement",
        //   description: "Lemmatisation d'un texte donné.",
        //   link: "https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer"
        // },
        {
          name: "Stop words",
          type: "Pré-traitement",
          description: "Suppression des stop-words inclus dans un texte.",
          link: "https://github.com/Alir3z4/python-stop-words"
        },
        {
          name: "Fiche de premières statistiques",
          type: "Analyse",
          description: "Informations de base sur le corpus",
          link: "https://github.com/demangejeremy"
        }
        // {
        //   name: "Nuage de mots",
        //   type: "Analyse",
        //   description: "Génération d'un nuage de mots (100 mots par défaut).",
        //   link: "https://github.com/amueller/word_cloud"
        // },
        // {
        //   name: "Topic Modelling (NLTK & Gensim)",
        //   type: "Analyse",
        //   description:
        //     "Génération d'un Topic Modelling interactif en HTML avec NLTK & Gensim.",
        //   link: "https://github.com/RaRe-Technologies/gensim"
        // }
      ];
    },

    editItem(item) {
      this.editedIndex = this.desserts.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    // deleteItem(item) {
    //   const index = this.desserts.indexOf(item);
    //   confirm("Are you sure you want to delete this item?") &&
    //     this.desserts.splice(index, 1);
    // },

    close() {
      this.dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.desserts[this.editedIndex], this.editedItem);
      } else {
        this.desserts.push(this.editedItem);
      }
      this.close();
    }
  }
};
</script>
