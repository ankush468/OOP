from requests import request
import os
from datetime import datetime, timedelta, date
from pprint import pprint
from auth_oop import Auth, Sheet
from flight_oop import Flight

AMADEUS_API_KEY = os.getenv('AMADEUS_API_KEY')
AMADEUS_API_SECRET = os.getenv('AMADEUS_API_SECRET')
NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')
BASE_URL = 'https://test.api.amadeus.com/v1'

################################ get access token ################################ 

token_endpoint = f'{BASE_URL}/security/oauth2/token'

payload = {
    'grant_type':'client_credentials',
    'client_id':AMADEUS_API_KEY,
    'client_secret':AMADEUS_API_SECRET,
}


headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

get_token = Auth(token_endpoint,headers,payload)
TOKEN = get_token.Get_token()
print(TOKEN)

################################ GET Data from sheety ################################ 

SHEET_URL = 'https://api.sheety.co/c10bc28ab99077d2754b7745ddabadcd/flightDeals/prices'

sheet_headers = {
    'Authorization': 'Bearer'+' '+NUTRITIONIX_API_KEY
}

print(sheet_headers)

# get_sheet_data = Sheet(SHEET_URL,sheet_headers)
# sheet_data = get_sheet_data.Get_sheet_data()
# pprint(sheet_data)

sheet_data = {'prices': [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
            {'city': 'Frankfurt', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
            {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
            {'city': 'Hong Kong', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
            {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
            {'city': 'Kuala Lumpur',
             'iataCode': '',
             'id': 7,
             'lowestPrice': 414},
            {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
            {'city': 'San Francisco',
             'iataCode': '',
             'id': 9,
             'lowestPrice': 260},
            {'city': 'Dublin', 'iataCode': '', 'id': 10, 'lowestPrice': 378}]}

# Get IATA code for each city

for city in sheet_data['prices']:
    print(city['city'])

    pram = {
        'keyword':city['city']
    }

    headers = {
        'Authorization': 'Bearer'+' '+TOKEN
    }

    cities_endpoint = f'{BASE_URL}/reference-data/locations/cities'

    print(pram)

    get_iana_code = Flight(cities_endpoint, headers, pram)
    iana_code = get_iana_code.Get_IATA_code()
    pprint(iana_code)
    break

