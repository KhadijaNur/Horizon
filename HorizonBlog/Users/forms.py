from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from HorizonBlog.models import User


class LoginForm(FlaskForm):
    email= StringField('Email', validators=[DataRequired(), Email()])
    password= PasswordField('Password', validators=[DataRequired()])
    submit=SubmitField('Log in')

class RegistrationForm(FlaskForm):
    email= StringField('Email', validators=[DataRequired(), Email()])
    name= StringField('Name', validators=[DataRequired()])
    username= StringField('Username', validators=[DataRequired()])
    password= PasswordField('Password', validators=[DataRequired(), EqualTo('confirm_password', message='Password must match!')])
    confirm_password= PasswordField('Confirm Password', validators=[DataRequired()])
    submit= SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise   ValidationError('This email is already registered!')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('This username is taken!')
        

class UpdateUserForm(FlaskForm):
    email= StringField('Email', validators=[DataRequired(), Email()])
    name= StringField('Name', validators=[DataRequired()])
    username= StringField('Username', validators=[DataRequired()])
    picture= FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit= SubmitField('Update')