from papybot.server.utils import parser_texte


def test_parser():
    """ Test the from isolated data"""

    question_1 = "Salut papy est ce que tu peux " \
                 "m'indiquer où se trouve Paris ? "
    question_2 = "Salut papy je veux aller à Vannes . " \
                 "Est-ce que t'as une adresse ?"
    right_parcing_qestion_1 = "Paris"
    right_parcing_qestion_2 = "Vannes"

    assert parser_texte.get_allowed_text(question_1) == right_parcing_qestion_1
    assert parser_texte.get_allowed_text(question_2) == right_parcing_qestion_2
