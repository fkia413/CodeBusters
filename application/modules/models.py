from application import db

# I used a length of 255 for a lot of them as it's common practice (compatibility, flexibility, avoiding data truncation)


class User(db.Model):
    user_email = db.Column(
        db.String(30), primary_key=True
    )  # Changed email to user_email
    username = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    hash = db.Column(db.String(60), nullable=False)
    # this can be removed
    #   -> flask_bcrypt handles the salt for us
    # salt = db.Column(db.String(30), nullable=False)
    # orders = db.relationship('Booking', backref='customer')
    # Define the bookings relationship and specify back_populates
    bookings = db.relationship(
        "Booking", back_populates="customer", overlaps="orders,user"
    )
    orders = db.relationship(
        "Booking", back_populates="user", overlaps="bookings,customer"
    )


class Booking(db.Model):
    booking_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"))
    screening_time = db.Column(db.DateTime, nullable=False)
    n_seats = db.Column(db.Integer, nullable=False)
    user_email = db.Column(db.String(30), db.ForeignKey("user.user_email"))
    ticket_type = db.Column(db.String(20), nullable=False)
    concession = db.Column(db.Boolean, nullable=False)
    # user = db.relationship('User', backref='bookings')
    # Define the user and customer relationships and specify back_populates
    user = db.relationship(
        "User", back_populates="orders", overlaps="bookings,customer"
    )
    customer = db.relationship(
        "User", back_populates="bookings", overlaps="user,orders"
    )


class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    poster_path = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    classification_id = db.Column(
        db.Integer, db.ForeignKey("classification.classification_id")
    )
    genres = db.relationship("MovieGenre", backref="movie")
    # Add this line to create a relationship with Classification
    classification = db.relationship("Classification", backref="movies")


class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey("booking.booking_id"))
    timestamp = db.Column(db.DateTime, nullable=False)
    card_holder_name = db.Column(db.String(50), nullable=False)
    card_number = db.Column(db.String(16), nullable=False)
    expiry_date = db.Column(db.String(5), nullable=False)
    security_code = db.Column(db.String(3), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    booking = db.relationship("Booking", backref="payment")


class MenuService(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_path = db.Column(db.String(255), nullable=False)


class DiscussionBoard(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(30), db.ForeignKey("user.user_email"))
    content = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    user = db.relationship("User", backref="posts")


class Classification(db.Model):
    classification_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    icon_path = db.Column(db.String(255), nullable=False)
    rules_and_conditions = db.Column(db.String(255))


class Genre(db.Model):
    genre_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)


class MovieGenre(db.Model):
    movie_genre_id = db.Column(db.Integer, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.genre_id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"))


class Cast(db.Model):
    cast_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    role = db.Column(db.String(30), nullable=False)


class MovieCast(db.Model):
    movie_cast_id = db.Column(db.Integer, primary_key=True)
    cast_id = db.Column(db.Integer, db.ForeignKey("cast.cast_id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"))


class Screen(db.Model):
    screen_id = db.Column(db.Integer, primary_key=True)
    screen_number = db.Column(db.String(5), nullable=False)
    screen_type = db.Column(db.String(20), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    seating_plan_img_path = db.Column(db.String(255))


class MovieScreen(db.Model):
    movie_screen_id = db.Column(db.Integer, primary_key=True)
    screen_id = db.Column(db.Integer, db.ForeignKey("screen.screen_id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"))
    showing_time = db.Column(db.DateTime, nullable=False)
