from flask import render_template, request, jsonify, make_response
from papybot import app
from papybot.server.controller import Controller


@app.route("/")
def home():
    """Defined the route for homepage"""
    return render_template('./index.html')


@app.route("/ajax", methods=["GET"])
def ajax():
    """Defined the route for the API request return"""
    controller = Controller()
    # Take the user data from formular
    user_text = request.args.get('userText')
    # Take the return tranformed API data from Controller
    paragraph_response = controller.get_query_paragraph_result(user_text)
    coord_response = controller.get_coord_from_here(user_text)
    address_response = controller.get_address_from_here(user_text)
    # Return the response object json
    response = make_response(jsonify(paragraph_response, coord_response,
                                     address_response))

    return response
