from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField


class DataTriggerForm(FlaskForm):
    submit = SubmitField('Refresh Data!')
