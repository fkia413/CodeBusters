#from application import db
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean

# I used length of 255 as it's common practice (compatibility, flexibility, avoiding data truncation)

class User(db.Model):

    email = db.Column(db.String(30), primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    hash = db.Column(db.String(60), nullable=False) 
    salt = db.Column(db.String(30), nullable=False) 
    #orders = db.relationship('Order', backref='customer')

 
class Booking(db.Model):

    booking_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'))
    screening_time = db.Column(db.DateTime, nullable=False)  
    n_seats = db.Column(db.Integer, nullable=False)  
    user_email = db.Column(db.String(30), db.ForeignKey('user.user_email'))
    ticket_type = db.Column(db.String(20), nullable=False) 
    concession = db.Column(db.Boolean, nullable=False)  # Assuming it's a boolean
    # order_details = db.relationship('Order_detail', backref='order')


class Movie(db.Model):

    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)  
    poster_path = db.Column(db.String(255))  
    status = db.Column(db.String(20), nullable=False)  
    classification_id = db.Column(db.Integer, db.ForeignKey('classification.classification_id'))
    # order_details = db.relationship('Order_detail', backref='product')


class Payment(db.Model):

    payment_id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.booking_id'))
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
    type = db.Column(db.String(20))  
    price = db.Column(db.Float, nullable=False)  # Assuming it's a float, or do we want to use int instead?
    image_path = db.Column(db.String(255))  


class DiscussionBoard(db.Model):

    post_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(30), db.ForeignKey('user.user_email'))
    content = db.Column(db.String(255), nullable=False)  
    timestamp = db.Column(db.DateTime, nullable=False)  


class Classification(db.Model):
    
    classification_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    icon_path = db.Column(db.String(255))  
    rules_and_conditions = db.Column(db.String(255))  


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
    gender = db.Column(db.String(10))  
    role = db.Column(db.String(30)) 


class MovieCast(db.Model):
    
    movie_cast_id = db.Column(db.Integer, primary_key=True)
    cast_id = db.Column(db.Integer, db.ForeignKey('cast.cast_id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'))


class Screen(db.Model):
    
    screen_id = db.Column(db.Integer, primary_key=True)
    screen_number = db.Column(db.String(5))  
    screen_type = db.Column(db.String(20))  
    capacity = db.Column(db.Integer, nullable=False) 
    seating_plan_img_path = db.Column(db.String(255))  


class MovieScreen(db.Model):
    
    movie_screen_id = db.Column(db.Integer, primary_key=True)
    screen_id = db.Column(db.Integer, db.ForeignKey('screen.screen_id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'))
    showing_time = db.Column(db.DateTime, nullable=False)



