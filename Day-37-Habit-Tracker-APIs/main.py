import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "deepakjindal"
TOKEN = "f34rj39348r3d23d2343r34x3d2xfeqsq3o"

user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# 1. Create a New User
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# 2. Create a New Graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

GRAPH_ID = "graph1"
GRAPH_NAME = "Daily Learning"

graph_config = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "hours",
    "type": "float",
    "color": "shibafu"
}

# response = requests.post(url= graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# 3. Post values to graph
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# date = datetime(year=2026, month=6, day=1)
date = datetime.now()

pixel_config = {
    "date": date.strftime("%Y%m%d"),
    "quantity": "2.5"
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# 4. Update a pixel value
update_date = datetime(year=2026,month=6, day=2)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{update_date.strftime('%Y%m%d')}"

update_pixel_config = {
    "quantity": "4"
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

# 5. Delete a pixel

delete_date = datetime(year=2026,month=6, day=1)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

