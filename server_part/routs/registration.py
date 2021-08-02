from flask_security import SQLAlchemyUserDatastore, Security, UserMixin, RoleMixin, login_required
from server_part.app import app
from server_part.database.tables import User, Role, roles_users
from flask import request, redirect, url_for, render_template
from server_part.database import db 

@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'], request.form['password'])
    db.session.add(user)
    db.session.commit()
    return {'username': 'Nightfoxer6', 'email': 'nightfoxer@ukr.net6', 'password': '19970601Dd'} # TODO заменить на что то 

'''@app.route('/add_product', methods=['POST'])
def add_product():
    product = In_demand(request.form['product_name'], request.form['found'], request.form['manufacturer'], request.form['picture_id'])
    db.session.add(product)
    db.session.commit()
    return {'username': 'Nightfoxer6', 'email': 'nightfoxer@ukr.net6', 'password': '19970601Dd'} # TODO заменить на что то '''


'''
@app.route('/add_product', methods=['POST'])
def add_product():
    product = In_demand(request.form['product_name'], request.form['manufacturer'], bool(request.form['found']), request.form['picture_id'])
    db.session.add(product)
    db.session.commit()
    return {'username': 'Nightfoxer6', 'email': 'nightfoxer@ukr.net6', 'password': '19970601Dd'} # TODO заменить на что то
'''

# post('http://localhost:5000/add_product', data={'product_name': 'chipsy', 'manufacturer': 'Lays', 'picture_id': 23, 'found': True}).json()

# post('http://localhost:5000/add_product', data={'product_name': 'chipsy', 'found': True, 'manufacturer': 'Lays',   'picture_id': 68969070090}).json()

@app.route('/add_role', methods=['POST'])
def add_role():
    role = Role(request.form['name'], request.form['description'])
    db.session.add(role)
    db.session.commit()
    return {'name': 'Nightfoxer6'} # TODO заменить на что то

# post('http://localhost:5000/add_role', data={'name': 'admin', 'description': 'Has all possible access rights'}).json()

@app.route('/add_role_for_user', methods=['POST'])
def add_role_for_user():
    User_and_role_id = [request.form['user_id'], request.form['role_id']]
    user = db.session.query(User).filter_by(id=User_and_role_id[0]).first()
    role = db.session.query(Role).filter_by(id=User_and_role_id[1]).first()
    user.roles.append(role)
    db.session.commit()
    return {'name': 'Nightfoxer6'} # TODO заменить на что то
    
# post('http://localhost:5000/add_role_for_user', data={'user_id': 2, 'role_id': 1}).json()

# post('http://localhost:5000/post_user', data={'username': 'Nightfoxer6', 'email': 'nightfoxer@ukr.net6', 'password': '19970601Dd'}).json()

'''impact alcohol angry plastic industry height suit swift grant crew coast ranch'''

