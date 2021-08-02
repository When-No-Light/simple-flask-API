from flask_sqlalchemy import SQLAlchemy
from server_part.database import db  
from server_part.app import app
from server_part.routs import *      # !!!!!!!!! переместить в другой файл
#db = SQLAlchemy(app)

#db.app = app

#db.create_all()
if __name__ == '__main__':
   #create table
#   db.create_all()
#   db.init_app(app)
   db.create_all()   #   !!!!!!!!!!!!!!! перенести куда то  makefile.py
   app.run()
   