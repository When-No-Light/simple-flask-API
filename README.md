# try_kivy_app


# to start project press `python -m server_part` to command line

# cp .env.example .env

For client test
# import libraries
`from requests.auth import HTTPBasicAuth`
`import requests`
# List of requests for server without https
`requests.get('http://localhost:5000/api/resource', auth=HTTPBasicAuth('Nisagfhtfoxer6', '1997d0601Dd')).json()`
`requests.get('http://localhost:5000/api/token', auth=HTTPBasicAuth('Nisagfhtfoxer6', '1997d0601Dd')).json()`
`requests.get('http://localhost:5000/api/resource', auth=HTTPBasicAuth('eyJhbGciOiJIUzUxMiIsImlhdCI6MTYyOTI5MzgwMCwiZXhwIjoxNjI5Mjk0NDAwfQ.eyJpZCI6OH0.LxNZfg3rZrmeiR6d2dpnRXJgkQEPxt4Q2GZfSnsxgqQ5XeGSLQTc3oT9XyQzDZEbhE7rulEF4dMyXEtS_AaL4w', 'unused')).json()`
`requests.post('http://localhost:5000/api/users', data={'username': 'Nisagfhtfoxer6', 'email': 'nisaght1foxer@ukr.net6', 'password': '1997d0601Dd'}).json()`
`requests.post('http://localhost:5000/post_user', data={'username': 'Nisagfhtfoxer6', 'email': 'nisaght1fox1er@ukr.net6', 'password': '1997d0601Dd'}).json()`
`curl -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTYyOTI5MzgwMCwiZXhwIjoxNjI5Mjk0NDAwfQ.eyJpZCI6OH0.LxNZfg3rZrmeiR6d2dpnRXJgkQEPxt4Q2GZfSnsxgqQ5XeGSLQTc3oT9XyQzDZEbhE7rulEF4dMyXEtS_AaL4w:unused -i -X GET http://127.0.0.1:5000/api/resource`
# 

# List of requests for server with https

`requests.get('https://localhost:5000/api/resource', verify = False, auth=HTTPBasicAuth('123', '123')).json()`


`curl -u Nisagfhtfoxer6:1997d0601Dd -i -X GET http://127.0.0.1:5000/api/resource`
`curl -u Nisagfhtfoxer6:1997d0601Dd -i -X GET http://127.0.0.1:5000/api/token`
`curl -u some_token:unused -i -X GET http://127.0.0.1:5000/api/resource`
