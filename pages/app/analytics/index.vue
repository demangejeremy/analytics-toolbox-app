<template>
  <div>
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
      console.log("Analyse");
    },
    seeLink(item) {
      window.open(item.link, "_blank");
    },
    initialize() {
      this.analyses = [
        {
          name: "Lemmatisation (bêta)",
          type: "Pré-traitement",
          description: "Lemmatisation d'un texte donné.",
          link: "https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer"
        },
        {
          name: "Stop words",
          type: "Pré-traitement",
          description: "Suppression des stop-words inclus dans un texte.",
          link: "https://github.com/Alir3z4/python-stop-words"
        },
        {
          name: "Nuage de mots",
          type: "Analyse",
          description: "Génération d'un nuage de mots (100 mots par défaut).",
          link: "https://github.com/amueller/word_cloud"
        },
        {
          name: "Topic Modelling (NLTK & Gensim)",
          type: "Analyse",
          description:
            "Génération d'un Topic Modelling interactif en HTML avec NLTK & Gensim.",
          link: "https://github.com/RaRe-Technologies/gensim"
        }
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
