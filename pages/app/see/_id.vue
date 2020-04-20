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
                  <!-- <v-file-input
                    :rules="rulesFile"
                    accept=".txt"
                    placeholder="Choisissez un fichier texte"
                    prepend-icon="mdi-file"
                    label="Fichier texte"
                    ref="file"
                    @change="handleFileUpload()"
                  ></v-file-input> -->
                  <input
                    type="file"
                    accept=".txt"
                    ref="file"
                    @change="handleFileUpload()"
                  />
                </v-col>
                <v-col cols="12" sm="12">
                  <v-select
                    :items="['Fichier texte simple', 'Fichier format iramuteq']"
                    label="Format du fichier"
                  ></v-select>
                </v-col>
                <v-col cols="12" sm="12">
                  <v-text-field
                    label="Nom du fichier"
                    autocomplete="mnjuio"
                    :counter="30"
                    required
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="12">
                  <v-text-field
                    label="Description du fichier"
                    autocomplete="adp"
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
                  :items="['Corpus de test']"
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
      <h3>{{ id }}</h3>
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
        <v-col class="d-flex justify-start" cols="4">
          <v-card class="mx-auto" max-width="400">
            <v-img
              class="white--text align-end"
              height="200px"
              src="/img/tweets-politiques-test.jpg"
              gradient="to bottom left, rgba(100,115,201,.33), rgba(25,32,72,.7)"
            >
              <v-card-title>Corpus de test</v-card-title>
            </v-img>

            <v-card-text class="text--primary">
              <p>
                Premier corpus de texte.
              </p>
            </v-card-text>

            <v-card-actions>
              <v-btn color="orange" text @click="viewCorpus = true">
                Voir le corpus
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
    id: "",
    // Liste pré-traitements
    pretraitements: ["Lemmatisation", "Stop words"],
    selectedPretraitements: [],
    // Liste analyses
    analyses: ["Nuage de mots", "Topic Modelling (NLTK & Gensim)"],
    selectedAnalyses: [],
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

  methods: {
    formAddCorpus() {
      console.log("test");
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
    prepareFormData: function() {
      this.formData = new FormData();
      this.formData.append("upload_preset", "test");
      this.formData.append("tags", "browser-upload"); // Optional - add tag for image admin in Cloudinary
      this.formData.append("file", this.fileUpload);
    },
    handleFileUpload() {
      console.log("Fichier modifié...");
      console.log(this.$refs);
      console.log(this.$refs.file.files[0]);
      this.fileUpload = this.$refs.file.files[0];
      // for (let myvar in this.$refs.file.files) {
      //   console.log("Un petit tour.");
      //   this.fileUpload = myvar;
      // }
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
      let reader = new FileReader();
      // attach listener to be called when data from file
      reader.addEventListener(
        "load",
        function() {
          this.fileContents = reader.result;
          this.prepareFormData();
          let cloudinaryUploadURL = `https://api.cloudinary.com/v1_1/fakir/upload`;
          let requestObj = {
            url: cloudinaryUploadURL,
            method: "POST",
            data: this.formData,
            onUploadProgress: function(progressEvent) {
              console.log("progress", progressEvent);
              this.progress = Math.round(
                (progressEvent.loaded * 100.0) / progressEvent.total
              );
              console.log(this.progress);
              //bind "this" to access vue state during callback
            }.bind(this)
          };
          //show progress bar at beginning of post
          this.showProgress = true;
          axios(requestObj)
            .then(response => {
              this.results = response.data;
              console.log(this.results);
              console.log("public_id", this.results.public_id);
            })
            .catch(error => {
              this.errors.push(error);
              console.log(this.error);
            })
            .finally(() => {
              setTimeout(
                function() {
                  this.showProgress = false;
                }.bind(this),
                1000
              );
            });
        }.bind(this),
        false
      );
      // call for file read if there is a file
      if (this.file && this.file.name) {
        reader.readAsDataURL(this.file);
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
