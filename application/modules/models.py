from application import db

# I used a length of 255 for a lot of them as it's common practice (compatibility, flexibility, avoiding data truncation)


class User(db.Model):
    user_email = db.Column(
        db.String(30), primary_key=True
    )  # Changed email to user_email -> updated on ERD
    username = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    hash = db.Column(db.String(60), nullable=False)
    # this can be removed
    #   -> flask_bcrypt handles the salt for us
    # salt = db.Column(db.String(30), nullable=False)
    booking = db.relationship("Booking", backref="user")
    discussion_board = db.relationship("DiscussionBoard", backref="user")


class Booking(db.Model):
    booking_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"), nullable=False)
    screening_time = db.Column(db.DateTime, nullable=False)
    user_email = db.Column(
        db.String(30), db.ForeignKey("user.user_email"), nullable=False
    )
    concession = db.Column(db.Boolean, nullable=False)
    payment = db.relationship("Payment", backref="booking")
    ticket_booking = db.relationship("TicketBooking", backref="booking")


class Ticket(db.Model):
    ticket_id = db.Column(db.Integer, primary_key=True)
    ticket_type = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    ticket_booking = db.relationship("TicketBooking", backref="ticket")


class TicketBooking(db.Model):
    ticket_booking_id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey("ticket.ticket_id"), nullable=False)
    booking_id = db.Column(
        db.Integer, db.ForeignKey("booking.booking_id"), nullable=False
    )
    seat_number = db.Column(db.String(10), nullable=False)


class Movie(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    poster_path = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    classification_id = db.Column(
        db.Integer, db.ForeignKey("classification.classification_id"), nullable=False
    )
    movie_genre = db.relationship("MovieGenre", backref="movie")
    movie_cast = db.relationship("MovieCast", backref="movie")
    movie_screen = db.relationship("MovieScreen", backref="movie")
    booking = db.relationship("Booking", backref="movie")


class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(
        db.Integer, db.ForeignKey("booking.booking_id"), nullable=False
    )
    timestamp = db.Column(db.DateTime, nullable=False)
    card_holder_name = db.Column(db.String(50), nullable=False)
    card_number = db.Column(db.String(16), nullable=False)
    expiry_date = db.Column(db.String(5), nullable=False)
    security_code = db.Column(db.String(3), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)


class MenuService(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_path = db.Column(db.String(255), nullable=False)


class DiscussionBoard(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    user_email = db.Column(
        db.String(30), db.ForeignKey("user.user_email"), nullable=False
    )
    content = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)


class Classification(db.Model):
    classification_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    icon_path = db.Column(db.String(255), nullable=False)
    rules_and_conditions = db.Column(db.String(255))
    movie = db.relationship("Movie", backref="classification")


class Genre(db.Model):
    genre_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    movie_genre = db.relationship("MovieGenre", backref="genre")


class MovieGenre(db.Model):
    movie_genre_id = db.Column(db.Integer, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.genre_id"), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"), nullable=False)


class Cast(db.Model):
    cast_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    role = db.Column(db.String(30), nullable=False)
    movie_cast = db.relationship("MovieCast", backref="cast")


class MovieCast(db.Model):
    movie_cast_id = db.Column(db.Integer, primary_key=True)
    cast_id = db.Column(db.Integer, db.ForeignKey("cast.cast_id"), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"), nullable=False)


class Screen(db.Model):
    screen_id = db.Column(db.Integer, primary_key=True)
    screen_number = db.Column(db.Integer, nullable=False, unique=True)
    screen_type = db.Column(db.String(20), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    seating_plan_img_path = db.Column(db.String(255))
    movie_screen = db.relationship("MovieScreen", backref="screen")


class MovieScreen(db.Model):
    movie_screen_id = db.Column(db.Integer, primary_key=True)
    screen_id = db.Column(db.Integer, db.ForeignKey("screen.screen_id"), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"), nullable=False)
    showing_time = db.Column(db.DateTime, nullable=False)
