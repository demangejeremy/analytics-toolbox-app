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
@app.route("/api/idhn_create_account", methods=["POST"])
def idhn():
    # Recupérer données du formulaire
    prenom = escape(request.form['prenom'])
    nom = escape(request.form['nom'])
    email = escape(request.form['email'])
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
    mycol = mydb["pre_inscription_idhn"]
    # Vérifier si le mail n'existe pas
    for x in mycol.find({ "email": email }):
        print(x)
        return jsonify(success="no", message="Votre inscription a déjà été pris en compte. Nous reviendrons vers vous sous peu.")
    mydict = { "prenom": prenom, "nom": nom, "email": email, "date": str(datetime_object)}
    # Ajouter en bdd
    try:
        mycol.insert_one(mydict)
        return jsonify(success="yes", message="Merci pour votre inscription. Votre compte va être validé par un administrateur d'ici quelques jours.")
    except:
        return jsonify(success="no", message="Problème inconnu. Merci de contacter l'administrateur du site.")