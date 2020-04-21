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
@app.route("/api/liste_corpus", methods=["POST"])
def idhn():
    
    # Recupérer données du formulaire
    login = escape(request.form['login'])
    dossier = escape(request.form['dossier'])

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
    mycol = mydb["corpus_texte"]
    myquery = { "utilisateur": login, "dossier": dossier }

    # Stockage
    lien = []
    nom = []
    description = []

    # Affichage
    for x in mycol.find(myquery):
        print(x)
        lien.append(x["lien"])
        nom.append(x["nom"])
        description.append(x["description"])

    # Retour de résultat
    return jsonify(success="yes", lien=lien, description=description, nom=nom)