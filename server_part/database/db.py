from flask_sqlalchemy import SQLAlchemy
from server_part.app import app




db = SQLAlchemy(app)

db.create_all()