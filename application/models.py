#from application import db
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 


class User(db.Model):

    email = db.Column(db.String(30), primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    hash = 
    salt = 
    #orders = db.relationship('Order', backref='customer')

 
class Booking(db.Model):

    booking_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'))
    screening_time = 
    n_seats = 
    user_email = db.Column(db.String(30), db.ForeignKey('user.user_email'))
    ticket_type = 
    concession = 
    # order_date = db.Column(db.DateTime)
    # status = db.Column(db.Boolean)  # True = Active cart, False = Checked out
    # is_cart = db.Column(db.Boolean, default=False)  # True if this order is a cart
    # order_details = db.relationship('Order_detail', backref='order')


class Movie(db.Model):

    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    release_date = 
    poster_path = 
    status = 
    classification_id = db.Column(db.Integer, db.ForeignKey('classification.classification_id'))
    # description = db.Column(db.String(500), nullable=False)
    # price = db.Column(db.Float)
    # stock_quantity = db.Column(db.Integer)
    # order_details = db.relationship('Order_detail', backref='product')


class Payment(db.Model):

    payment_id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.booking_id'))
    timestamp = 
    card_holder_name = 
    card_number = 
    expiry_date = 
    security_code = 
    amount = 
    status = 
    # order_detail_id = db.Column(db.Integer, primary_key=True)
    # order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
    # product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    # quantity = db.Column(db.Integer, nullable = False)
    # price = db.Column(db.Float, nullable=False)


class MenuService(db.Model):

    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    type = 
    price = 
    image_path = 


class DiscussionBoard(db.Model):

    post_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(30), db.ForeignKey('user.user_email'))
    content = 
    timestamp = 


class Classification(db.Model):
    
    classification_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    icon_path = 
    rules_and_conditions = 


class Genre(db.Model):
    
    genre_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)


class MovieGenre(db.Model):
    
    movie_genre_id = db.Column(db.Integer, primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.genre_id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'))


class Cast(db.Model):
    
    cast_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    gender = 
    role = 


class MovieCast(db.Model):
    
    movie_cast_id = db.Column(db.Integer, primary_key=True)
    cast_id = db.Column(db.Integer, db.ForeignKey('cast.cast_id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'))


class Screen(db.Model):
    
    screen_id = db.Column(db.Integer, primary_key=True)
    screen_number = 
    screen_type = 
    capacity = 
    seating_plan_img_path = 


class MovieScreen(db.Model):
    
    movie_screen_id = db.Column(db.Integer, primary_key=True)
    screen_id = db.Column(db.Integer, db.ForeignKey('screen.screen_id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'))
    showing_time = 



