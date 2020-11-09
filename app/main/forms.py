from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class HelloWorldForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    message = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()
