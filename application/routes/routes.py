from flask import render_template, url_for, flash, redirect
from application import app, db, bcrypt
<<<<<<< HEAD
from application.modules.form import Login, Registration, Checkout, Payment, Search, Booking
from application.modules.models import User, Booking, Screen, Movie
import re

=======
from application.modules.form import Login, Registration, Checkout, Payment, Search
from application.modules.models import User
import re


>>>>>>> cc1571d53c9252e5499ec241e44b6b84f044c198
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/movies")
def movies():
    return render_template('movies.html')

@app.route("/classification")
def classification():
    return render_template('classification.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    #If they enter wrong email or password, they cannot log in. 
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
<<<<<<< HEAD
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
            
=======
        if user and bcrypt.check_password_hash(user.hash, form.password.data):
            flash("Login successful!", "success")
            return redirect(url_for("home"))

>>>>>>> cc1571d53c9252e5499ec241e44b6b84f044c198
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    
    return render_template('login.html', form=form)

@app.route("/Register", methods=['GET', 'POST'])
def register():
    form = Registration()

    if form.validate_on_submit():
<<<<<<< HEAD
        
        existing_email_user = User.query.filter((User.email == form.email.data) | (User.username == form.username.data)).first()
            # if username and/or the email is already registered, they must choose different username or if email is registered must sign in
        if existing_email_user:
            if existing_email_user.email == form.email.data:
                flash('Email address is already registered. Please sign in or choose a different email address.', 'warning')
            if existing_email_user.username == form.username.data:
                flash('Username is already registered. Please choose a different username.', 'warning')
            return redirect(url_for('register'))
=======
        existing_user = User.query.filter(
            (User.user_email == form.email.data) | (User.username == form.username.data)
        ).first()
        # if username and/or the email is already registered, they must choose different username or if email is registered must sign in
        if existing_user:
            if existing_user.user_email == form.email.data:
                flash(
                    "Email address is already registered. Please sign in or choose a different email address.",
                    "warning",
                )
            if existing_user.username == form.username.data:
                flash(
                    "Username is already registered. Please choose a different username.",
                    "warning",
                )
            return redirect(url_for("register"))
>>>>>>> cc1571d53c9252e5499ec241e44b6b84f044c198
        else:
            # This checks if the password meets complexity requirements
            if not re.match(password_pattern, form.password.data):
                flash('Password does not meet complexity requirements. It must contain at least 1 lowercase letter, 1 uppercase letter, 1 digit, 1 special character, and be at least 8 characters long.', 'danger')
                return redirect(url_for('register'))
            # This ensures that the password is in hashed format so no one can access the password. Also add the user who created account to the database
<<<<<<< HEAD
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, firstname=form.Firstname.data, lastname=form.lastname.data, email=form.email.data, password=hashed_password)
=======
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
                "utf-8"
            )
            user = User(
                user_email=form.email.data,
                username=form.username.data,
                first_name=form.Firstname.data,
                last_name=form.lastname.data,
                hash=hashed_password,
            )
>>>>>>> cc1571d53c9252e5499ec241e44b6b84f044c198
            db.session.add(user)
            db.session.commit()
            flash(f'Account created for {form.Firstname.data} {form.lastname.data}! You are now able to log in', 'success')
            return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.context_processor
def tickets():
    form = Booking()
    return dict(form=form)
    
@app.route("/booking", methods = ['GET', 'POST'])
def booking():
    form = Booking()
    form.movie_id.choices = [(movie.id, movie.title) for movie in Movie.query.all()]
    if form.validate_on_submit():
        movie_id = form.movie_id.data
        user_email = current_user.email
        ticket_type = form.ticket_type.data
        concession = form.concession.data
        
        booking = Booking(
            movie_id=movie_id,
            user_email=user_email,
            ticket_type=ticket_type,
            concession=concession
        )
        
        db.session.add(booking)
        db.session.commit()
        
        flash( 'Booking Successful!', 'success')
        return redirect(url_for('paymment'))
        
    return render_template('booking.html', form=form)

@app.route("/checkout")
def checkout():
    form = Checkout()
    return render_template('checkout.html', form = form )

@app.route("/payment", methods=['GET', 'POST'])
def payment():
    form = Payment()
    return render_template('payment.html', form = form,)

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/discussion")
def discussion():
    
    return render_template('discussion.html')

@app.route("/discussion/new", methods = ['GET', 'POST'])
def new():
    form = CreatePosts()
    if form.validate_on_submit():
        flash('Your post has been created!', 'success')
        return redirect(url_for('discussion'))
    return render_template('create_post.html', title = 'New Post', form = form)

#passing stuff to navbar

@app.context_processor
def nav():
    form = Search()
    return dict(form=form)

# create search function
@app.route("/search", methods = ["POST"])
def search():
    form = Search()
    if form.validate_on_submit():
        # movie.searched = form.searched.data
        return render_template("search.html", form = form ) # searched = movie.searched