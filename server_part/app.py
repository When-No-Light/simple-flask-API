from flask import Flask



app = Flask(__name__, template_folder='templates')
# app.config.from_pyfile('config.py', silent=True)
app.config.from_object('config.Config')
app.debug = True


