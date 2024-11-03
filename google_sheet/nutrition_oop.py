from requests import request

class Nutrition():

    def __init__(self, nlp_endpoint, header, payload) -> None:
        
        self.nlp_endpoint = nlp_endpoint
        self.header = header
        self.payload = payload
        
        
    def nlp_exercise(self):

        response = request(method="POST",url = self.nlp_endpoint, headers = self.header, json = self.payload)
        return response.json()