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
import datetime

# Mise en place de l'application
app = Flask(__name__)

# Retour message inscription
@app.route("/api/connexion", methods=["POST"])
def idhn():
    
    # Recupérer données du formulaire
    login = escape(request.form['login'])
    password = escape(request.form['password'])

    # Retour de résultat
    if login == "Linguiste" and password == "idhn4Ever!":
        return jsonify(success="yes", nom="Linguiste", id=1)
    else:
        return jsonify(success="no")