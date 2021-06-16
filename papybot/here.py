import requests
# from papybot.constants import url_request_hereapi, hereapi_key
# #from papybot.utils import cleaned_user_texte
# from papybot.views import ajax
import json


# get API
# def hereapi_get_data():
#     """Launch the API fetch"""
#     url_request_hereapi = 'https://geocode.search.hereapi.com/v1/geocode'
#     products_params = {
#      "q": ['nantes'],
#      "apiKey": "qIsbqNYYlr45pUMK1bQTfa_r5fAi-Q2EbfGRLkgXM9U",
#      "items": "address, position"
#
#      }
#     try:
#
#         request_response = requests.get(url_request_hereapi, products_params)
#         print (request_response)
#         response = json.loads(request_response.text)
#         return response.get()
#         print(response)
#     except Exception as e:
#         raise e



def hereapi_get_data():



    url_request_hereapi = 'https://geocode.search.hereapi.com/v1/geocode'
# url_request_hereapi_auto =
    # 'https://autosuggest.search.hereapi.com/v1/autosuggest'
    # hereapi_key = 'Bn9eoZ-0hBETw8Qs6dUJb3ZcbXl7hoa_AVSNi-9Sf5o'
    products_params = {
                    "q": ['paris'],
                    "apiKey": "f9Sov_GAYZ4n-fzQzXJCY-ykdQB6hnHwPoHEY31z9S8",
                    "items": "address, position"
                    }
    try:

        request_response = requests.get(url_request_hereapi, products_params)
        print(request_response.url)
        print(request_response.text)
        response = json.loads(request_response.text)
        print(response)
        print(type(response))
        print(response["items"])
        print(type(response["items"]))
    # Vérifier si try est vraiment nécessaire et permet d'afficher une erreure en cas
    #de non récuperation d'API'
    except Exception as e:
        raise e


hereapi_get_data()

# def extract_geo_coord(response):
#     """Extraction de coordonnées geo pour wikipedia api"""
#
#     dict_geo_coord = {}
#     for data, type in response.hereapi_get_data():
#         if type == "position":
#             dict_geo_coord[data]
#             print(dict_geo_coord)
#
# extract_geo_coord()
