from papybot.server.utils import parser_texte
import pytest

def test_parser():
    """ Test from data isolated"""

    question_1 = "a b c v g Paris"
    question_2 = "ah aujourd'hui Nantes"

    assert parser_texte.get_allowed_text(question_1) == ("Paris")
    assert parser_texte.get_allowed_text(question_2) == ("Nantes")
