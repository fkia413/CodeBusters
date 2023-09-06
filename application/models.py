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
    name = db.Column(db.String(30), nullable=False)
    # description = db.Column(db.String(500), nullable=False)
    # price = db.Column(db.Float)
    # stock_quantity = db.Column(db.Integer)
    # order_details = db.relationship('Order_detail', backref='product')

 

class Payment(db.Model):

    # order_detail_id = db.Column(db.Integer, primary_key=True)
    # order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'), nullable=False)
    # product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    # quantity = db.Column(db.Integer, nullable = False)
    # price = db.Column(db.Float, nullable=False)