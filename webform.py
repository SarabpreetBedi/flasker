from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField,ValidationError
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea




class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit =   SubmitField("Submit")
    
    
    
# Create a Posts Form

class PostForm(FlaskForm):
      title =  StringField("Title", validators=[DataRequired()])
      content =  StringField("Content" , validators=[DataRequired()], widget=TextArea())
      author = StringField("Author")
      slug = StringField("Slug" , validators=[DataRequired()])
      submit = SubmitField("Submit")
      
      
      
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("UserName", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    favorite_color  = StringField("Favorite Color")
    password_hash = PasswordField('Password', validators=[DataRequired(),EqualTo('password_hash2', message='Passwords Must Match!')])
    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField("Submit")   
    
    
class NameForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")    
    
class PasswordForm(FlaskForm):
    email = StringField("What's Your Email", validators=[DataRequired()])
    password_hash = PasswordField("What's Your Password", validators=[DataRequired()])
    submit = SubmitField("Submit")      
