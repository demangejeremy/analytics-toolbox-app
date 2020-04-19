export const state = () => ({
  id: 0,
  prenom: "",
  login: false
});

export const mutations = {
  yes(state, prenom, id) {
    state.id = id;
    state.prenom = prenom;
    state.login = true;
  },
  no(state) {
    state.id = 0;
    state.prenom = "";
    state.login = false;
  }
};

export const getters = {
  login: state => state.login
};
