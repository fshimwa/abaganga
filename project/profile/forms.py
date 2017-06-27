# project/user/forms.py


from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ProfileForm(Form):
    firstName = StringField('firstName', validators=[DataRequired(), Length(min=6, max=25)])
    lastName = StringField('lastName', validators=[DataRequired(), Length(min=6, max=25)])
    bio = StringField('bio', validators=[DataRequired(), Length(min=6, max=25)])
    profilePic = StringField('profilePic', validators=[DataRequired(), Length(min=6, max=25)])
    occupation = StringField('occupation', validators=[DataRequired(), Length(min=6, max=25)])
    workPlace = StringField('workPlace', validators=[DataRequired(), Length(min=6, max=25)])
    levels = StringField('levels', validators=[DataRequired(), Length(min=6, max=25)])
    country = StringField('country', validators=[DataRequired(), Length(min=6, max=25)])

# class RegisterForm(Form):
#     email = StringField(
#         'email',
#         validators=[DataRequired(), Email(message=None), Length(min=6, max=40)])
#     password = PasswordField(
#         'password',
#         validators=[DataRequired(), Length(min=6, max=25)]
#     )
#     confirm = PasswordField(
#         'Repeat password',
#         validators=[
#             DataRequired(),
#             EqualTo('password', message='Passwords must match.')
#         ]
#     )
#
#     def validate(self):
#         initial_validation = super(RegisterForm, self).validate()
#         if not initial_validation:
#             return False
#         user = User.query.filter_by(email=self.email.data).first()
#         if user:
#             self.email.errors.append("Email already registered")
#             return False
#         return True
#
#
# class ChangePasswordForm(Form):
#     password = PasswordField(
#         'password',
#         validators=[DataRequired(), Length(min=6, max=25)]
#     )
#     confirm = PasswordField(
#         'Repeat password',
#         validators=[
#             DataRequired(),
#             EqualTo('password', message='Passwords must match.')
#         ]
#     )
