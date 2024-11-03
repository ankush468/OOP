import requests
from datetime import datetime
from track_API_oop import IS_iss_overhead


MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


while True:
    if IS_iss_overhead