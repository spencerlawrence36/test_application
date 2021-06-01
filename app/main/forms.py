from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

class UserTextForm(FlaskForm):
	user_text = TextAreaField('User Text', validators=[DataRequired()])
	socket_id = TextAreaField()
	submit = SubmitField('Submit')
