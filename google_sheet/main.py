from requests import request
import os
from datetime import datetime, timedelta, date
from nutrition_oop import Nutrition
from pprint import pprint

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
pprint(nlp_response)

 # print day month year
DATE = datetime.now().strftime("%d/%m/%Y")

# print time in hour min sec format
TIME = datetime.now().strftime("%X") 

############## GET/UPDATE sheet with the data ##################################

SHEET_URL = 'https://api.sheety.co/c10bc28ab99077d2754b7745ddabadcd/ankush2Workouts/workoutsi'

sheet_headers = {
    'Authorization': 'Bearer'+' '+NUTRITIONIX_API_KEY
}

print(sheet_headers)

get_sheet_data = nlp_query.Get_sheet_data(SHEET_URL,sheet_headers )
print(get_sheet_data)

payload={
    'workout':{
        'date': DATE,
        'time' : TIME,
        'exercise':nlp_response['exercises'][0]['name'],
        'duration': nlp_response['exercises'][0]['duration_min'],
        'calories': nlp_response['exercises'][0]['nf_calories'],
    }
}

update_sheet_data = nlp_query.Update_sheet_data(SHEET_URL,sheet_headers,payload)
print(update_sheet_data)
