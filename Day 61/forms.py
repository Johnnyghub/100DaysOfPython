from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField(label='Email', render_kw={'style': 'width: 30ch'}, validators=[InputRequired(), Email()])
    password = PasswordField(label='Password', render_kw={'style': 'width: 20ch'}, validators=[InputRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")
