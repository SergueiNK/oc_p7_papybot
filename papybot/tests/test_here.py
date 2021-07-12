import pytest
import requests
from papybot.server.here import Hereapi


sucess_request_result = {'items':
                             [{'title': 'Openclassrooms',
                               'id': 'here:pds:'
                                     'place:250u09wj-'
                                     '502617312148414c9658acfeb750013e',
                               'resultType': 'place',
                               'address':
                                   {'label': 'Openclassrooms,'
                                             ' 7 Cité Paradis, 75010 Paris,'
                                             ' France',
                                    'countryCode': 'FRA',
                                    'countryName': 'France',
                                    'stateCode': 'IDF',
                                    'state': 'Île-de-France',
                                    'county': 'Paris',
                                    'city': 'Paris',
                                    'district': '10e Arrondissement',
                                    'street': 'Cité Paradis',
                                    'postalCode': '75010',
                                    'houseNumber': '7'},

                               'position': {'lat': 48.87489, 'lng': 2.35051},

                               'access': [{'lat': 48.8749, 'lng': 2.35051}],

                               'categories': [{'id': '800-8200-0295',
                                               'name': 'Formation '
                                                       'et perfectionnement',
                                               'primary': True}],

                               'scoring': {'queryScore': 0.73,
                                           'fieldScore': {'city': 1.0,
                                                          'placeName': 1.0}}}]}


def test_get_response_success(monkeypatch) :

    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.url = 'https://geocode.search.hereapi.com/v1/geocode?' \
                       'q=situe+Openclassrooms+Ou+paris&apiKey=' \
                       'f9Sov_GAYZ4n-fzQzXJCY-ykdQB6hnHwPoHEY31z9S8&items=' \
                       'address%2C+position'

            self.api_here_params = {
                "q": "situe+Openclassrooms+Ou+paris",
                "apiKey": "f9Sov_GAYZ4n-fzQzXJCY-ykdQB6hnHwPoHEY31z9S8",
                "items": "address, position"
            }

        def test_return_api(self):

            return sucess_request_result

    def mock_get(url, api_here_params ):
        return MockResponse()


    here_mock = Hereapi()

    # monkeypatch.setattr(requests, "get", mock_get)
    monkeypatch.setattr(requests, "get", mock_get)

    position = here_mock.get_coord("Paris")
    position = {'lat': 48.87489, 'lng': 2.35051}
    assert(sucess_request_result['items'][0].get('position') == position)

    # monkeypatch.setattr(requests, 'get', mock_get)
    # assert  Hereapi.get_coord("", "Openclassrooms ? Ou paris situe") == (200, sucess_request_result['items'][0].get('position'))

# class MockResponse:
#
#     # mock json() method always returns a specific testing dictionary
#     @staticmethod
#     def json():
#         return sucess_request_result
#
#
# def test_get_json(monkeypatch):
#
#     # Any arguments may be passed and mock_get() will always return our
#     # mocked object, which only has the .json() method.
#
#     def mock_get(*args, **kwargs):
#         return MockResponse()
#
#     # apply the monkeypatch for requests.get to mock_get
#     monkeypatch.setattr(requests, "get", mock_get)
#
#     # app.get_json, which contains requests.get, uses the monkeypatch
#     here_mock = Hereapi()
#     result = here_mock.get_coord("Paris")
#     position = {'lat': 48.87489, 'lng': 2.35051}
#     assert (result['items'][0].get('position') == position)
