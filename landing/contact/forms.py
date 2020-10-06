from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, ValidationError
from sqlalchemy import not_
from .models import EmailSignup

class ViewContactForm(FlaskForm):
	password = PasswordField('Password', validators=[validators.DataRequired(message='Password required')])
	def validate_password(self, field):
		if field.data != 'Royal713!':
			raise ValidationError('No permission to view')

class ContactForm(FlaskForm):
	first_name = StringField('First Name', render_kw={"class": "form-control"}, validators=[validators.DataRequired(message='Your first name is required')])
	last_name = StringField('Last Name', render_kw={"class": "form-control"}, validators=[validators.DataRequired(message='Your last name is required')])
	email = StringField('Email', render_kw={"class": "form-control"}, validators=[validators.DataRequired(message='Your email is required'), validators.Email()])
	phone_number = StringField('Phone #', render_kw={"class": "form-control"}, validators=[validators.DataRequired(message='Your phone number is required')])