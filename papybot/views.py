from flask import render_template, jsonify, request
from . import app
import json
# from . utils import transform_to_upper
from . utils import get_difference
@app.route("/")
def home():
    return render_template("index.html")


# Ajout de nouveau route pour gérer les appels ajax et envoyer une réponse jsonify


@app.route("/ajax", methods=["POST"])
def ajax():
    # acceder à mes données de formulaire
    # récuperation de données 1ere étape
    user_text = request.form["userText"]
    #print(type(user_text))
    # response = transform_to_upper(user_text)
    response = get_difference(user_text)
    #print(type(response))
    #jsonpickle pour transformer set en python, mais en réalité ça fait un string
    response_type = json.loads(response)
    #print(type(response_type))
    print (response_type)
    # jsonify pour transformer string en json
    # response_type_json = jsonify(response_type)
    # print(type(response_type_json))
    #return jsonify(response)
    #return jsonpickle.encode(response)
    return response_type

