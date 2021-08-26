import requests

BASE_URL = 'http://localhost:5000/api/resource'
token = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYyOTI5MzgwMCwiZXhwIjoxNjI5Mjk0NDAwfQ.eyJpZCI6OH0.LxNZfg3rZrmeiR6d2dpnRXJgkQEPxt4Q2GZfSnsxgqQ5XeGSLQTc3oT9XyQzDZEbhE7rulEF4dMyXEtS_AaL4w"

headers = {'Authorization': "Bearer {}".format(token)}
auth_response = requests.get(BASE_URL, headers=headers)

print(auth_response.json())