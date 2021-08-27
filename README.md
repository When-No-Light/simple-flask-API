# simple-flask-API

This is a very simple and primitive API designed for a mobile application using PostgreSQL and allowing users to restrict its functionality depending on what access level they have.

## Installing / Getting started

* Clone the project from Github

```shell
    $ git clone https://github.com/When-No-Light/simple-flask-API.git
    $ cd simple-flask-API
```

* Create the .env file:

```shell
    $ cp .env.example .env
```

In the .env file, there are config related to the database and mail that must be added.

* Create the virtual environment file:

```shell
    $ virtualenv venv
    $ . venv/bin/activate
    for windows 
    $ . venv/Scripts/activate
```

* Install dependencies from requirements.txt file

```shell
    $ pip install -r requirements.txt
```


*   Start the development server

```shell
    $ python -m server_part
```















`cp .env.example .env`
to start project press `python -m server_part` to command line



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
curl -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTYyOTI5MzgwMCwiZXhwIjoxNjI5Mjk0NDAwfQ.eyJpZCI6OH0.LxNZfg3rZrmeiR6d2dpnRXJgkQEPxt4Q2GZfSnsxgqQ5XeGSLQTc3oT9XyQzDZEbhE7rulEF4dMyXEtS_AaL4w:unused -i -X GET http://127.0.0.1:5000/api/resource
# 

# List of requests for server with https

`requests.get('https://localhost:5000/api/resource', verify = False, auth=HTTPBasicAuth('123', '123')).json()`


`curl -u Nisagfhtfoxer6:1997d0601Dd -i -X GET http://127.0.0.1:5000/api/resource`
`curl -u Nisagfhtfoxer6:1997d0601Dd -i -X GET http://127.0.0.1:5000/api/token`
`curl -u some_token:unused -i -X GET http://127.0.0.1:5000/api/resource`
