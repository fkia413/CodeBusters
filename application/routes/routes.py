from flask import render_template, url_for, flash, redirect, jsonify, request
from application import app, db, bcrypt

from application.modules.form import (
    Login,
    Registration,
    Payment,
    SearchForm,
    BookingForm,
    CreatePosts,
)

from application.modules.models import User, Movie, Booking, MovieScreen
import re
from decimal import Decimal


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/movies")
def movies():
    return render_template("movies.html")


@app.route("/classification")
def classification():
    return render_template("classification.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login()
    # If they enter wrong email or password, they cannot log in.
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash("Login successful!", "success")
            return redirect(url_for("home"))

        else:
            flash("Login Unsuccessful. Please check username and password", "danger")

    return render_template("login.html", form=form)


@app.route("/Register", methods=["GET", "POST"])
def register():
    form = Registration()

    if form.validate_on_submit():
        existing_email_user = User.query.filter(
            (User.email == form.email.data) | (User.username == form.username.data)
        existing_email_user = User.query.filter(
            (User.email == form.email.data) | (User.username == form.username.data)
        ).first()
        # if username and/or the email is already registered, they must choose different username or if email is registered must sign in
        if existing_email_user:
            if existing_email_user.email == form.email.data:
                flash(
                    "Email address is already registered. Please sign in or choose a different email address.",
                    "warning",
                )
            if existing_email_user.username == form.username.data:
                flash(
                    "Username is already registered. Please choose a different username.",
                    "warning",
                )
            return redirect(url_for("register"))
        else:
            # password pattern regex
            password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!])[A-Za-z\d@#$%^&+=!]{8,}$"

            # This checks if the password meets complexity requirements
            if not re.match(password_pattern, form.password.data):
                flash(
                    "Password does not meet complexity requirements. It must contain at least 1 lowercase letter, 1 uppercase letter, 1 digit, 1 special character, and be at least 8 characters long.",
                    "danger",
                )
                return redirect(url_for("register"))
            # This ensures that the password is in hashed format so no one can access the password. Also add the user who created account to the database
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
                "utf-8"
            )
            user = User(
            user = User(
                username=form.username.data,
                firstname=form.Firstname.data,
                lastname=form.lastname.data,
                email=form.email.data,
                password=hashed_password,
            )
            db.session.add(user)
            db.session.commit()
            flash(
                f"Account created for {form.Firstname.data} {form.lastname.data}! You are now able to log in",
                "success",
            )
            return redirect(url_for("login"))

    return render_template("register.html", form=form)

    
@app.route("/booking", methods = ['GET', 'POST'])
def booking():
    form = BookingForm()
    form.movie_id.choices = [(movie.movie_id, movie.title) for movie in Movie.query.all()]
    
    if form.validate_on_submit():
        movie_id = form.movie_id.data
        user_email = current_user.user_email
        concession = form.concession.data
        screening_time = form.screening_time.data
        adult_tickets = form.adult_tickets.data
        child_tickets = form.child_tickets.data
        selected_movie = Movie.query.filter_by(movie_id=movie_id).first()
        selected_screening = MovieScreen.query.filter_by(movie_id=movie_id, showing_time=screening_time).first()
        
        total_price = Decimal(0)
        
        adult_ticket_price = Tickets.adult_price  # Replace with your actual ticket prices
        child_ticket_price = Tickets.child_price  # Replace with your actual ticket prices
        total_price = (
            (Decimal(adult_ticket_price) * adult_tickets) +
            (Decimal(child_ticket_price) * child_tickets)
        )
        
        selected_screening = MovieScreen.query.filter_by(movie_id=movie_id, showing_time=screening_time).first()
        
        if selected_movie and selected_screening:
            booking = Booking(
                movie=selected_movie,
                screening_time=selected_screening,
                user_email=user_email,
                n_seats=adult_tickets + child_tickets,
                concession=concession,
                total_price=total_price, 
            )
        
        db.session.add(booking)
        db.session.commit()
        
        flash( 'Booking Successful!', 'success')
        return redirect(url_for('payment'))
        
    return render_template('booking.html', form=form )

@app.route("/get_screening_times")
def get_screening_times():
    movie_id = request.args.get("movie_id")
    selected_movie = Movie.query.get(movie_id)

    if selected_movie:
        # Get the screening times for the selected movie
        screening_times = MovieScreen.query.filter_by(movie_id=movie_id, showing_time=screening_time).all()
        return jsonify(screening_times)
    
    # Return an empty list or an appropriate response if the movie is not found
    return jsonify([])


@app.route("/payment", methods=["GET", "POST"])
def payment():
    form = Payment()
    return render_template(
        "payment.html",
        form=form,
    )


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/discussion")
def discussion():
    return render_template("discussion.html")


@app.route("/discussion/new", methods=["GET", "POST"])
def new():
    form = CreatePosts()
    if form.validate_on_submit():
        flash("Your post has been created!", "success")
        return redirect(url_for("discussion"))
    return render_template("create_post.html", title="New Post", form=form)

# passign stuff to navbar


@app.context_processor
def nav():
    form = SearchForm()
    return dict(form=form)


# create search function
@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    results = []  # This will store the search results

    if form.validate_on_submit():
        search_query = form.search_query.data

        # Perform a search based on the query (e.g., search movies, screenings, etc.)
        # search movies by title:
        results = Movie.query.filter(Movie.title.ilike(f'%{search_query}%')).all()

    return render_template('search.html', form=form, results=results)
