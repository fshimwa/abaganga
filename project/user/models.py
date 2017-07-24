# project/models.py


import datetime

from flask_login import AnonymousUserMixin

from project import db, bcrypt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    firstName = db.Column(db.String(255), unique=False, nullable=False)
    lastName = db.Column(db.String(255), unique=False, nullable=True)
    workPlace = db.Column(db.String(255), unique=False, nullable=True)
    gender = db.Column(db.String(255), unique=False, nullable=False)
    dateOfBirth = db.Column(db.String(255), unique=False, nullable=False)
    category = db.Column(db.String(255), unique=False, nullable=False)
    title = db.Column(db.String(255), unique=False, nullable=True)
    country = db.Column(db.String(255), unique=False, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    confirmed = db.Column(db.Boolean, nullable=True, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    profile = db.relationship("Profile", back_populates="user", lazy='dynamic')
    last_login_at = db.Column(db.DateTime, nullable=True)
    current_login_at = db.Column(db.DateTime, nullable=True)
    last_login_ip = db.Column(db.String(255), nullable=True)
    current_login_ip = db.Column(db.String(255), nullable=True)
    login_count = db.Column(db.Integer, nullable=True)

    def __init__(self, email, firstName, lastName, workPlace, gender, dateOfBirth, category, title, country, password, confirmed, paid=False, admin=False, confirmed_on=None):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.workPlace = workPlace
        self.gender = gender
        self.dateOfBirth = dateOfBirth
        self.category = category
        self.title = title
        self.country = country
        self.password = bcrypt.generate_password_hash(password)
        self.registered_on = datetime.datetime.now()
        self.admin = admin
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<email {}'.format(self.email)
