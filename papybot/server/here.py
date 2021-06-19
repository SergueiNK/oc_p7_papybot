import requests
import json
from papybot.server.utils import constants


class Hereapi:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Création d\'une instance Hereapi')
            cls._instance = super(Hereapi, cls).__new__(cls)
        return cls._instance

    def get_coord(self, user_text):
        try:
            self.api_here_params = {
                "q": f"{user_text}",
                "apiKey": "f9Sov_GAYZ4n-fzQzXJCY-ykdQB6hnHwPoHEY31z9S8",
                "items": "address, position"
            }
            request_response = requests.get(
                constants.url_request_hereapi,
                self.api_here_params
            )
            print(request_response.status_code)
            if request_response.status_code == 200:
                result_json = json.loads(request_response.text)
                items_list = result_json.get('items')
                if len(items_list) > 0:
                    return items_list[0].get('position')
                else:
                    raise Exception("No results found")
            else:
                raise Exception(f"{request_response.status_code} {request_response.text}")
        except Exception as e:
            raise e
