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
            Text Analytics Toolbox (actuellement en version bêta), vous permets
            de gérer vos corpus et de lancer des analyses de celles-ci
            directement en ligne. Nous possédons plusieurs serveurs puissants en
            Europe qui vous permettront de générer vos analyses dans le cloud en
            seulement quelques secondes.
          </p>
          <p>
            <b>
              Doctorant de l'IDHN ? Nous vous mettons à disposition cet outil
              gratuitement en ligne pour le temps de vos recherches.</b
            >
          </p>
          <p>
            Notre outil est en Open Source (sous licence MIT). Nous vous
            indiquerons dans quelques semaines comment l'installer sur votre
            propre serveur et nous vous fournirons le code source nécessaire.
          </p>
          <p>
            Pour toute question, merci de contacter Jérémy DEMANGE à cette
            adresse : jeremy (at) fakir.io
          </p>
          <v-btn
            to="/creer-compte-idhn"
            nuxt
            block
            class="mt-8 mb-4"
            color="secondary"
            dark
            >Je suis doctorant à l'IDHN et je souhaite créer un compte
            gratuitement</v-btn
          >
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {};
</script>
