import requests
import json
from papybot.server.utils import constants
import os


class Hereapi:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Création d\'une instance Hereapi')
            cls._instance = super(Hereapi, cls).__new__(cls)
        return cls._instance

    def get_coord(self, user_text):
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
            # print(request_response.url)
            # print(request_response.status_code)
            if request_response.status_code == 200:
                # print(request_response)
                # print(type(request_response.text))
                # result_json = json.loads(request_response.text)
                result_json = request_response.json()
                # print(result_json)
                items_list = result_json.get('items')
                # print(items_list)
                if len(items_list) > 0:
                    # print(items_list[0].get('position'))
                    # print(items_list[0].get('address').get('label'))
                    # print(type(items_list[0].get('position')))
                    # print(type(items_list[0].get('address').get('label')))
                    return items_list[0].get('position'), items_list[0].get('address').get('label')
                else:
                    raise Exception("No results found")
            else:
                return request_response.status_code
        except Exception as e:
            raise e


