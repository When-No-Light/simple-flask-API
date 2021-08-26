from flask_security import SQLAlchemyUserDatastore, Security, UserMixin, RoleMixin, login_required
#from sqlalchemy.orm import relation, relationship

from datetime import datetime
from .db import db 
from passlib.apps import custom_app_context as pwd_context

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

from server_part.app import app 

# many to many relationships between roles and users

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

post_votes = db.Table('post_votes',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('post_id', db.Integer(), db.ForeignKey('post.id')))

comment_votes = db.Table('comment_votes',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('comment_id', db.Integer(), db.ForeignKey('comment.id')))
# basic users information 

class User(db.Model, UserMixin):  
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45), unique=True)
    username = db.Column(db.String(15))
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean(), default=False)
    is_banned = db.Column(db.Boolean(), default=False)
    adding_at = db.Column(db.Date(), default=datetime.utcnow().date())
    confirmed_on = db.Column(db.DateTime(), nullable=True)
    last_activity = db.Column(db.DateTime(), default = datetime.utcnow)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    comment_votes = db.relationship('Comment', secondary=comment_votes,
                            backref=db.backref('users', lazy='dynamic'))
    post_votes = db.relationship('Post', secondary=post_votes,
                            backref=db.backref('users', lazy='dynamic'))                        
                            
    post = db.relationship('Post')

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        

    def __repr__(self):
        return "<User(id='%s', email='%s', username='%s', password_hash='%s', active='%s', \
                    confirmed_at='%s', last_activity='%s', roles='%s')>" % (self.id,  \
                    self.email, self.username, self.password_hash, self.confirmed, \
                    self.confirmed_on, self.last_activity, self.roles)

    def generate_auth_token(self, expiration = 600):
        s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps({ 'id': self.id })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user
                    

# user roles in application

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(35), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name, description):
        self.name = name
        self.description = description

     


# many to many relationships between tags and posts

post_tags = db.Table('post_tags',
        db.Column('tag_id', db.Integer(), db.ForeignKey('tag.id')),
        db.Column('post_id', db.Integer(), db.ForeignKey('post.id')))

# user posts on a forum 


class Post(db.Model):  
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45), unique=False)
    post_text = db.Column(db.Text)
    confirmed_at = db.Column(db.DateTime(), default = datetime.now())
    outdated = db.Column(db.Boolean(), default=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    tag = db.relationship('Tag', secondary=post_tags,
                            backref=db.backref('post', lazy='dynamic'))

    def __init__(self, title, post_text, user_id):
        self.title = title
        self.post_text = post_text
        self.user_id = user_id
    def __repr__(self):
        return "<Post(id='%s', title='%s', post_text='%s', confirmed_at='%s')>" % (self.id,  \
                    self.title, self.post_text, self.confirmed_at)

# post tag

class Tag(db.Model):
    __tablename__ = 'tag'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(35), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Tag(id='%s', name='%s')>" % (self.id, self.name)
    




# users comments to some posts or other comments

class Comment(db.Model):  
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.Text)
    confirmed_at = db.Column(db.DateTime(), default = datetime.now())
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=True)
    # comment = relationship("Comment", backref="comment")


    

    def __init__(self, comment_text, post_id, user_id):
        self.comment_text = comment_text
        self.post_id = post_id
        self.user_id = user_id

    def __repr__(self):
        return "<Post(id='%s', title='%s', post_text='%s', voutes='%s', confirmed_at='%s', \
                    confirmed_at='%s', last_activity='%s', roles='%s')>" % (self.id,  \
                    self.title, self.post_text, self.voutes, self.confirmed_at)


