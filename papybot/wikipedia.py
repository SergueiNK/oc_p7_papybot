import requests
import json

url_request_wikipedia = 'https://fr.wikipedia.org/w/api.php'
# url_request_hereapi_auto = 'https://autosuggest.search.hereapi.com/v1/autosuggest'
    # hereapi_key = 'Bn9eoZ-0hBETw8Qs6dUJb3ZcbXl7hoa_AVSNi-9Sf5o'
products_params = {
            "format": "json",
            "action": "query",
            "prop": "extracts|info",
            "inprop": "url",
            "exchars": 400,
            "explaintext": True,
            "generator": "geosearch",
            "ggscoord": "48.85717|2.3414",

}
request_response = requests.get(url_request_wikipedia, products_params)
print(request_response.url)
print(request_response.text)
response = json.loads(request_response.text)
print(response)
