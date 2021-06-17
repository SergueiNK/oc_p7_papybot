from flask import render_template, jsonify, request
from . import app
import json
# from . utils import transform_to_upper
from .controller import Controller



@app.route("/")
def home():
    return render_template("index.html")


# Ajout de nouveau route pour gérer
# les appels ajax et envoyer une réponse jsonify


@app.route("/ajax", methods=["POST"])
def ajax():
    controller = Controller()
    # acceder à mes données de formulaire
    # récuperation de données 1ere étape
    user_text = request.form["userText"]
    response_type = controller.get_result_from_here(user_text)
    # print(str(coord))
    # jsonify pour transformer string en json
    # response_type_json = jsonify(response_type)
    # print(type(response_type_json))
    return response_type
