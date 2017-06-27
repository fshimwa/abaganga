# project/models.py


import datetime

from sqlalchemy.orm import relationship

from project import db, bcrypt
from project.user.models import User


class Profile(db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String, unique=False, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    bio = db.Column(db.String, nullable=False)
    profilePic = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)
    workPlace = db.Column(db.String, nullable=False)
    levels = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    validity = db.Column(db.Boolean, nullable=True, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship(User, uselist=False, back_populates="profile")

    def __init__(self, user, firstName, lastName, bio, profilePic, occupation, workPlace, levels, country, validity):
        self.user = user
        self.firstName = firstName
        self.lastName = lastName
        self.bio = bio
        self.profilePic = profilePic
        self.occupation = occupation
        self.workPlace = workPlace
        self.levels = levels
        self.country = country
        self.validity = validity

    def __repr__(self):
        return '<firstName {}'.format(self.firstName)
