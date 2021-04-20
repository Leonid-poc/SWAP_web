from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    title = StringField('Название товара', validators=[DataRequired()])
    content = TextAreaField("Описание")
    # photo = StringField('Фото', validators=[DataRequired()])
    # connection = StringField('Связаться с нами', validators=[DataRequired()])
    # category = StringField('Категория', validators=[DataRequired()])
    submit = SubmitField('Добавить')