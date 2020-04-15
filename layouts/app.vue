<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title v-text="title" />
      <v-spacer />
    </v-app-bar>
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
    <v-footer :fixed="fixed" class="d-flex justify-center" app>
      <span class="caption"
        >&copy; {{ new Date().getFullYear() }} -
        <a href="https://linkedin.com/in/demangejeremy" target="_blank"
          >Jérémy DEMANGE</a
        >
        -
        <a
          href="https://www.u-cergy.fr/fr/laboratoires/idhn.html"
          target="_blank"
          >Laboratoire IDHN</a
        ></span
      >
    </v-footer>
  </v-app>
</template>

<script>
import { mapMutations } from "vuex";
import { mapState } from "vuex";

export default {
  metaInfo: {
    titleTemplate: "%s - Text Analytics Toolbox",
    htmlAttrs: {
      lang: "fr",
      amp: false
    }
  },
  data() {
    return {
      majLog: false,
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: "mdi-apps",
          title: "Dashboard",
          to: "/app"
        },
        {
          icon: "mdi-folder-multiple",
          title: "Créer un dossier",
          to: "/app/folders"
        },
        {
          icon: "mdi-account-plus",
          title: "Se déconnecter",
          to: "/app/deconnexion"
        }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: "Text Analytics Toolbox"
    };
  }
};
</script>
