import requests
from papybot.server.here import Hereapi
from papybot.tests import test_constants

class MockResponse:
    def __init__(self):
        self.sucess_request_result = test_constants.here_test_result
        self.status_code = 200

    def json(self):
        return self.sucess_request_result


def test_get_json(monkeypatch):

    def mock_get(*args, **kwargs):

        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    here_mock = Hereapi()
    position = here_mock.get_coord("situe Openclassrooms Ou paris")
    position_mock_result = ({'lat': 48.87489, 'lng': 2.35051},
                            "Openclassrooms, "
                            "7 Cité Paradis, 75010 Paris, France")
    assert position == position_mock_result
