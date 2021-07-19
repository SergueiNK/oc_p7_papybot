from papybot.server.utils import parser_texte


def test_parser():
    """ Test from data isolated"""

    question_1 = "Salut papy est ce que tu peux m'indiquer où se trouve Paris ? "
    question_2 = "Salut papy je veux aller à Vannes . Est-ce que t'as une adresse ?"

    assert parser_texte.get_allowed_text(question_1) == ("Paris")
    assert parser_texte.get_allowed_text(question_2) == ("Vannes")
