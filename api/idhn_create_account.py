#
# Sauvegarde utilisateurs IDHN
#

# Importations
import pymongo
import os
from flask import Flask
from flask import request
from flask import escape
from flask import jsonify
import datetime
from http.server import BaseHTTPRequestHandler
import json
import cgi


class handler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=UTF-8')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()

    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype = cgi.parse_header(self.headers.get('content-type'))
        
        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        # read the message and convert it into a python dictionary
        length = int(self.headers.getheader('content-length'))
        message = json.loads(self.rfile.read(length))

        # Recupérer données du formulaire
        prenom = escape(message['prenom'])
        nom = escape(message['nom'])
        email = escape(message['email'])
        datetime_object = datetime.datetime.now()

        # Enregistrer en BDD
        myclient = pymongo.MongoClient(os.environ['MONGO_URL'])
        mydb = myclient["analyticstoolbox"]

        # Ajouter dans une collection
        mycol = mydb["pre_inscription_idhn"]
        mydict = { "prenom": prenom, "nom": nom, "email": email, "date": str(datetime_object)}

        # Ajouter en bdd
        try:
            mycol.insert_one(mydict)
            result = {"success": "yes", "message": "Merci pour votre inscription. Votre compte va être validé par un administrateur d'ici quelques jours."}
            self._set_headers()
            self.wfile.write(json.dumps(result))
            return

        except:
            result = {"success": "no", "message": "Problème inconnu. Merci de contacter l'administrateur du site."}
            self._set_headers()
            self.wfile.write(json.dumps(result))
            return            
        
        # add a property to the object, just to mess with data
        message['received'] = 'ok'
        
        # send the message back
        self._set_headers()
        self.wfile.write(json.dumps(message))
        return

# # Retour message inscription
# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def idhn():
#     # Recupérer données du formulaire
#     prenom = escape(request.form['prenom'])
#     nom = escape(request.form['nom'])
#     email = escape(request.form['email'])
#     datetime_object = datetime.datetime.now()
#     # Enregistrer en BDD
#     myclient = pymongo.MongoClient(os.environ['MONGO_URL'])
#     mydb = myclient["analyticstoolbox"]
#     # Ajouter dans une collection
#     mycol = mydb["pre_inscription_idhn"]
#     mydict = { "prenom": prenom, "nom": nom, "email": email, "date": str(datetime_object)}
#     # Ajouter en bdd
#     try:
#         mycol.insert_one(mydict)
#         return jsonify(success="yes", message="Merci pour votre inscription. Votre compte va être validé par un administrateur d'ici quelques jours.")
#     except:
#         return jsonify(success="no", message="Problème inconnu. Merci de contacter l'administrateur du site.")