import json
from papybot.data.stopwords import stopwords_list

# Fonction qui permet de récuperer le texte et de le renvoyer au serveur transformé,
#dans l'exemple ca sera uniquement passage au majuscule minute 36,53 du webinaire
# Fichier utils qui pemet de travailler le texte pourra être le parser
#
# def non_match_elements(text, stopwords_list):
#
# 	non_match = []
# 	for item in text:
# 		if item not in stopwords_list:
# 			non_match.append(item)
# 	return non_match
# # non_match = non_match_elements(text, stopwords_list)
# 	print("No match elements: ", non_match)

def get_difference(text):
	# return set(text)-set(stopwords_list)
	#print(type(stopwords_list))
	#print(type(text))
	text_list = text.split()
	print(type(text_list))
	cleaned_user_texte = set(text_list)-set(stopwords_list)
	print (type(cleaned_user_texte))
	return {"texte-original": text, "text-transformed": cleaned_user_texte }
	# non_match = list(get_difference(text, stopwords_list))



# def transform_to_upper(text):
# 	print(text)
# 	# text.upper texte en majiscule
# 	return  {"texte-original": text, "text-transformed": text.upper()}
