export const state = () => ({
  id: 0,
  prenom: "",
  login: false
});

export const mutations = {
  connect(state, prenom, id) {
    state.id = id;
    state.prenom = prenom;
    state.login = true;
  },
  deconnect(state) {
    state.id = 0;
    state.prenom = "";
    state.login = false;
  }
};
