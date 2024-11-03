from requests import request
import os
from datetime import datetime, timedelta, date
from pprint import pprint

AMADEUS_API_KEY = os.getenv('AMADEUS_API_KEY')
AMADEUS_API_SECRET = os.getenv('AMADEUS_API_SECRET')
BASE_URL = 'https://trackapi.nutritionix.com'

print(AMADEUS_API_KEY,AMADEUS_API_SECRET)
