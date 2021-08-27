import datetime
from flask_security import login_required
from routs.mail import send_email
from utils.token_for_mail import confirm_token, generate_confirmation_token
from server_part.app import app
from server_part.database.tables import User, Role
from flask import request, redirect, url_for, render_template
from server_part.database import db 
from flask import abort, jsonify, g
from server_part.utils.misc import auth

from flask import flash


@app.route('/index')
def index():
    return jsonify({ 'data': 'Hello'})


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({ 'data': 'Hello, %s  !' % g.user})


# User.query.filter_by(id=8).first().roles[0].name 




# @auth.verify_password                https://127.0.0.1:5000/api/resource
# def verify_password(username, password):
#     user = User.query.filter_by(username = username).first()
#     if not user or not user.verify_password(password):
#         return False
#     g.user = user
#     return True

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username = username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

    


# @app.route('/post_user', methods=['POST'])
# def post_user():
#     user = User(request.form['username'], request.form['email'])
#     password = request.form['password']
#     db.session.add(user)
#     db.session.commit()
#     token = generate_confirmation_token(user.email)
#     confirm_url = url_for('user.confirm_email', token=token, _external=True)
#     html = render_template('server_part/templates/activate.html', confirm_url=confirm_url)
#     subject = "Please confirm your email"
#     send_email(user.email, subject, html)

#     flash('A confirmation email has been sent via email.', 'success')
#     # return redirect(url_for("main.home"))
#     return 'Ok'



@app.route('/api/users1', methods = ['POST'])
def new_user1():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    if username is None or password is None or email is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        # abort(400) # existing user
        return 'username already taken'
    if User.query.filter_by(email = email).first() is not None:
        # abort(400) # existing email in database
        return 'email already taken'
    user = User(username=username, email=email)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    token = generate_confirmation_token(user.email)
    confirm_url = url_for('confirm_email', token=token, _external=True)
    html = render_template('activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(user.email, subject, html)

    flash('A confirmation email has been sent via email.', 'success')
    # return redirect(url_for("main.home"))
    return 'Ok'
# requests.get('http://localhost:5000/api/resource', auth=HTTPBasicAuth('Nisagfhtfoxer6', '1997d0601Dd')).json()

# curl -u Nisagfhtfoxer6:1997d0601Dd -i -X GET http://127.0.0.1:5000/api/resource
#  requests.post('http://localhost:5000/api/users1', data={'username': 'Nisagfhtfoxer6', 'email': 'nisagh2t1fox1er@ukr.net6', 'password': '1997d0601Dd'}).json()
#  requests.post('http://localhost:5000/api/users1', data={'username': 'nightfoxer', 'email': 'aragornes228@gmail.com', 'password': '1997d0601Dd'}).json()






@app.route('/api/users', methods = ['POST'])
def new_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']


    if username is None or password is None or email is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        # abort(400) # existing user
        return 'username already taken'
    if User.query.filter_by(email = email).first() is not None:
        # abort(400) # existing email in database
        return 'email already taken'
    user = User(username=username, email=email)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201, {'Location': url_for('get_user', id = user.id, _external = True)}
# requests.get('http://localhost:5000/api/resource', auth=HTTPBasicAuth('Nisagfhtfoxer6', '1997d0601Dd')).json()

# curl -u Nisagfhtfoxer6:1997d0601Dd -i -X GET http://127.0.0.1:5000/api/resource
#  

@app.route('/confirm/<token>')
# @login_required            
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        user.confirmed_on = datetime.datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    return redirect(url_for('index'))






@app.route('/api/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})



@app.route('/api/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({ 'confirm_email': token.decode('ascii') })




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
























@app.route('/admin')
# @auth.login_required(role='common')
@auth.login_required(role=['admin', 'common'])
def admins_only():
    return "Hello {}, you are an admin!".format(auth.current_user())












    