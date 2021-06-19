from flask import render_template, request
from papybot import app
# from . utils import transform_to_upper
from papybot.server.controller import Controller


@app.route("/")
def home():
    return render_template('./index.html')


# Ajout de nouveau route pour gérer
# les appels ajax et envoyer une réponse jsonify


@app.route("/ajax", methods=["POST"])
def ajax():
    controller = Controller()
    # acceder à mes données de formulaire
    # récuperation de données 1ere étape
    user_text = request.form["userText"]
    paragraph_response = controller.get_query_paragraph_result(user_text)
    return paragraph_response
