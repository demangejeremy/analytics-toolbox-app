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
@app.route("/api/create_dossier", methods=["POST"])
def idhn():
    # Recupérer données du formulaire
    utilisateur = escape(request.form['user'])
    # lienImage = escape(request.form['lien'])
    nom = escape(request.form['nom'])
    description = escape(request.form['description'])
    datetime_object = datetime.datetime.now()
    dossier = str(calendar.timegm(time.gmtime()))

    # Enregistrer en BDD
    try:
        myclient = pymongo.MongoClient(environ.get('MONGODB_URL'))
    except:
        print("Connexion impossible à la BDD")
        print(environ.get('MONGODB_URL'))
        raise
    mydb = myclient["analyticstoolbox"]
    # Ajouter dans une collection
    mycol = mydb["dossiers"]
    # Ajout en dictionnaire
    mydict = { "utilisateur": utilisateur, "dossier": dossier, "nom": nom, "description": description, "date": str(datetime_object)}
    # Ajouter en bdd
    try:
        mycol.insert_one(mydict)
        return jsonify(success="yes", message="Le dossier a bien été crée.")
    except:
        return jsonify(success="no", message="Problème lors de la création du dossier.")