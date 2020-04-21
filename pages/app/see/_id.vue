<template>
  <div>
    <v-dialog v-model="viewCorpus" persistent max-width="500px">
      <v-card outlined class="bgc-white">
        <v-card-title>
          <span class="headline"><b>Corpus de test</b></span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <iframe
              src="https://res.cloudinary.com/fakir/raw/upload/v1586659293/1578865117_hd25ry.txt"
              width="100%"
              height="500px"
              frameborder="0"
            ></iframe>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="viewCorpus = false"
            >Fermer</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="viewAnalyse" persistent max-width="800px">
      <v-card outlined class="bgc-white">
        <v-card-title>
          <span class="headline"><b>Nuage de mots</b></span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <iframe
              src="https://res.cloudinary.com/fakir/image/upload/v1587354613/analytics-toolbox/1_x_oWNj934KrGaEDsN6J3jw_uv2unn.png"
              width="1000"
              height="500"
              frameborder="0"
            ></iframe>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="viewAnalyse = false"
            >Fermer</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="createCorpus" persistent max-width="600px">
      <v-card outlined>
        <v-card-title>
          <span class="headline"><b>Ajouter un nouveau corpus</b></span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <form @submit.prevent="formAddCorpus">
              <v-row>
                <v-col cols="12" sm="12">
                  <v-file-input
                    :rules="rulesFile"
                    accept=".txt"
                    placeholder="Choisissez un fichier texte"
                    prepend-icon="mdi-file"
                    label="Fichier texte"
                    v-model="file"
                  ></v-file-input>
                </v-col>
                <v-col cols="12" sm="12">
                  <v-select
                    :items="['Fichier texte simple', 'Fichier format iramuteq']"
                    v-model="typeFile"
                    label="Format du fichier"
                  ></v-select>
                </v-col>
                <v-col cols="12" sm="12">
                  <v-text-field
                    label="Nom du fichier"
                    autocomplete="mnjuio"
                    v-model="nomFile"
                    :counter="30"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="12">
                  <v-text-field
                    label="Description du fichier"
                    autocomplete="adp"
                    v-model="descriptionFile"
                    hint="Décrivez ce que l'on peut trouver dans le fichier texte."
                    :counter="150"
                  ></v-text-field>
                </v-col>
              </v-row>
            </form>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeCorpus">Fermer</v-btn>
          <v-btn color="blue darken-1" text @click="submitFile">Créer</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="createAnalyse" persistent max-width="600px">
      <v-card outlined>
        <v-card-title>
          <span class="headline"><b>Ajouter une nouvelle analyse</b></span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12" sm="12">
                <v-select
                  :items="listeCorpus"
                  label="Sélectionner le fichier corpus à analyser"
                ></v-select>
              </v-col>
              <v-col cols="12" sm="12">
                <v-select
                  v-model="selectedPretraitements"
                  :items="pretraitements"
                  label="Sélectionner les prétraitements"
                  multiple
                >
                  <template v-slot:prepend-item>
                    <v-list-item ripple @click="toggle">
                      <v-list-item-action>
                        <v-icon
                          :color="
                            selectedPretraitements.length > 0
                              ? 'indigo darken-4'
                              : ''
                          "
                          >{{ icon }}</v-icon
                        >
                      </v-list-item-action>
                      <v-list-item-content>
                        <v-list-item-title>Tout sélectionner</v-list-item-title>
                      </v-list-item-content>
                    </v-list-item>
                    <v-divider class="mt-2"></v-divider>
                  </template>
                  <template v-slot:append-item>
                    <v-divider class="mb-2"></v-divider>
                    <v-list-item disabled>
                      <v-list-item-avatar color="dark lighten-3">
                        <v-icon>mdi-chart-bar</v-icon>
                      </v-list-item-avatar>

                      <v-list-item-content v-if="likesAllFruit">
                        <v-list-item-title
                          >Vous avez sélectionné tous les
                          pré-traitements</v-list-item-title
                        >
                      </v-list-item-content>

                      <v-list-item-content v-else-if="likesSomeFruit">
                        <v-list-item-title
                          >Nombre d'éléments sélectionnés
                        </v-list-item-title>
                        <v-list-item-subtitle>{{
                          selectedPretraitements.length
                        }}</v-list-item-subtitle>
                      </v-list-item-content>

                      <v-list-item-content v-else>
                        <v-list-item-title>
                          À vous de choisir
                        </v-list-item-title>
                        <v-list-item-subtitle>
                          Choisissez les pré-traitements qui vous conviennent.
                        </v-list-item-subtitle>
                      </v-list-item-content>
                    </v-list-item>
                  </template>
                </v-select>
              </v-col>
              <v-col cols="12" sm="12">
                <v-select
                  :items="['Nuage de mots', 'Topic Modelling (NLTK & Gensim)']"
                  label="Sélectionner l'analyse à réaliser après pré-traitements"
                ></v-select>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeAnalyse">Fermer</v-btn>
          <v-btn color="blue darken-1" text @click="closeAnalyse">Créer</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-container>
      <h1>Dossier</h1>
      <!-- <h3>{{ id }}</h3> -->
      <hr class="mt-6" />
    </v-container>
    <v-container>
      <v-row>
        <v-col class="d-flex justify-start" cols="6">
          <h2>Mes corpus</h2>
        </v-col>
        <v-col class="d-flex justify-end" cols="6">
          <v-btn class="ma-0" tile outlined color="white" @click="newCorpus">
            <v-icon left>mdi-plus</v-icon> Ajouter un corpus
          </v-btn>
        </v-col>
      </v-row>
      <v-row class="mt-8 d-flex justify-start">
        <div v-if="loadingCorpus">
          <h4>Liste des corpus en cours de chargement...</h4>
        </div>
        <div v-if="corpus">
          <v-col
            class="d-flex justify-start"
            cols="4"
            v-for="c in corpus"
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
                <v-btn color="orange" text @click="viewCorpus = true">
                  Voir le corpus
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </div>
        <div class="mb-5" v-else>
          <h2>Aucun dossier crée</h2>
        </div>
      </v-row>
    </v-container>
    <v-container class="mt-5">
      <v-row>
        <v-col class="d-flex justify-start" cols="6">
          <h2>Mes analyses</h2>
        </v-col>
        <v-col class="d-flex justify-end" cols="6">
          <v-btn class="ma-0" tile outlined color="white" @click="newAnalyse">
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
              <v-card-title
                >Mots les plus fréquents <br />/ Nuage de mots</v-card-title
              >
            </v-img>

            <v-card-text class="text--primary">
              <p>
                Première analyse.
              </p>
            </v-card-text>

            <v-card-actions>
              <v-btn color="orange" text @click="viewAnalyse = true">
                Voir l'analyse
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  layout: "app",
  middleware: "auth",

  data: () => ({
    // Affichage des corpus
    listeCorpus: [],
    loadingCorpus: true,
    corpus: [],
    // Affichage des analyses
    analyses: [],
    // Id de la page
    id: "",
    // Liste pré-traitements
    pretraitements: ["Lemmatisation", "Stop words"],
    selectedPretraitements: [],
    // Liste analyses
    analyses: ["Nuage de mots", "Topic Modelling (NLTK & Gensim)"],
    selectedAnalyses: [],
    // Fichiers
    typeFile: null,
    nomFile: null,
    descriptionFile: null,
    // Formulaires
    fileUpload: null,
    formData: null,
    fileContents: null,
    results: null,
    errors: [],
    file: null,
    filesSelected: 0,
    cloudName: "",
    preset: "",
    tags: "browser-upload",
    progress: 0,
    showProgress: false,
    // Modals
    createCorpus: false,
    createAnalyse: false,
    viewCorpus: false,
    viewAnalyse: false,
    // Rules
    rulesFile: [
      value =>
        !value ||
        value.size < 2000000 ||
        "La taille du fichier doit être inférieure à 2MB."
    ]
  }),

  head() {
    return {
      titleTemplate: this.id + " - Text Analytics Toolbox"
    };
  },

  created() {
    this.test();
  },

  computed: {
    likesAllFruit() {
      return this.selectedPretraitements.length === this.pretraitements.length;
    },
    likesSomeFruit() {
      return this.selectedPretraitements.length > 0 && !this.likesAllFruit;
    },
    icon() {
      if (this.likesAllFruit) return "mdi-close-box";
      if (this.likesSomeFruit) return "mdi-minus-box";
      return "mdi-checkbox-blank-outline";
    }
  },

  mounted() {
    this.getCorpus();
  },

  methods: {
    getCorpus() {
      let formData = new FormData();
      formData.append("user", "Linguiste");
      formData.append("dossier", this.id);
      // Appel avec axios
      axios
        .post("/api/liste_corpus", formData)
        .then(response => {
          // Traitement en API
          console.log(response.data);
          this.corpus = response.data.content;
          this.loadingCorpus = false;
          for (let i = 0; i < response.data.content.length; i++) {
            console.log("Hello !");
            this.listeCorpus.push(response.data.content[i].nom);
          }
          // Fin de traitement en API
        })
        .catch(error => {
          alert(error2.data);
          this.loadingCorpus = false;
        });
    },
    formAddCorpus() {
      console.log("test");
      this.upload();
    },
    toggle() {
      this.$nextTick(() => {
        if (this.likesAllFruit) {
          this.selectedPretraitements = [];
        } else {
          this.selectedPretraitements = this.pretraitements.slice();
        }
      });
    },
    submitFile() {
      this.upload();
    },
    test() {
      this.id = this.$route.params.id;
    },
    newCorpus() {
      this.createCorpus = true;
    },
    closeCorpus() {
      this.createCorpus = false;
    },
    newAnalyse() {
      this.createAnalyse = true;
    },
    closeAnalyse() {
      this.createAnalyse = false;
    },
    upload: function() {
      if (true) {
        // Mettre le loading
        this.loading = true;
        // Création du formulaire
        let formData = new FormData();
        formData.append("importer-texte", this.file);
        // Appel avec axios
        axios
          .post(
            "https://demangejeremy.pythonanywhere.com/importer-texte-idhn",
            formData
          )
          .then(response => {
            // Traitement en API
            console.log(response.data);
            formData = new FormData();
            formData.append("user", "Linguiste");
            formData.append(
              "lien",
              `https://demangejeremy.pythonanywhere.com/static/idhn/${response.data.name}.txt`
            );
            formData.append("nom", this.nomFile);
            formData.append("dossier", this.id);
            formData.append("format", this.typeFile);
            formData.append("description", this.descriptionFile);
            // Appel avec axios
            axios
              .post("/api/import_corpus", formData)
              .then(response2 => {
                // Traitement en API
                console.log(response2.data);
                alert(response2.data.message);
                document.location.reload(true);
                // Fin de traitement en API
              })
              .catch(error2 => {
                alert(error2.data);
              });
            // Fin de traitement en API
          })
          .catch(error => {
            alert(error.data);
          });
      }
    }
  }
};
</script>

<style scoped>
.bgc-white {
  background-color: #fff;
  color: black;
}
</style>
