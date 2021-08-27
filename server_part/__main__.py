from server_part.database import db  
from server_part.app import app


if __name__ == '__main__':
   #create table
   db.create_all()  
   app.run()
   # app.run(ssl_context='adhoc')
   
   