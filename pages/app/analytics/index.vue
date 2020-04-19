<template>
  <h1>Les analyses</h1>
</template>

<script>
export default {
  head() {
    return {
      titleTemplate: "Liste des analyses - Text Analytics Toolbox"
    };
  },
  layout: "app",
  middleware: "auth"
};
</script>
