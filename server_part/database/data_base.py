from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template
from flask_security import SQLAlchemyUserDatastore, Security, UserMixin, RoleMixin, login_required
from sqlalchemy.orm import relation, relationship

from datetime import date, datetime

admin_password = 20010101

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{admin_password}@localhost/grocery_app'
app.config['SECRET_KEY'] = 'super-secret'
app.config['SECURITY_REGISTERABLE'] = True

app.debug = True
db = SQLAlchemy(app)


# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))




class User(db.Model, UserMixin):  
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45), unique=True)
    username = db.Column(db.String(15))
    password = db.Column(db.String(30))
    active = db.Column(db.Boolean(), default=False)
    is_banned = db.Column(db.Boolean(), default=False)
    confirmed_at = db.Column(db.DateTime(), default=date.today())
    last_activity = db.Column(db.DateTime(), default = datetime.now())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
                            
    post = db.relationship('Post')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return "<User(id='%s', email='%s', username='%s', password='%s', active='%s', \
                    confirmed_at='%s', last_activity='%s', roles='%s')>" % (self.id,  \
                    self.email, self.username, self.password, self.active, \
                    self.confirmed_at, self.last_activity, self.roles)


                    


# post('http://localhost:5000/post_user', data={'username': 'Nightfoxer6', 'email': 'nightfoxer@ukr.net6', 'password': '19970601Dd'}).json()


       # return '<username %r, email %r, password %r, active %r, confirmed_at %r, last_activity %r, confirmed_at %r>' % (self.username, self.email)
#return "(%s, %s, %s)" % (self.x, self.y, self.z)




class Role(db.Model, RoleMixin):
    __tablename__ = 'role'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(35), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Role(id='%s', name='%s', description='%s')>" % (self.id,  \
                    self.name, self.description)




post_tags = db.Table('post_tags',
        db.Column('tag_id', db.Integer(), db.ForeignKey('tag.id')),
        db.Column('post_id', db.Integer(), db.ForeignKey('post.id')))


class Post(db.Model):  
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45), unique=False)
    post_text = db.Column(db.Text)
    voutes = db.Column(db.String(30))
    confirmed_at = db.Column(db.DateTime(), default = datetime.now())
    outdated = db.Column(db.Boolean(), default=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    tag = db.relationship('Tag', secondary=post_tags,
                            backref=db.backref('post', lazy='dynamic'))

    def __init__(self, title, post_text):
        self.title = title
        self.post_text = post_text

    def __repr__(self):
        return "<Post(id='%s', title='%s', post_text='%s', voutes='%s', confirmed_at='%s', \
                    confirmed_at='%s', last_activity='%s', roles='%s')>" % (self.id,  \
                    self.title, self.post_text, self.voutes, self.confirmed_at)



class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(35), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Tag(id='%s', name='%s')>" % (self.id, self.name)
    






class Comment(db.Model):  
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.Text)
    voutes = db.Column(db.String(30))
    confirmed_at = db.Column(db.DateTime(), default = datetime.now())
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=True)
    # comment = relationship("Comment", backref="comment")


    

    def __init__(self, title, post_text):
        self.title = title
        self.post_text = post_text

    def __repr__(self):
        return "<Post(id='%s', title='%s', post_text='%s', voutes='%s', confirmed_at='%s', \
                    confirmed_at='%s', last_activity='%s', roles='%s')>" % (self.id,  \
                    self.title, self.post_text, self.voutes, self.confirmed_at)







# class In_demand(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     product_name = db.Column(db.String(35))
#     manufacturer = db.Column(db.String(35))
#     found = db.Column(db.Boolean())
#     date_added = db.Column(db.DateTime())
#     picture_id = db.Column(db.Integer)

#     def __init__(self, product_name, manufacturer, found=False, picture_id=1, date_added=datetime.now()):
#         self.product_name = product_name
#         self.manufacturer = manufacturer
#         self.found = found
#         self.date_added = date_added
#         self.picture_id = picture_id

#     def __repr__(self):
#         return "<In_demand(id='%s', product_name='%s', manufacturer='%s', found='%s',  \
#                     date_added='%s', picture_id='%s')>" % (self.id, self.product_name, \
#                     self.manufacturer, self.found, self.date_added, self.picture_id)

# post('http://localhost:5000/add_product', data={'product_name': 'chipsy', 'manufacturer': 'Lays', 'found': False, 'picture_id': 68969070090}).json()
# post('http://localhost:5000/add_product', data={'product_name': 'chipsy', 'manufacturer': 'Lays', 'found': True}).json()




# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.route('/')
def index():
    #return "User was added successfully"
    return {'username': 'Nightfoxer6', 'email': 'nightfoxer@ukr.net6', 'password': '19970601Dd'}
@app.route('/profile/<email>')
@login_required
def profile(email):
    user = User.query.filter_by(email=email).first()
    return render_template('profile.html', user=user)


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


# @app.route('/add_product', methods=['POST'])
# def add_product():
#     product = In_demand(request.form['product_name'], request.form['manufacturer'], bool(request.form['found']), request.form['picture_id'])
#     db.session.add(product)
#     db.session.commit()
#     return {'username': 'Nightfoxer6', 'email': 'nightfoxer@ukr.net6', 'password': '19970601Dd'} # TODO заменить на что то


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

db.create_all()




if __name__ == "__main__":
    app.run()

# post('http://localhost:5000/post_user', data={'username': 'Nightfoxer6', 'email': 'nightfoxer@ukr.net6', 'password': '19970601Dd'}).json()

'''impact alcohol angry plastic industry height suit swift grant crew coast ranch'''