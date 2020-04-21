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
import calendar
import time

# Mise en place de l'application
app = Flask(__name__)

# Retour message inscription
@app.route("/api/create_analyse", methods=["POST"])
def idhn():
    # Recupérer données du formulaire
    utilisateur = escape(request.form['user'])
    dossier = escape(request.form['dossier'])
    lienAnalyse = escape(request.form['lien'])
    nom = escape(request.form['nom'])
    description = escape(request.form['description'])
    datetime_object = datetime.datetime.now()

    # Enregistrer en BDD
    try:
        myclient = pymongo.MongoClient(environ.get('MONGODB_URL'))
    except:
        print("Connexion impossible à la BDD")
        raise
    mydb = myclient["analyticstoolbox"]
    # Ajouter dans une collection
    mycol = mydb["analyses"]
    # Ajout en dictionnaire
    mydict = { "utilisateur": utilisateur, "dossier": dossier, "lien": lienAnalyse, "nom": nom, "description": description, "date": str(datetime_object)}
    # Ajouter en bdd
    try:
        mycol.insert_one(mydict)
        return jsonify(success="yes", message="L'analyse a bien été générée.")
    except:
        return jsonify(success="no", message="Problème lors de la création de l'analyse.")