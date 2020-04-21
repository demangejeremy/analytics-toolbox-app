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
    dossier = escape(request.form['dossier'])
    corpus = escape(request.form['corpus'])
    pre = escape(request.form['pre'])
    analyse = escape(request.form['analyse'])
    description = "À partir du corpus " + corpus
    datetime_object = datetime.datetime.now()

    # Enregistrer en BDD
    try:
        myclient = pymongo.MongoClient(environ.get('MONGODB_URL'))
    except:
        print("Connexion impossible à la BDD")
        raise

    # Lien BDD
    mydb = myclient["analyticstoolbox"]

    # Récupérer lien corpus
    mycol = mydb["corpus_texte"]
    myquery = { "dossier": dossier, "nom": corpus }
    mydoc = mycol.find(myquery)

    # Stockage
    identifAnalyse = ""

    # Affichage
    print("Avant affichage")
    for x in mydoc:
        identifAnalyse = x["idtxt"]

    # Ajout en dictionnaire
    mycol = mydb["analyses"]
    mydict = { "dossier": dossier, "nom": "Fiche de première analyse", "corpus": corpus, "pre": pre, "description": description, "idtxt": identifAnalyse, "date": str(datetime_object)}

    # Ajouter en bdd
    try:
        mycol.insert_one(mydict)
        return jsonify(success="yes", message="L'analyse a bien été générée.")
    except:
        return jsonify(success="no", message="Problème lors de la création de l'analyse.")