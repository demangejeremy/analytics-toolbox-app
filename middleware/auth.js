export default function({ store, redirect }) {
  // Si l'utilisateur n'est pas authentifié
  if (!store.state.connect.login) {
    return redirect("/connexion");
  }
}
