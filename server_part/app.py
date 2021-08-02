from flask import Flask

admin_password = 'password to database'   # you need to insert password 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{admin_password}@localhost/grocery_app'
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True

app.debug = True

if __name__ == "__main__":
    app.run()