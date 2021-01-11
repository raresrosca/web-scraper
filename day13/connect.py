import requests
import pprint

api_key = "42db1904170b7de3fd71ca32e6cf590c"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MmRiMTkwNDE3MGI3ZGUzZmQ3MWNhMzJlNmNmNTkwYyIsInN1YiI6IjVmZmMwYjIwYTNiNWU2MDA0MDM3ZmRmYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ovmHTKNBPfNf7nYBCvdYHExBCvkHahCgQU29scjZ5sI"

#HTTP request methods:
"""
GET -> get data
POST -> add/update data
PATCH 
PUT
DELETE
"""

# What's our endpoint? (What's the url? Where do we want to request the data from?)
# REST API have an endpoint that you call in order to do something.

# What is the HTTP method that we need?

"""
Endpoint
GET
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=42db1904170b7de3fd71ca32e6cf590c
"""

#Using v3

movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
print(endpoint)
# r = requests.get(endpoint) #, data = {"api_key": api_key})
# print(r.status_code)
# print(r.text)

#Using v4

# movie_id = 501
# api_version = 3
# api_base_url = f"https://api.themoviedb.org/{api_version}"
# endpoint_path = f"/movie/{movie_id}"
# endpoint = f"{api_base_url}{endpoint_path}"
# headers = {'Authorization': f'Bearer {api_key_v4}',
#             'Content-Type': 'application/json;charset=utf-8'}
# r = requests.get(endpoint, headers = headers) 
# print(r.status_code)
# print(r.text)

movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query=Endgame"
print(endpoint)
r = requests.get(endpoint) #, data = {"api_key": api_key})
print(r.status_code)
pprint.pprint(r.json())