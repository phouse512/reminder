from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, EqualTo

class LoginForm(Form):
	username = TextField('username', validators = [Required()])
	pin = PasswordField('pin', validators = [Required()])

class SignupForm(Form):
	username = TextField('username', validators = [Required()])
	phone = TextField('phone', validators = [Required()])
	pin = PasswordField('pin', validators = [
		Required(),
		EqualTo('confirm', message="Pins must match")
	])
	confirm = PasswordField('confirm')
