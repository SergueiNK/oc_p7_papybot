import requests
import json
from . import constants

class Hereapi:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Création d\'une instance Hereapi')
            cls._instance = super(Hereapi, cls).__new__(cls)
        return cls._instance

    def hereapi_get_data(self, result_texte):
        # self.request_location = result_texte
        # print(result_texte)

        try:
            self.products_params = {
                "q": f"{result_texte}",
                "apiKey": "f9Sov_GAYZ4n-fzQzXJCY-ykdQB6hnHwPoHEY31z9S8",
                "items": "address, position"
            }
            request_response = requests.get(constants.url_request_hereapi, self.products_params)
            print(request_response.status_code)
            if request_response.status_code == 200:
                response = json.loads(request_response.text)
                items = response.get('items')
                if len(items) > 0:
                    return items[0].get('position')
                else:
                    raise Exception("No results found")
            else:
                raise Exception(f"{request_response.status_code} {request_response.text}")
        # Vérifier si try est vraiment nécessaire
        # et permet d'afficher une erreure en cas
        # de non récuperation d'API'

        except Exception as e:
            raise e

    # def extract_geo_coord(response):
    #  """Extraction de coordonnées geo pour wikipedia api"""
    #     dict_geo_coord = {}
    #     for data, type in response.hereapi_get_data():
    #       if type == "position":
    #         return dict_geo_coord[data]



