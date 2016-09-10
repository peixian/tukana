from flask_wtf import FlaskForm
from wtforms import tStringField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    
