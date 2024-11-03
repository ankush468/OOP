from requests import request
from habit_track_oop import Habit_tracking
import os

HABIT_USER_NAME = os.getenv('HABIT_UNAME')
HABIT_TRACK_TOKEN = os.getenv('NEWS_API_KEY')
BASE_URL = 'https://pixe.la'

print(HABIT_USER_NAME)




# create user account return a dict

user_creation_endpoint = '/v1/users'

user_creation_url = f'{BASE_URL}{user_creation_endpoint}'

print(user_creation_url)

user_creation_payload = {
    'token': HABIT_TRACK_TOKEN,
    'username' : HABIT_USER_NAME,
    'agreeTermsOfService': 'yes',
    'notMinor':'yes',
}

create_user = Habit_tracking(user_creation_url,user_creation_payload)
# user = create_user.Create_user()
# print(user)

# create a graph defination

graph_creation_endpoint = '/v1/users/'+HABIT_USER_NAME+'/graphs'

graph_creation_url = f'{BASE_URL}{graph_creation_endpoint}'

# print(graph_creation_url)

header_for_all = {
    'X-USER-TOKEN' : HABIT_TRACK_TOKEN
}

graph_creation_payload = {
    'id':'graph1',
    'name': 'ankush_graph',
    'unit': 'km',
    'type':'float',
    'color':'ajisai'
}

Create_graph = create_user.Create_graph(graph_creation_url, header_for_all,graph_creation_payload)
print(Create_graph)


# get graph details

get_graph_endpoint = f'{BASE_URL}{graph_creation_endpoint}'

print(get_graph_endpoint)


# get_graph = create_user.Get_graph(get_graph_endpoint, header_for_all)
# print(get_graph)



# post a value on the graph

post_pixel_endpoint = f'{BASE_URL}{graph_creation_endpoint}/{graph_creation_payload['id']}'

create_pixel = create_user

print(post_pixel_endpoint)