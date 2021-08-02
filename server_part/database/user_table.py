from datetime import date, datetime
from flask_security.core import UserMixin

from server_part.app  import db 
from data_base import roles_users


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