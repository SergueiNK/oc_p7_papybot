from .utils import parser_texte
from .here import Hereapi
from papybot.server.wikipedia import Wikiapi


class Controller(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Création d\'une instance Controller')
            cls._instance = super(Controller, cls).__new__(cls)
        return cls._instance

    def get_query_paragraph_result(self, user_text):
        coord = self.get_coord_from_here(user_text)
        if coord in range(201, 599):
            paragraph = 'error'
        else:
            paragraph = self.get_paragraph_from_wiki(coord)
        return paragraph

    def get_coord_from_here(self, user_text):
        here_api = Hereapi()
        result_texte = parser_texte.get_allowed_text(user_text)
        coord = here_api.get_coord(result_texte)
        return coord

    def get_paragraph_from_wiki(self, coord):
        wiki_api = Wikiapi()
        wiki_paragraph = wiki_api.wikipedia_get_article(coord['lat'], coord['lng'])
        # print(wiki_paragraph)
        return wiki_paragraph
