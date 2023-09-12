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
from wtforms.validators import DataRequired, Length, Optional, EqualTo, NumberRange, ValidationError


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


class Paymentform(FlaskForm):
    cardname = StringField(
        "Name on card", validators=[DataRequired(), Length(min=2, max=30)]
    )
    cardnum = StringField(
        "Card number", validators=[DataRequired(), Length(min=16, max=16)]
    )
    expire = DateField("Expiration date", format="%m-%Y", validators=[DataRequired()])
    cvc = StringField("CVC", validators=[DataRequired(), Length(min=3, max=3)])
    submit = SubmitField("Place order")


# Create a search form
class SearchForm(FlaskForm):
    search_query = StringField("Search", validators=[DataRequired()])
    submit = SubmitField("Search")

class NonNegativeIntegerField(IntegerField):
    def __init__(self, label='', validators=None, **kwargs):
        if validators is None:
            validators = [DataRequired(), NumberRange(min=0, message="Tickets cannot be negative")]
        else:
            validators.append(DataRequired())
            validators.append(NumberRange(min=0, message="Tickets cannot be negative"))
        super(NonNegativeIntegerField, self).__init__(label, validators, **kwargs)
        
class BookingForm(FlaskForm):
    movie_id = SelectField("Movie Title", coerce=int, validators=[DataRequired()])
    screening_time = SelectField(
        "Screening Time", coerce=str
    )
    booker_name = StringField("Name of Booker", validators=[DataRequired()]
                            )
    adult_tickets = NonNegativeIntegerField(
        "Number of Adult Tickets", default=0
        )
    child_tickets = NonNegativeIntegerField(
        "Number of Child Tickets", default=0
        )
    concession = RadioField(
        "Concession: ",
        choices=[("Yes", "Yes"), ("No", "No")],
        validators=[DataRequired()],
    )
    total_price = DecimalField("Total Price", places=2, render_kw={"readonly": True})
    submit = SubmitField("Book Tickets")
def no_swearing_content(form, field):
    swear_words = ["arse","stupid","bastard","bloody","cow","crap","ginger","arsehole","balls","bitch","bollocks","bullshit","feck","munter","pissed","pissed off","fuck off","slut","hoe","whore","shit","son of a bitch","titsbastard","cock","dick","dickhead","prick","pussy","twat","fuck","cunt","motherfucker","fucking","kill your self", "die","piece of shit"]

    content = field.data.lower()
    for word in swear_words:
        if word in content:
            raise ValidationError("Swearing is not allowed in the content.")

def no_swearing_title(form, field):
    swear_words = ["arse","stupid","bastard","bloody","cow","crap","ginger","arsehole","balls","bitch","bollocks","bullshit","feck","munter","pissed","pissed off","fuck off","slut","hoe","whore","shit","son of a bitch","titsbastard","cock","dick","dickhead","prick","pussy","twat","fuck","cunt","motherfucker","fucking","kill your self", "die","piece of shit"]

    title = field.data.lower()
    for word in swear_words:
        if word in title:
            raise ValidationError("Swearing is not allowed in the title.")

class CreatePosts(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), no_swearing_title])
    content = TextAreaField("Content", validators=[DataRequired(), no_swearing_content])
    submit = SubmitField("Post")