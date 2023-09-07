from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, SelectField, SubmitField, DateField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Optional, EqualTo

class Registration(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    Firstname = StringField('First name', validators=[DataRequired(), Length(min=2, max=30)])
    lastname = StringField('Last name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Join')


class Login(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class Checkout(FlaskForm):
    
    firstname = StringField('First name', validators=[DataRequired(), Length(min=2, max=30)])
    lastname = StringField('Last name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email (Optional)', validators=[Optional(), Email()])
    phonenumber = IntegerField('Phone number (Optional)', validators=[Optional()])
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=100)])
    country = SelectField('Country', choices=[('UK', 'United Kingdom')], validators=[DataRequired()])
    county = SelectField('County', choices=[('Avon', 'Avon'), ('Bedfordshire', 'Bedfordshire')], validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired(), Length(min=5, max=8)])
    submit = SubmitField('Continue to payment')


class Payment(FlaskForm):
    cardname = StringField('Name on card', validators=[DataRequired(), Length(min=2, max=30)])
    cardnum = IntegerField('Card number',validators=[DataRequired(), Length(min=16, max=16)]) 
    expire = DateField('Expiration date', format='%m-%Y', validators=[DataRequired()])
    cvc = IntegerField('CVC', validators= [DataRequired(), Length(min=3, max=3)])
    
#Create a search form

class Search(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Search")
    
class CreatePosts(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField('Post')
    
class Booking(FlaskForm):
    movie_id = SelectField('Movie Title', coerce=int, validators=[DataRequired()])
    screening_time = SelectField('Screening Time', coerce=int, validators=[DataRequired()])
    num_seats = IntegerField('Number of Seats', validators=[DataRequired()])
    booker_name = StringField('Name of Booker', validators=[DataRequired()])
    ticket_type = SelectField('Ticket Type', choices=[('Adult', 'Adult'), ('Child', 'Child')], validators=[DataRequired()])
    concession = BooleanField('Concession')
    submit = SubmitField('Book Tickets')