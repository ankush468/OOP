import requests
from datetime import datetime
from track_API_oop import ISS


MY_LAT = 20.593683 # Your latitude
MY_LONG = 78.962883 # Your longitude

ISS_API = "http://api.open-notify.org/iss-now.json"
Day_Track_API = "https://api.sunrise-sunset.org/json"
PARAMETERS = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
}


Track_ISS_Data = ISS(ISS_API,MY_LAT,MY_LONG)
ISS_position = Track_ISS_Data.is_iss_overhead()
print(ISS_position)

Check_if_night = Track_ISS_Data.is_night(Day_Track_API,PARAMETERS)

sunrise = Check_if_night[0]
sunset = Check_if_night[1]

time_now = datetime.now().hour

if time_now >= sunset or time_now <= sunrise:
    print("Yes")



