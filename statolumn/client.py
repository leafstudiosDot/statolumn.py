import requests

class Client:
    access_token = ""

    def __init__(self, clientid, secret):
        self.clientid = clientid
        self.secret = secret
        pass

    def setAccessToken(self, token):
        self.access_token = token
        pass

    def getAccessToken(self):
        return self.access_token

    def getUserDetails(self):
        pass

    def getStatusLists(self, limit):
        pass