# project/user/forms.py
# -*- coding: utf-8 -*-
import pycountry
import pprint

from flask_wtf import Form
from wtforms import TextField, PasswordField, DateField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from project.user.models import User


def load_countries():
    t = pycountry.countries
    return [(c.alpha_2, c.name) for c in t]


def load_titles():
    t = {'Dr': 'Dr', 'Mr': 'Mr', 'Mrs': 'Mrs', 'Ms': 'Ms'}
    return [('Doctor', 'Mr')]


class LoginForm(Form):
    email = TextField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterForm(Form):
    email = TextField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
    firstName = TextField(
        'firstName',
        validators=[DataRequired(), Length(min=2, max=40)])
    lastName = TextField(
        'lastName',
        validators=[Length(min=0, max=40)])
    workPlace = TextField(
        'workPlace',
        validators=[Length(min=3, max=40)])
    gender = SelectField('gender', validators=[DataRequired("Please select gender")],
                         choices=[('female', 'Female'), ('male', 'Male')])
    dateOfBirth = DateField('dateOfBirth', validators=[DataRequired("Please select Date Of Birth")])
    category = TextField(
        'category',
        validators=[DataRequired(), Length(min=6, max=40)])
    title = SelectField('title', validators=[DataRequired("Please select a Title")],
                        choices=[('MD', 'Medical Doctor (MD)'), ('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'),
                                 ('Phd', 'Phd.')])
    country = SelectField('country', choices=load_countries())

    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True


class ChangePasswordForm(Form):
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )
