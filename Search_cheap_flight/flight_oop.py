from requests import request
class Flight():

    def __init__(self, IANA_ENDPOINT:str, CITY:str, TOKEN:str) -> None:

        self.IANA_ENDPOINT = IANA_ENDPOINT
        self.CITY = CITY
        self.TOKEN = TOKEN
        self.flight_token_headers = {
            'Authorization': 'Bearer'+' '+self.TOKEN
        }

    def Get_IATA_code(self):

        IANA_pram = {
        'keyword':self.CITY,
        "max": "2",
        "include": "AIRPORTS"
        }

        response = request(method="GET",url=self.IANA_ENDPOINT, headers=self.flight_token_headers, params=IANA_pram)
        return response.json()['data'][0]['iataCode']
    
    def Flight_from_lon(self, Search_Flight_endpoint, iana_code, non_stop):

        pram = {
        'originLocationCode': 'LON',
        'destinationLocationCode': iana_code,
        'departureDate': '2024-11-07',
        'adults': 1,
        'nonStop': non_stop
                   }

        response = request(method="GET",url=Search_Flight_endpoint, params=pram, headers=self.flight_token_headers)
        print(response.json())

        flight_price_data = response.json()['data']

        cheap_flight = 10000

        for price in flight_price_data:
            price_int = float(price['price']['total'])
            if price_int< cheap_flight:
                cheap_flight = price_int

        if cheap_flight == 10000:

            return False
        
        return cheap_flight

