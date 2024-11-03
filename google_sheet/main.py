from requests import request
import os
from datetime import datetime, timedelta, date
from nutrition_oop import Nutrition

NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')
NUTRITIONIX_API_ID = os.getenv('NUTRITIONIX_API_ID')
BASE_URL = 'https://trackapi.nutritionix.com'

############### creating first API call ######################

nlp_endpoint = f"{BASE_URL}/v2/natural/exercise"
query = input("enter your query")


header = {
    'x-app-key' : NUTRITIONIX_API_KEY,
    'x-app-id' : NUTRITIONIX_API_ID
}

payload = {
      'query':query
}

nlp_query = Nutrition(nlp_endpoint, header, payload)
nlp_response = nlp_query.nlp_exercise()
print(nlp_response)


