from requests import request
class Flight():

    def __init__(self, cities_endpoint, headers, pram) -> None:

        self.cities_endpoint = cities_endpoint
        self.headers = headers
        self.pram = pram

    def Get_IATA_code(self):

        response = request(method="GET",url=self.cities_endpoint, headers=self.headers, params=self.pram)
        return response.json()

