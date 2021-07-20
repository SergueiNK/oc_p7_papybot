from .utils import parser_texte
from .here import Hereapi
from papybot.server.wikipedia import Wikiapi


class Controller(object):
    """
    Dispatch and recover data from here and wikipedia API.
    Send transformed API data to views_web
    """
    _instance = None

    def __new__(cls):
        """Creating a singleton"""
        if cls._instance is None:
            cls._instance = super(Controller, cls).__new__(cls)
        return cls._instance

    def get_query_paragraph_result(self, user_text):
        """
        Take the coord from here. Put that like argument
        to wikipedia. Return the wikipedia paragraph
        """

        coord = self.location_from_here(user_text)[0]

        # Check the status code
        if coord in range(201, 599):
            paragraph = 'error'
        else:
            paragraph = self.get_paragraph_from_wiki(coord)
        return paragraph

    def location_from_here(self, user_text):
        """
        Use parser for clean the user text.
        Send it to here and return location.
        """

        here_api = Hereapi()
        result_texte = parser_texte.get_allowed_text(user_text)
        location = here_api.get_coord(result_texte)
        return location

    def get_paragraph_from_wiki(self, coord):
        """
        Send the coord to wekipedia and return paragraph
        """
        wiki_api = Wikiapi()
        wiki_paragraph = \
            wiki_api.wikipedia_get_article(coord['lat'], coord['lng'])
        return wiki_paragraph

    def get_coord_from_here(self, user_text):
        """
        Take coord from location
        """
        coord = self.location_from_here(user_text)[0]
        return coord

    def get_address_from_here(self, user_text):
        """
        Take address from location
        """
        address = self.location_from_here(user_text)[1]
        return address
