from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    IntegerField,
    SelectField,
    SubmitField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField,
    EmailField,
    TextAreaField,
    RadioField,
    DecimalField,
)
from wtforms.validators import DataRequired, Length, Optional, EqualTo


class Registration(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    Firstname = StringField(
        "First name", validators=[DataRequired(), Length(min=2, max=30)]
    )
    lastname = StringField(
        "Last name", validators=[DataRequired(), Length(min=2, max=30)]
    )
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Join")


class Login(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class Checkout(FlaskForm):
    firstname = StringField(
        "First name", validators=[DataRequired(), Length(min=2, max=30)]
    )
    lastname = StringField(
        "Last name", validators=[DataRequired(), Length(min=2, max=30)]
    )
    email = EmailField("Email (Optional)", validators=[Optional()])
    phonenumber = IntegerField("Phone number (Optional)", validators=[Optional()])
    address = StringField(
        "Address", validators=[DataRequired(), Length(min=2, max=100)]
    )
    country = SelectField(
        "Country", choices=[("UK", "United Kingdom")], validators=[DataRequired()]
    )
    county = SelectField(
        "County",
        choices=[("Avon", "Avon"), ("Bedfordshire", "Bedfordshire")],
        validators=[DataRequired()],
    )
    postcode = StringField(
        "Postcode", validators=[DataRequired(), Length(min=5, max=8)]
    )
    submit = SubmitField("Continue to payment")


class Payment(FlaskForm):
    cardname = StringField(
        "Name on card", validators=[DataRequired(), Length(min=2, max=30)]
    )
    cardnum = IntegerField(
        "Card number", validators=[DataRequired(), Length(min=16, max=16)]
    )
    expire = DateField("Expiration date", format="%m-%Y", validators=[DataRequired()])
    cvc = IntegerField("CVC", validators=[DataRequired(), Length(min=3, max=3)])


# Create a search form
class SearchForm(FlaskForm):
    search_query = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')


class BookingForm(FlaskForm):
    movie_id = SelectField("Movie Title", coerce=int, validators=[DataRequired()])
    screening_time = SelectField("Screening Time", coerce=str, validators=[DataRequired()])
    booker_name = StringField("Name of Booker", validators=[DataRequired()])
    adult_tickets = IntegerField("Number of Adult Tickets", validators=[DataRequired()], default=0)
    child_tickets = IntegerField("Number of Child Tickets", validators=[DataRequired()], default=0)
    concession = RadioField("Concession: ", choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    total_price = DecimalField("Total Price", places=2, render_kw={'readonly': True})
    submit = SubmitField("Book Tickets")


class CreatePosts(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Post")
