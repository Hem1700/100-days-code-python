import requests
from datetime import datetime

today = datetime().now().strftime('%Y%m%d')


USERNAME = 'hemparekh'
TOKEN = 'thisissecret'
GRAPHID = 'graph1'
DATE =  today

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url= pixela_endpoint , json= user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_params = {
    'id': GRAPHID,
    'name': 'Cycling',
    'unit': 'km',
    'type': 'float',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)



pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}'



pixel_params = {
    'date': DATE,
    'quantity': input('How many kilometers did you cycle today?'),
}

response = requests.post(url= pixel_endpoint , json= pixel_params, headers= headers)
print(response.text)



# pixel_update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{DATE}'

# pixel_update_data = {
#     'quantity': '4',
# }

# # response = requests.put(url = pixel_update_endpoint , json= pixel_update_data, headers=headers)
# # print(response.text)


# delete = requests.delete(url= pixel_update_endpoint , headers=headers)
# print(delete.text)
