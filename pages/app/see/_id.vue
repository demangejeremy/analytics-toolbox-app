<template>
  <div>
    <h1>Bienvenue sur la page {{ id }}</h1>
  </div>
</template>

<script>
export default {
  data: () => ({
    id: ""
  }),

  created() {
    this.test();
  },

  methods: {
    test() {
      this.id = this.$route.params.id;
    }
  }
};
</script>
