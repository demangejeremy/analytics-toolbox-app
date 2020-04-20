#
# Connexion à l'application
#

# Importations
import pymongo
from os import environ 
from flask import Flask
from flask import request
from flask import escape
from flask import jsonify, flash, redirect, url_for
from datetime import datetime  
from datetime import timedelta  
from werkzeug.utils import secure_filename
import os

# Cloudinary
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Json webToken
# import jwt
# import simplejson as json

# Mise en place de l'application
UPLOAD_FOLDER = 'files/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "jjdk,99878990PKLjos"
app.config['SESSION_TYPE'] = 'filesystem'

# Fichiers autorisés
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Retour message inscription
@app.route("/api/import_corpus", methods=["POST"])
def idhn():

    # Recupération du fichier
    # if 'file' not in request.files:
    #     flash('No file part')
    #     return jsonify(success="no", message="Problème, pas de fichier dans la requête.")

    # Prendre le fichier
    file = request.files['file']

    # Fichier vide
    if file.filename == '':
        flash('No selected file')
        return jsonify(success="no", message="Problème, le fichier est vide.")

    # Fichier correct
    if file and allowed_file(file.filename):
        print("ici")
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #lienFile = url_for('uploaded_file', filename=filename)
        print("ici")
        lienFile = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print("là")
    
    # Recupérer données du formulaire
    login = "Linguiste"
    typeTexte = "simple"
    datetime_object = datetime.datetime.now()

    # Enregistrer en BDD
    try:
        myclient = pymongo.MongoClient(environ.get('MONGODB_URL'))
    except:
        print("Connexion impossible à la BDD")
        return jsonify(success="no", message="Problème de connexion en base de données. Merci de contacter l'administrateur du site.")

    # Sauvegarde du fichier
    try:
        cloudinary.uploader.upload(lienFile, 
            folder = "corpus/", 
            public_id = "test",
            overwrite = true, 
            resource_type = "raw")
    except:
        print("Impossible d'envoyer le fichier")
        return jsonify(success="no", message="Impossible d'envoyer le fichier sur le serveur.")


    # Nom de la base
    mydb = myclient["analyticstoolbox"]

    # Sélection de la collection
    mycol = mydb["corpus"]

    # Vérifier si le mail n'existe pas
    # for x in mycol.find({ "email": email }):
    #     print(x)
    #     return jsonify(success="no", message="Votre inscription a déjà été pris en compte. Nous reviendrons vers vous sous peu.")

    # Ajout du contenu
    mydict = { "login": login, "fichier": lienFile, "type": typeTexte, "date": str(datetime_object)}

    # Retour de résultat
    try:
        # Ajout en DB
        mycol.insert_one(mydict)
        return jsonify(success="yes", message="Votre texte a bien été importée")
    except:
        return jsonify(success="no", message="Problème d'ajout en base de données. Merci de contacter l'administrateur du site.")