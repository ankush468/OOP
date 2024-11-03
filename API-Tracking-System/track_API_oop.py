from requests import request

class ISS():

    def __init__(self,ISS_API:str  ,MY_LAT:float,  MY_LONG:float) -> None:

        self.ISS_API = ISS_API
        self.MY_LAT = MY_LAT
        self.MY_LONG = MY_LONG

    def is_iss_overhead(self):

        response = request(method="GET",url=self.ISS_API)
        response.raise_for_status()
        self.data = response.json()

        iss_latitude = float(self.data["iss_position"]["latitude"])
        iss_longitude = float(self.data["iss_position"]["latitude"])

        if self.MY_LAT-5 <= iss_latitude <= self.MY_LAT+5 and self.MY_LONG-5 <= iss_latitude <= self.MY_LONG+5:
            return True
        
        else:
            return False

    def is_night(self):
        pass