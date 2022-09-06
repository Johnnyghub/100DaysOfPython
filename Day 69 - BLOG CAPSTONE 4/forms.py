from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    email = StringField("Email", render_kw={'style': 'width: 50ch'}, validators=[DataRequired(), Email()])
    username = StringField("Username", render_kw={'style': 'width: 30ch'}, validators=[DataRequired()])
    password = PasswordField("Password", render_kw={'style': 'width: 30ch'}, validators=[DataRequired()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email", render_kw={'style': 'width: 50ch'}, validators=[DataRequired(), Email()])
    password = PasswordField("Password", render_kw={'style': 'width: 30ch'}, validators=[DataRequired()])
    submit = SubmitField("Log In")


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Post Comment")
