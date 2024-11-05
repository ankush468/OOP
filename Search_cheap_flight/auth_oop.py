from requests import request
import os
 
class Auth():

    def __init__(self , BASE_URL:str, AMADEUS_API_KEY:dict, AMADEUS_API_SECRET:dict) -> str:

        self.BASE_URL = BASE_URL
        self.AMADEUS_API_KEY = AMADEUS_API_KEY
        self.AMADEUS_API_SECRET = AMADEUS_API_SECRET

    def Get_token(self):

        self.token_endpoint = f'{self.BASE_URL}/v1/security/oauth2/token'

        self.payload = {
            'grant_type':'client_credentials',
            'client_id':self.AMADEUS_API_KEY,
            'client_secret':self.AMADEUS_API_SECRET,
        }


        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = request(method="POST", url=self.token_endpoint, headers=self.headers, data=self.payload)
        return response.json()['access_token']

class Sheet():

    def __init__(self, SHEET_GET_URL:str, NUTRITIONIX_API_KEY:dict) -> dict:

            self.SHEET_GET_URL = SHEET_GET_URL
            self.NUTRITIONIX_API_KEY = NUTRITIONIX_API_KEY
            self.nutririonix_sheet_headers = {
                      'Authorization': 'Bearer'+' '+self.NUTRITIONIX_API_KEY
                       }

    def Get_sheet_data(self):

           
        response = request(method="GET", headers=self.nutririonix_sheet_headers, url= self.SHEET_GET_URL)
        return response.json()
    
    def Update_sheet_data(self, Sheet_put_endpoint,iana_code,):

        put_payload={
                   'price':{
                         "iataCode": iana_code
                          }
                    }

        response = request(method="PUT", headers=self.nutririonix_sheet_headers, url=Sheet_put_endpoint ,json=put_payload)
        return response.json()