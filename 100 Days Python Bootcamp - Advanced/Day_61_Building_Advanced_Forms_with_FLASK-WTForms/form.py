from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email

class MyForm(FlaskForm):
    def check_email(form, field):
        if '@' not in field.data:
            raise ValidationError("Please include '@' in email")
        
    def check_password(form, field):
        if len(field.data) < 8:
            raise ValidationError("Please enter at least 8 characters")

    email = StringField(label='E-mail', validators=[DataRequired(), Email(), check_email])
    password = PasswordField(label='Password', validators=[DataRequired(), check_password])
    submit = SubmitField(label="Log In")
