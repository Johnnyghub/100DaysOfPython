from requests import post, put, delete
from datetime import datetime as date

# commented out resquests means they have been completed, uncomment to rerun/change data

TOKEN = "fgwfgwrgfweggvreg"
USERNAME = "johnnym2"
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'

HEADERS = {
    "X-USER-TOKEN": TOKEN,
}

parameters = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# with post(url=PIXELA_ENDPOINT, json=parameters) as response:
#     print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

GRAPH_ID = "graph1"

graphs_params = {
    "id":GRAPH_ID,
    "name":"Coding Graph",
    "unit":"mins",
    "type":"int",
    "color":"ajisai",
}

# with post(url=graph_endpoint, json=graphs_params, headers=HEADERS) as response:
#     print(response.text)

pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_params = {
    "date": date.now().strftime("%Y%m%d"),  # formats date in YYYYmmDD
    "quantity":"120",
}

# with post(url=pixel_endpoint, json=pixel_params, headers=HEADERS) as response:
#     print(response.text)

update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date.now().strftime('%Y%m%d')}"

update_params = {"quantity":"150"}

# with put(url=update_endpoint, json=update_params, headers=HEADERS) as response:
#     print(response.text)

delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date.now().strftime('%Y%m%d')}"

# with delete(url=delete_endpoint, headers=HEADERS) as response:
#     print(response.text)
