# project/models.py


import datetime

from sqlalchemy.orm import relationship

from project import db, bcrypt
from project.user.models import User


class Profile(db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(255), nullable=False)
    profilePic = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    validity = db.Column(db.Boolean, nullable=True, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = relationship(User, uselist=False, back_populates="profile")

    def __init__(self, user, bio, profile_pic, phone, validity):
        self.user = user
        self.bio = bio
        self.profilePic = profile_pic
        self.phone = phone
        self.validity = validity

    def __repr__(self):
        return '<firstName {}'.format(self.user.firstName)
