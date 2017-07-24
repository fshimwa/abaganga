# project/user/forms.py


from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ProfileForm(Form):
    bio = StringField('bio', validators=[DataRequired(), Length(min=6, max=25)])
    profilePic = StringField('profilePic', validators=[DataRequired(), Length(min=6, max=25)])
    phone = StringField('phone', validators=[DataRequired(), Length(min=2, max=25)])
