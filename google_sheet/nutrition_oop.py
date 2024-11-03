from requests import request

class Nutrition():

    def __init__(self, nlp_endpoint, header, payload) -> None:
        
        self.nlp_endpoint = nlp_endpoint
        self.header = header
        self.payload = payload
        
        
    def nlp_exercise(self):

        response = request(method="POST",url = self.nlp_endpoint, headers = self.header, json = self.payload)
        return response.json()
    
    def Get_sheet_data(self, SHEET_URL, sheet_headers):

        response = request(method="GET", headers=sheet_headers, url=SHEET_URL)
        return response.json()
    
    def Update_sheet_data(self, SHEET_URL,sheet_headers,payload):

        response = request(method="POST", headers=sheet_headers, url=SHEET_URL ,json=payload)
        return response.json()