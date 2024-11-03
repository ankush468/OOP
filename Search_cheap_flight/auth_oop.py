from requests import request
class Auth():

    def __init__(self , token_endpoint:str, headers:dict, payload:dict) -> str:

        self.token_endpoint = token_endpoint
        self.headers = headers
        self.payload = payload

    def Get_token(self):

        response = request(method="POST", url=self.token_endpoint, headers=self.headers, data=self.payload)
        # return response.json()
        return response.json()['access_token']

class Sheet():

    def __init__(self, SHEET_URL:str, sheet_headers:dict) -> dict:

            self.SHEET_URL = SHEET_URL
            self.sheet_headers = sheet_headers

    def Get_sheet_data(self):

        response = request(method="GET", headers=self.sheet_headers, url=self.SHEET_URL)
        return response.json()