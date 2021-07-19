import requests
from papybot.server.wikipedia import Wikiapi
from papybot.tests import test_constants

class MockResponse:

    def __init__(self):
        self.sucess_request_result = test_constants.wiki_test_result
        self.status_code = 200

    def json(self):
        return self.sucess_request_result


def test_get_json(monkeypatch):

    def mock_get(*args, **kwargs):

        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    wiki_mock = Wikiapi()
    text = wiki_mock.wikipedia_get_article(['48.87489'], ['2.35051'])
    text_mock_result = "La rue d’Hauteville est une voie publique située dans le 10e arrondissement de Paris."
    assert text == text_mock_result
