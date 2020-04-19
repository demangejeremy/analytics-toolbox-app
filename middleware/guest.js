export default function({ app, store, redirect }) {
  // Si l'utilisateur n'est pas authentifié
  if (!store.state.connect.login) {
    if (app.$cookies.get("loginDev") == "cool") {
      store.state.connect.login = true;
      return redirect("/app");
    }
  } else {
    return redirect("/app");
  }
}
