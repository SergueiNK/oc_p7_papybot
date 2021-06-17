import requests
import json


class Wikiapi:
    """
        api wiki
    """
    def __init__(self):

        self.url_request_wikipedia = 'https://fr.wikipedia.org/w/api.php'
        self.products_params = {
            "format": "json",
            "action": "query",
            "prop": "extracts|info",
            "inprop": "url",
            "exchars": 400,
            "explaintext": True,
            "generator": "geosearch",
            "ggscoord": "48.85717|2.3414",

        }
        self.wikipedia_get_data()

    def wikipedia_get_data(self):


        try:

            request_response = requests.get(self.url_request_wikipedia, self.products_params)
            print(request_response.url)
            print(request_response.text)
            response = json.loads(request_response.text)
            print(response)

        except Exception as e:
            raise e

    wikipedia_get_data()

    def extract_wiki_section(self):
        """Extract the section of taked data"""
        pass
