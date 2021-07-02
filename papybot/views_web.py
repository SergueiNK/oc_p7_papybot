from flask import render_template, request, jsonify, make_response
from papybot import app
from papybot.server.controller import Controller


@app.route("/")
def home():
    return render_template('./index.html')


# Ajout de nouveau route pour gérer
# les appels ajax et envoyer une réponse jsonify


@app.route("/ajax", methods=["GET"])
def ajax():
    controller = Controller()
    # acceder à mes données de formulaire
    # récuperation de données 1ere étape
    # user_text = request.form["userText"]
    user_text = request.args.get('userText')
    paragraph_response = controller.get_query_paragraph_result(user_text)
    coord_response = controller.get_coord_from_here(user_text)
    #print(coord_response)
    #print(type(coord_response))
    #print(paragraph_response)
    #print(type(paragraph_response))
    response = make_response(jsonify(paragraph_response, coord_response))
    print(response.status)
    return response

