from papybot.server.utils import constants


# Fonction qui permet de récuperer le texte et de le renvoyer au
# serveur transformé,
# dans l'exemple ca sera uniquement passage au majuscule minute 36,53
# du webinaire
# Fichier utils qui pemet de travailler le texte pourra être le parser


def get_allowed_text(user_request):
    user_request_list = user_request.split()
    cleaned_user_words_list = list(set(user_request_list) -
                                   set(constants.stopwords_list))
    return ' '.join(cleaned_user_words_list)
