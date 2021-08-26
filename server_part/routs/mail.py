from flask.helpers import flash
from flask_security.utils import login_user, url_for_security
from utils.token_for_mail import generate_confirmation_token
from server_part.app import app
from server_part.database.tables import User
from flask_mail import Mail, Message
from server_part.database import db 
from flask import render_template, redirect, url_for, request


mail = Mail(app)


def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)



