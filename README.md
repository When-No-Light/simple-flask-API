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
    $ python -m venv nvenv
    for linux
    $ env/bin/activate
    for windows 
    $ nvenv/Scripts/activate
```

* Install dependencies from requirements.txt file

```shell
    $ pip install -r requirements.txt
```


*   Start the development server

```shell
    $ python -m server_part
```

## Examples of simple requests to the server with python 

* At first we need make some imports 

```shell
    $ python
    $ import requests
    $ from requests.auth import HTTPBasicAuth
```

* Post user, get user info, create user token, login to server with token

```shell
    $ requests.post('http://localhost:5000/post_user', data={'username': 'Username', 'email': 'nisaght1fox1er@ukr.net6', 'password': 'user_password'}).json()
    $ requests.get('http://localhost:5000/api/resource', auth=HTTPBasicAuth('Username', 'user_password')).json()
    $ requests.get('http://localhost:5000/api/token', auth=HTTPBasicAuth('Username', 'user_password')).json()
    $ requests.get('http://localhost:5000/api/resource', auth=HTTPBasicAuth('eyJhbGciOiJIUzUxMiIsImlhdCI6MTYyOTI5MzgwMCwiZXhwIjoxNjI5Mjk0NDAwfQ.eyJpZCI6OH0.LxNZfg3rZrmeiR6d2dpnRXJgkQEPxt4Q2GZfSnsxgqQ5XeGSLQTc3oT9XyQzDZEbhE7rulEF4dMyXEtS_AaL4w', 'unused')).json()
```

* If you want to use https your requests will be lucks like

```shell
    $ requests.get('https://localhost:5000/api/resource', verify = False, auth=HTTPBasicAuth('123', '123')).json()
```

* Login to server with token and get user info using Curl

```shell
    $ curl -u eyJhbGciOiJIUzUxMiIsImlhdCI6MTYyOTI5MzgwMCwiZXhwIjoxNjI5Mjk0NDAwfQ.eyJpZCI6OH0.LxNZfg3rZrmeiR6d2dpnRXJgkQEPxt4Q2GZfSnsxgqQ5XeGSLQTc3oT9XyQzDZEbhE7rulEF4dMyXEtS_AaL4w:unused -i -X GET http://127.0.0.1:5000/api/resource
    $ curl -u Nisagfhtfoxer6:1997d0601Dd -i -X GET http://127.0.0.1:5000/api/resource
```

