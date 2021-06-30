import requests
import json
from papybot.server.utils import constants


class Wikiapi:
    _instance = None
    """
        api wiki
    """
    def __new__(cls):
        if cls._instance is None:
            print('Création d\'une instance Wikiapi')
            cls._instance = super(Wikiapi, cls).__new__(cls)
        return cls._instance

    def wikipedia_get_article(self, latitude, longitude):

        try:
            self.api_wiki_params = {
                "format": "json",
                "action": "query",
                "prop": "extracts|info",
                "inprop": "url",
                "exchars": 400,
                "explaintext": True,
                "exintro": True,
                "generator": "geosearch",
                "exlimit": 1,
                "ggscoord": f"{latitude}|{longitude}"
            }
            request_response = requests.get(
                constants.url_request_wikipedia,
                self.api_wiki_params
            )
            print(request_response.status_code)
            if request_response.status_code == 200:
                return self.extract_wiki_section(
                    json.loads(request_response.text)
                )
            else:
                raise Exception(f"{request_response.status_code} {request_response.text}")
                # return response.status_code
        except Exception as e:
            raise e

    def extract_wiki_section(self, data):
        """Extract the section of taked data"""
        try:
            pages_dict = data.get('query').get('pages')
            for _, page in pages_dict.items():
                return page.get('extract')
        except Exception as e:
            raise e
