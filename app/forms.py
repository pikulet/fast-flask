from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    text = StringField('Enter text here...', validators=[DataRequired()])
    submit = SubmitField('Confirm')
