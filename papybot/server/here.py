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
            print(request_response.url)
            # print(request_response.status_code)
            if request_response.status_code == 200:
                result_json = json.loads(request_response.text)
                print(result_json)
                items_list = result_json.get('items')
                print(items_list)
                # print(items_list)
                if len(items_list) > 0:
                    return items_list[0].get('position'), items_list[0].get('address').get('label')
                else:
                    raise Exception("No results found")
            else:
                return request_response.status_code
        except Exception as e:
            raise e


