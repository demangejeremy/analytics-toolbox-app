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
import jwt
import simplejson as json

# Mise en place de l'application
app = Flask(__name__)

# Retour message inscription
@app.route("/api/connexion", methods=["POST"])
def idhn():
    
    # Recupérer données du formulaire
    login = escape(request.form['login'])
    password = escape(request.form['password'])

    # Récupérer date
    date = str(datetime.now() + timedelta(days=1))
    print("Actual date: " + str(datetime.now()))
    print(date)

    # Générer le web Token
    encoded = jwt.encode({'usr': login, 'dt': date}, environ.get('JWT_TOKEN'), algorithm='HS256')

    # Retour de résultat
    if login == "Linguiste" and password == "idhn4Ever!":
        return jsonify(success="yes", nom="Linguiste", id=1, token=encoded)
    elif login == "julien" and password == "idhn2020#":
        return jsonify(success="yes", nom="Julien", id=1, token=encoded)
    elif login == "jeremy" and password == "idhn2020#":
        return jsonify(success="yes", nom="Jérémy", id=1, token=encoded)
    else:
        return jsonify(success="no")