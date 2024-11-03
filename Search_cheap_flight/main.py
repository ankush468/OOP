from requests import request
import os
from datetime import datetime, timedelta, date
from pprint import pprint

NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')
NUTRITIONIX_API_ID = os.getenv('NUTRITIONIX_API_ID')
BASE_URL = 'https://trackapi.nutritionix.com'
