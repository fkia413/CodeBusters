from flask import render_template, url_for, flash, redirect, jsonify, request, session
from application import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime
import random
from sqlalchemy import desc

from application.modules.form import (
    Login,
    Registration,
    Paymentform,
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
    classifications = Classification.query.all()
    return render_template("classification.html", classifications=classifications)


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
            if existing_email_user.user_email == form.email.data:
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
@app.route("/booking/<int:movie_id>", methods=["GET", "POST"])
@app.route("/booking/<int:movie_id>/<int:screening_id>", methods=["GET", "POST"])
# @login_required  # Protect the route with login_required
def booking():
    form = BookingForm()
    form.movie_id.choices = [
        (movie.movie_id, movie.title) for movie in Movie.query.all()
    ]

    # Fetch ticket prices from the database
    ticket_prices = {
        "adult_price": Ticket.query.filter_by(ticket_type="Adult").first().price,
        "child_price": Ticket.query.filter_by(ticket_type="Child").first().price,
    }

    if form.validate_on_submit() and request.method == "POST":
        movie_id = form.movie_id.data
        user_email = current_user.user_email
        concession = form.concession.data
        screening_time = form.screening_time.data
        adult_tickets = form.adult_tickets.data
        child_tickets = form.child_tickets.data
        selected_movie = Movie.query.get(movie_id)
        selected_screening = MovieScreen.query.filter_by(
            movie_id=movie_id, showing_time=screening_time
        ).first()

        total_price = Decimal(0)

        adult_ticket_price = ticket_prices["adult_price"]
        child_ticket_price = ticket_prices["child_price"]
        total_price = (Decimal(adult_ticket_price) * adult_tickets) + (
            Decimal(child_ticket_price) * child_tickets
        )

        if selected_movie and selected_screening:
            booking = Booking(
                movie=selected_movie,
                screening_time=selected_screening,
                user_email=user_email,
                concession=concession,
            )
            total_price=total_price

            db.session.add(booking)
            db.session.commit()

            flash("Booking Successful!", "success")
            return redirect(url_for("payment"))

    return render_template("booking.html", form=form, ticket_prices=ticket_prices)


@app.route("/get_screening_times", methods=["GET"])
def get_screening_times():
    movie_id = request.args.get("movie_id")
    selected_movie = Movie.query.get(movie_id)

    if selected_movie:
        # Get the screening times for the selected movie
            showing_times = [
                f"{screen.showing_time.strftime('%d.%m.%Y %H:%M')} - {screen.screen.screen_type}"
                for screen in MovieScreen.query.filter_by(movie_id=movie_id).all()
            ]
            return jsonify(showing_times)

    # Return an empty list or an appropriate response if the movie is not found
    return jsonify([])


@app.route("/get_ticket_prices", methods=["GET"])
def get_ticket_prices():
    # Fetch ticket prices from the database
    adult_price = Ticket.query.filter_by(ticket_type="Adult").first().price
    child_price = Ticket.query.filter_by(ticket_type="Child").first().price

    # Return ticket prices as JSON
    return jsonify({"adult_price": adult_price, "child_price": child_price})


@app.route("/payment", methods=["GET", "POST"])
def payment():
    form = Paymentform() 
    if form.validate_on_submit() and request.method == "POST":
        # total_price = session["total_price"]
        total_price = 30.99
        booking = Booking.query.filter_by(booking_id = 1).first()
        hashed_card_number = bcrypt.hashpw(str(form.cardnum.data).encode(), bcrypt.gensalt())
        hashed_security_code = bcrypt.hashpw(str(form.cvc.data).encode(), bcrypt.gensalt())
        print(booking , form.cardname.data, hashed_card_number.decode(), form.expire.data.strftime("%m-%Y"), hashed_security_code.decode())
        
        payment = Payment(
            booking = booking,
            card_holder_name=form.cardname.data,
            card_number=hashed_card_number.decode(),  
            expiry_date=form.expire.data.strftime("%m-%Y"),
            security_code=hashed_security_code.decode(), 
            amount= total_price, 
            status= "pending",
            timestamp = datetime.now()

        )

        db.session.add(payment)
        db.session.commit()

        return redirect(url_for("success")) 


    return render_template('payment.html', form=form)


@app.route("/services")
def services():
    # Query your MenuService database model to fetch menu items
    menu_items = MenuService.query.all()
    # Render the HTML template with menu_items
    return render_template("services.html", menu_items=menu_items)


@app.route("/discussion")
def discussion():
    # return all posts from newest to oldest
    posts = DiscussionBoard.query.order_by(desc(DiscussionBoard.timestamp)).all()
    return render_template("discussion.html", posts=posts)


@app.route("/discussion/new", methods=["GET", "POST"])
@login_required
def new():
    form = CreatePosts()

    if form.validate_on_submit() and request.method == "POST":
        current_time = datetime.utcnow()

        post = DiscussionBoard(
            title=form.title.data,
            content=form.content.data,
            user_email=current_user.user_email,  # Use current_user.email
            timestamp=current_time,
        )
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created!", "success")
        return redirect(url_for("discussion"))
    else:
        flash("You must be logged in to create a post.", "danger")
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
