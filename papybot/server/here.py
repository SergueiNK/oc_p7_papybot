import requests
from papybot.server.utils import constants
import os


class Hereapi:
    _instance = None

    def __new__(cls):
        """Creating a singleton"""
        if cls._instance is None:
            print('Création d\'une instance Hereapi')
            cls._instance = super(Hereapi, cls).__new__(cls)
        return cls._instance

    def get_coord(self, user_text):
        """
        Send the API request with params.
        Return the API data. Sort the API data.
        """
        key_here = os.environ.get('SECRET_KEY_HERE')
        try:
            self.api_here_params = {
                "q": f"{user_text}",
                "apiKey": f"{key_here}",
            }
            request_response = requests.get(
                constants.url_request_hereapi,
                self.api_here_params
            )

            if request_response.status_code == 200:
                result_json = request_response.json()
                items_list = result_json.get('items')
                if len(items_list) > 0:
                    return items_list[0].get('position'), \
                           items_list[0].get('address').get('label')
                else:
                    raise Exception("No results found")
            else:
                return request_response.status_code
        except Exception as e:
            raise e
