from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

.
class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "country" in dic:
            url = "https://restcountries.com/v3.1/name/country"
            r = requests.get(url + dic["country"])
            data = r.json()
            for item in data:
                capital = item["capital"][0]
            message = f'The capital of {dic["country"]} is {capital}.'

        elif "capital" in dic:
            url = "https://restcountries.com/v3.1/capital/"
            r = requests.get(url + dic["capital"])
            data = r.json()
            for item in data:
                country = item["name"]["common"]
            message = f'{dic["capital"]} is the capital of {country}.'

        else:
            message = 'Please give me a Country'

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return
