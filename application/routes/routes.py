from flask import render_template, url_for, flash, redirect, jsonify, request
from application import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
import random

from application.modules.form import (
    Login,
    Registration,
    Payment,
    SearchForm,
    BookingForm,
    CreatePosts,
)


from application.modules.models import *
import re
from decimal import Decimal


@app.route("/")
@app.route("/home")
def home():
    # a bit of trickery, we get random brand new movies
    total_movies = Movie.query.filter(
        Movie.release_date >= datetime(2023, 1, 1)
    ).count()

    # number of movies we want to retrieve
    # for now, we pick only 3 movies
    n_movies = 3

    # ensuring that the number of random movies is not greater than the number of available movies
    if n_movies > total_movies:
        n_movies = total_movies

    # generating random indices for selecting random movies
    random_indices = random.sample(range(1, total_movies + 1), n_movies)

    # we query the database for the movies with the generated indices
    random_movies = Movie.query.filter(Movie.movie_id.in_(random_indices)).all()

    # print(random_movies)  # debug

    # randomising order
    random.shuffle(random_movies)

    # rendering appropriate template
    return render_template("home.html", movies=random_movies)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/movies")
def movies():
    # retrieving all movies
    all_movies = Movie.query.all()
    # retrieving latest releases
    brand_new_releases = Movie.query.filter(Movie.release_date >= datetime(2023, 1, 1))

    # banner movies
    n_banner_movies = 5

    # ensuring that the number of random movies is not greater than the number of available movies
    if n_banner_movies > len(all_movies):
        n_banner_movies = len(all_movies)

    # randomising order
    banner_movies = random.sample(all_movies, n_banner_movies)

    return render_template(
        "movies.html",
        all_movies=all_movies,
        brand_new_releases=brand_new_releases,
        banner_movies=banner_movies,
    )


@app.route("/movies/<int:movie_id>")
def movie_details(movie_id: int):
    # retrieving movie using passed movie_id
    movie = Movie.query.filter_by(movie_id=movie_id).first()

    # retrieving genres of the movie
    genres = ", ".join(
        [
            genre.name
            for genre in Genre.query.join(MovieGenre)
            .filter(MovieGenre.movie_id == movie_id)
            .all()
        ]
    )

    # retrieving cast of the movie
    directors = ", ".join(
        [
            f"{cast.first_name} {cast.last_name}"
            for cast in Cast.query.join(MovieCast)
            .filter(MovieCast.movie_id == movie_id)
            .filter(Cast.role == "Director")
            .all()
        ]
    )

    actors = ", ".join(
        [
            f"{cast.first_name} {cast.last_name}"
            for cast in Cast.query.join(MovieCast)
            .filter(MovieCast.movie_id == movie_id)
            .filter(Cast.role == "Actor")
            .all()
        ]
    )

    # get showing times
    showing_times = [
        f"{screen.showing_time.strftime('%d.%m.%Y %H:%M')} - {screen.screen.screen_type}"
        for screen in MovieScreen.query.filter_by(movie_id=movie_id).all()
    ]

    # rendering appropriate template
    return render_template(
        "movie_details.html",
        movie=movie,
        genres=genres,
        directors=directors,
        actors=actors,
        showing_times=showing_times,
    )


@app.route("/classification")
def classification():
    classification = Classification.query.all()
    return render_template("classification.html", classifications=classification)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = Login()
    # If they enter wrong email or password, they cannot log in.
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.hash, form.password.data):
            login_user(user, remember=form.remember.data)

            return redirect(url_for("home"))

        else:
            flash("Login Unsuccessful. Please check username and password", "danger")

    return render_template("login.html", form=form)


@app.route("/Register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    form = Registration()

    if form.validate_on_submit():
        existing_email_user = User.query.filter(
            (User.user_email == form.email.data) | (User.username == form.username.data)
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
                username=form.username.data,
                first_name=form.Firstname.data,
                last_name=form.lastname.data,
                user_email=form.email.data,
                hash=hashed_password,
            )
            db.session.add(user)
            db.session.commit()
            flash(
                f"Account created for {form.Firstname.data} {form.lastname.data}! You are now able to log in",
                "success",
            )
            return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/booking", methods=["GET", "POST"])
def booking():
    form = BookingForm()
    form.movie_id.choices = [
        (movie.movie_id, movie.title) for movie in Movie.query.all()
    ]

    if form.validate_on_submit():
        movie_id = form.movie_id.data
        user_email = current_user.user_email
        concession = form.concession.data
        screening_time = form.screening_time.data
        adult_tickets = form.adult_tickets.data
        child_tickets = form.child_tickets.data
        selected_movie = Movie.query.filter_by(movie_id=movie_id).first()
        selected_screening = MovieScreen.query.filter_by(
            movie_id=movie_id, showing_time=screening_time
        ).first()

        total_price = Decimal(0)

        adult_ticket_price = (
            Ticket.adult_price
        )  # Replace with your actual ticket prices
        child_ticket_price = (
            Ticket.child_price
        )  # Replace with your actual ticket prices
        total_price = (Decimal(adult_ticket_price) * adult_tickets) + (
            Decimal(child_ticket_price) * child_tickets
        )

        selected_screening = MovieScreen.query.filter_by(
            movie_id=movie_id, showing_time=screening_time
        ).first()

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

        flash("Booking Successful!", "success")
        return redirect(url_for("payment"))

    return render_template("booking.html", form=form)


@app.route("/get_screening_times")
def get_screening_times():
    movie_id = request.args.get("movie_id")
    selected_movie = Movie.query.get(movie_id)

    if selected_movie:
        # Get the screening times for the selected movie
        screening_times = MovieScreen.query.filter_by(
            movie_id=movie_id, showing_time=screening_times
        ).all()
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
    posts = DiscussionBoard.query.all()
    return render_template("discussion.html")


@app.route("/discussion/new", methods=["GET", "POST"])
def new():
    form = CreatePosts()
    if form.validate_on_submit():
        post = DiscussionBoard(
            title=form.title.data, content=form.content.data, author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created!", "success")
        return redirect(url_for("discussion"))
    return render_template("create_post.html", title="New Post", form=form)


# passign stuff to navbar


@app.context_processor
def nav():
    form = SearchForm()
    return dict(form=form)


# create search function
@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    results = []  # This will store the search results

    if form.validate_on_submit():
        search_query = form.search_query.data

        # Perform a search based on the query (e.g., search movies, screenings, etc.)
        # search movies by title:
        results = Movie.query.filter(Movie.title.ilike(f"%{search_query}%")).all()

    return render_template("search.html", form=form, results=results)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/account")
@login_required
def account():
    return render_template("account.html", title=account)
