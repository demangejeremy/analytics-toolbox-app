#
# Sauvegarde utilisateurs IDHN
#

# Importations
import pymongo
from os import environ 
from flask import Flask
from flask import request
from flask import escape
from flask import jsonify
import datetime

# Mise en place de l'application
app = Flask(__name__)

# Retour message inscription
@app.route("/api/import_corpus", methods=["POST"])
def idhn():
    # Recupérer données du formulaire
    utilisateur = escape(request.form['user'])
    dossier = escape(request.form['dossier'])
    lienFichier = escape(request.form['lien'])
    nomFichier = escape(request.form['nom'])
    formatFichier = escape(request.form['format'])
    descriptionFichier = escape(request.form['description'])
    datetime_object = datetime.datetime.now()

    # Enregistrer en BDD
    try:
        myclient = pymongo.MongoClient(environ.get('MONGODB_URL'))
    except:
        print("Connexion impossible à la BDD")
        print(environ.get('MONGODB_URL'))
        raise
    mydb = myclient["analyticstoolbox"]
    # Ajouter dans une collection
    mycol = mydb["corpus_texte"]
    # Ajout en dictionnaire
    mydict = { "utilisateur": utilisateur, "dossier": dossier, "lien": lienFichier, "nom": nomFichier, "format": formatFichier, "description": descriptionFichier, "date": str(datetime_object)}
    # Ajouter en bdd
    try:
        mycol.insert_one(mydict)
        return jsonify(success="yes", message="Votre corpus a bien été importé.")
    except:
        return jsonify(success="no", message="Problème inconnu. Merci de contacter l'administrateur du site.")