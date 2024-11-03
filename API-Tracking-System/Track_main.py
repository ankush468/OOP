import requests
from datetime import datetime
from track_API_oop import ISS


MY_LAT = 20.593683 # Your latitude
MY_LONG = 78.962883 # Your longitude

ISS_API = "http://api.open-notify.org/iss-now.json"
Day_Track_API = "https://api.sunrise-sunset.org/json"

while True:
    Track_ISS_Data = ISS(ISS_API,MY_LAT,MY_LONG)
    ISS_position = Track_ISS_Data.is_iss_overhead()
    print(ISS_position)