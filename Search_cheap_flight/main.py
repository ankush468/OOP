from requests import request
import os,json
from datetime import datetime, timedelta, date
from pprint import pprint
from auth_oop import Auth, Sheet
from flight_oop import Flight

AMADEUS_API_KEY = os.getenv('AMADEUS_API_KEY')
AMADEUS_API_SECRET = os.getenv('AMADEUS_API_SECRET')
NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')
BASE_URL = 'https://test.api.amadeus.com/'
SHEET_GET_URL = 'https://api.sheety.co/c10bc28ab99077d2754b7745ddabadcd/flightDeals/prices'
IANA_ENDPOINT = f'{BASE_URL}/v1/reference-data/locations/cities'

################################ get access token ################################ 

get_token = Auth(BASE_URL,AMADEUS_API_KEY,AMADEUS_API_SECRET)
TOKEN = get_token.Get_token()
print(TOKEN)

################################ GET Data from sheety ################################ 


get_sheet_data = Sheet(SHEET_GET_URL,NUTRITIONIX_API_KEY)
sheet_data = get_sheet_data.Get_sheet_data()
pprint(sheet_data)

# Get IATA code for each city

for city in sheet_data['prices']:
    CITY = city['city']

    get_iana_code = Flight(IANA_ENDPOINT, CITY,TOKEN)
    iana_code = get_iana_code.Get_IATA_code()
    pprint(iana_code)

# ############## GET/UPDATE sheet with the data ##################################

    Sheet_put_endpoint = 'https://api.sheety.co/c10bc28ab99077d2754b7745ddabadcd/flightDeals/prices/'+str(city['id'])

    update_sheet_data = get_sheet_data.Update_sheet_data(Sheet_put_endpoint, iana_code)
    print(update_sheet_data)


# ############################ get flight detail from london to all locations Direct ##################
    
    Search_Flight_endpoint = f'{BASE_URL}/v2/shopping/flight-offers'

    non_stop = 'true'

    cheap_flight = get_iana_code.Flight_from_lon(Search_Flight_endpoint, iana_code, non_stop)

    if cheap_flight:

        print(f'Getting cheap Flights for {CITY}\n{CITY}: ${cheap_flight}')

    else:

        non_stop = 'false'

        print(f'there is no direct flight for {CITY} checking indirect flight')

        cheap_flight = get_iana_code.Flight_from_lon(Search_Flight_endpoint, iana_code, non_stop)

        print(cheap_flight)

        print(f'Getting cheap Flights for {CITY}\n{CITY}: ${cheap_flight}')
    


