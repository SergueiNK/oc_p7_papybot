import requests
from papybot.server.wikipedia import Wikiapi
from papybot.tests import test_constants


class MockResponse:
    """Mock reposnse for requests"""
    def __init__(self):
        """Initialize the mock class"""
        self.sucess_request_result = test_constants.wiki_api_return
        self.status_code = 200

    def json(self):
        """Mocking json response from API"""
        return self.sucess_request_result


def test_wiki_article(monkeypatch):
    """Test here class with monkey patch """
    def mock_get(*args, **kwargs):
        """Mock get method if success"""
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    wiki_mock = Wikiapi()
    wiki = wiki_mock.wikipedia_get_article(['48.87489'], ['2.35051'])
    text_mock_result = "La rue d’Hauteville est une voie publique située " \
                       "dans le 10e arrondissement de Paris."
    assert wiki == text_mock_result
