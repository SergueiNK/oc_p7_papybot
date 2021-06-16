import json
from papybot.data.stopwords import stopwords_list

# Fonction qui permet de récuperer le texte et de le renvoyer au serveur transformé,
#dans l'exemple ca sera uniquement passage au majuscule minute 36,53 du webinaire
# Fichier utils qui pemet de travailler le texte pourra être le parser

def get_difference(user_request):

	user_request_list = user_request.split()
	print(type(user_request_list))
	cleaned_user_texte = list(set(user_request_list)-set(stopwords_list))
	print(type(cleaned_user_texte))
	return json.dumps({"texte-original": user_request, "text-transformed": cleaned_user_texte })


