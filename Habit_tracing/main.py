from requests import request
from habit_track_oop import Habit_tracking
import os

HABIT_USER_NAME = os.getenv('HABIT_UNAME')
HABIT_TRACK_TOKEN = os.getenv('NEWS_API_KEY')
BASE_URL = 'https://pixe.la'

print(HABIT_USER_NAME)




# create user account

user_creation_endpoint = '/v1/users'

user_creation_url = BASE_URL+user_creation_endpoint

user_creation_payload = {
    'token': HABIT_TRACK_TOKEN,
    'username' : HABIT_USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor':'yes',
}

create_user = Habit_tracking(user_creation_url,user_creation_payload)
user = create_user.Create_user()
print(user)

# create a graph defination

graph_creation_endpoint = '/v1/users/@'+HABIT_USER_NAME+'graphs'

graph_creation_url = BASE_URL+graph_creation_endpoint

graph_creation_header = {
    'X-USER-TOKEN' : HABIT_TRACK_TOKEN
}

graph_creation_payload = {
    'id':'10',
    'name': 'ankush_graph',
    'unit': 'commit',
    'type':'int',
    'color':'ajisai'
}

Create_graph = create_user.Create_graph(graph_creation_url, graph_creation_header,graph_creation_payload)
print(Create_graph)






