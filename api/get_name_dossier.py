#
# Connexion à l'application
#

# Importations
import pymongo
from os import environ 
from flask import Flask
from flask import request
from flask import escape
from flask import jsonify
from datetime import datetime  
from datetime import timedelta  

# Json webToken
# import jwt
# import simplejson as json

# Mise en place de l'application
app = Flask(__name__)

# Retour message inscription
@app.route("/api/get_name_dossier", methods=["POST"])
def idhn():
    
    # Recupérer données du formulaire
    identifiant = escape(request.form['id'])

    # Enregistrer en BDD
    try:
        myclient = pymongo.MongoClient(environ.get('MONGODB_URL'))
    except:
        print("Connexion impossible à la BDD")
        print(environ.get('MONGODB_URL'))
        raise

    # Lien BDD
    mydb = myclient["analyticstoolbox"]

    # Ajouter dans une collection
    mycol = mydb["dossiers"]
    myquery = { "dossier": identifiant }
    mydoc = mycol.find(myquery)

    # Stockage
    nomDossier = ""

    # Affichage
    print("Avant affichage")
    for x in mydoc:
        nomDossier = x["nom"]

    # Retour de résultat
    return jsonify(success="yes", nom=nomDossier)