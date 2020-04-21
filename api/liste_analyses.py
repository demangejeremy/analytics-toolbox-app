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
@app.route("/api/liste_analyses", methods=["POST"])
def idhn():
    
    # Recupérer données du formulaire
    login = escape(request.form['user'])
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
    mycol = mydb["analyses"]
    myquery = { "dossier": dossier }
    mydoc = mycol.find(myquery)

    # Stockage
    idc = 0
    content = []

    # Affichage
    print("Avant affichage")
    for x in mydoc:
        content.append({"id": idc, "lien": x["idtxt"], "nom": x["nom"], "description": x["description"]})
        print(content)
        idc += 1

    # Retour de résultat
    return jsonify(success="yes", content=content)