from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    title = StringField('Ваше имя', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    submit = SubmitField('Опубликовать')