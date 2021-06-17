
from . import parser_texte
from .here import Hereapi

class Controller(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Création d\'une instance Controller')
            cls._instance = super(Controller, cls).__new__(cls)
        return cls._instance

    def get_result_from_here(self, user_text):
        here_api = Hereapi()
        result_texte = parser_texte.get_difference(user_text)
        print(result_texte)
        coord = here_api.hereapi_get_data(result_texte)
        print(coord)
        return coord
