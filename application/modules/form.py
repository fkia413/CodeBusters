from flask_wtf import FlaskForm
from datetime import datetime

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
from wtforms.validators import (
    DataRequired,
    Length,
    Optional,
    EqualTo,
    NumberRange,
    ValidationError,
)


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


# custom validator for the expiry date
class CardExpiryDateCheck:
    def __init__(self, message=None):
        if not message:
            message = "Please re-enter your card's expiry date"
        self.message = message

    def __call__(self, form, field):
        expiry_date = field.data
        today = datetime.today().date()
        if expiry_date < today:
            raise ValidationError(self.message)


# custom validator for the security code
class CardSecurityCodeCheck:
    def __init__(self, message=None):
        if not message:
            message = "Please re-enter your card's CVV/CVC code"
        self.message = message

    def __call__(self, form, field):
        security_code = field.data
        if not (100 <= security_code <= 999):
            raise ValidationError(self.message)


# custom validator for the card number
class CardNumberCheck:
    def __init__(self, message=None):
        if not message:
            message = "Please re-enter your card number"
        self.message = message

    def __call__(self, form, field):
        # remove white spaces
        card_number = field.data.replace(" ", "")
        if not card_number.isdigit() or len(card_number) != 16:
            raise ValidationError(self.message)


class Paymentform(FlaskForm):
    cardholder_name = StringField("Cardholder Name", validators=[DataRequired()])
    card_number = StringField(
        "Card Number",
        validators=[
            DataRequired(),
            CardNumberCheck("Please enter a valid 16-digit card number"),
        ],
    )
    expire = DateField(
        "Expiration date",
        validators=[
            DataRequired(),
            CardExpiryDateCheck("The card seems to have expired"),
        ],
    )
    cvc = IntegerField(
        "CVC",
        validators=[
            DataRequired(),
            CardSecurityCodeCheck("Please enter a valid 3-digit security code"),
        ],
    )
    submit = SubmitField("Place order")


# Create a search form
class SearchForm(FlaskForm):
    search_query = StringField("Search", validators=[DataRequired()])
    submit = SubmitField("Search")


class NonNegativeIntegerField(IntegerField):
    def __init__(self, label="", validators=None, **kwargs):
        if validators is None:
            validators = [
                DataRequired(),
                NumberRange(min=0, message="Tickets cannot be negative"),
            ]
        else:
            validators.append(DataRequired())
            validators.append(NumberRange(min=0, message="Tickets cannot be negative"))
        super(NonNegativeIntegerField, self).__init__(label, validators, **kwargs)


class BookingForm(FlaskForm):
    movie_id = StringField("Movie", validators=[DataRequired()])
    screen_type = StringField("Screen type", validators=[DataRequired()])
    screening_time = StringField("Screening time", validators=[DataRequired()])
    booker_email = StringField("Booker email", validators=[DataRequired()])
    adult_tickets = IntegerField("# Adult tickets", default=1)
    child_tickets = IntegerField("# Child tickets", default=0)
    concession = RadioField(
        "Concession",
        choices=[(True, "Yes"), (False, "No")],
        default=False,  # You can set the default value to "No"
        validators=[DataRequired()],
    )
    total_price = DecimalField("Total Price", places=2, render_kw={"readonly": True})
    submit = SubmitField("Book Tickets")


def no_swearing_content(form, field):
    swear_words = [
        "arse",
        "stupid",
        "bastard",
        "bloody",
        "cow",
        "crap",
        "ginger",
        "arsehole",
        "balls",
        "bitch",
        "bollocks",
        "bullshit",
        "feck",
        "munter",
        "pissed",
        "pissed off",
        "fuck off",
        "slut",
        "hoe",
        "whore",
        "shit",
        "son of a bitch",
        "titsbastard",
        "cock",
        "dick",
        "dickhead",
        "prick",
        "pussy",
        "twat",
        "fuck",
        "cunt",
        "motherfucker",
        "fucking",
        "kill your self",
        "die",
        "piece of shit",
    ]

    content = field.data.lower()
    for word in swear_words:
        if word in content:
            raise ValidationError("Swearing is not allowed in the content.")


def no_swearing_title(form, field):
    swear_words = [
        "arse",
        "stupid",
        "bastard",
        "bloody",
        "cow",
        "crap",
        "ginger",
        "arsehole",
        "balls",
        "bitch",
        "bollocks",
        "bullshit",
        "feck",
        "munter",
        "pissed",
        "pissed off",
        "fuck off",
        "slut",
        "hoe",
        "whore",
        "shit",
        "son of a bitch",
        "titsbastard",
        "cock",
        "dick",
        "dickhead",
        "prick",
        "pussy",
        "twat",
        "fuck",
        "cunt",
        "motherfucker",
        "fucking",
        "kill your self",
        "die",
        "piece of shit",
    ]

    title = field.data.lower()
    for word in swear_words:
        if word in title:
            raise ValidationError("Swearing is not allowed in the title.")


class CreatePosts(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), no_swearing_title])
    content = TextAreaField("Content", validators=[DataRequired(), no_swearing_content])
    submit = SubmitField("Post")
