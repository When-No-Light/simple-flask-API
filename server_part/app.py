from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
# admin_password = '20010101'   # you need to insert password 
# env.read_envfile()

app = Flask(__name__, template_folder='templates')
# app.config.from_pyfile('config.py', silent=True)
app.config.from_object('config.Config')
login_manager = LoginManager()
login_manager.init_app(app)
app.debug = True

# requests.get('http://localhost:5000/api/resource', headers={'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsImlhdCI6MTYyOTI5MTY4NiwiZXhwIjoxNjI5MjkyMjg2fQ.eyJpZCI6OH0.CxDqZhoA3dM8ZZfB0_saPjoVvBPkC_S7PhTAWF7TXVudMMYHUtyWrHl8wC337OfHRd_SweRJaULGLzbbmZbw9g'})




# SECRET_KEY = env('SECRET_KEY', cast=str)
# SECURITY_REGISTERABLE = env('SECURITY_REGISTERABLE', cast=int)
# SECURITY_REGISTERABLE = env.bool('SECURITY_REGISTERABLE')
# POSTGRES_USER = env('POSTGRES_USER', cast=str, default='localhost')
# POSTGRES_PASSWORD = env('POSTGRES_PASSWORD', cast=str)
# POSTGRES_HOST = env('POSTGRES_HOST', cast=str, default='localhost')
# POSTGRES_PORT = env('POSTGRES_PORT', cast=str, default='5432')
# POSTGRES_DB = env('POSTGRES_DB', cast=str)
# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:20010101@localhost/grocery_app'
# app.config['SECRET_KEY'] = 'super-secret'
# app.config['SECRET_KEY'] = SECRET_KEY
# app.config['SECURITY_REGISTERABLE'] = True
# app.config['SECURITY_REGISTERABLE'] = SECURITY_REGISTERABLE
# app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
# print("postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")

