from flask_security import SQLAlchemyUserDatastore, Security, UserMixin, RoleMixin, login_required
#from sqlalchemy.orm import relation, relationship

from datetime import datetime
from .db import db 





# many to many relationships between roles and users

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


# basic users information 

class User(db.Model, UserMixin):  
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45), unique=True)
    username = db.Column(db.String(15))
    password = db.Column(db.String(30))
    active = db.Column(db.Boolean(), default=False)
    is_banned = db.Column(db.Boolean(), default=False)
    confirmed_at = db.Column(db.Date(), default=datetime.utcnow().date())
    last_activity = db.Column(db.DateTime(), default = datetime.utcnow)
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


                    

# user roles in application

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


