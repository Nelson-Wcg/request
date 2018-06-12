# encoding: utf-8
import requests


class Request():
    def __init__(self):
        self.demoin = "localhost"
        self.port = "8087"
        self.request_url = "/"

    def do_request(self):
        url = "http://" + self.demoin + ":" + self.port + self.request_url
        ret = requests.get(url)
        return ret.text
