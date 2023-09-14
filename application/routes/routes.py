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


# COMPLETED
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


# COMPLETED
@app.route("/about")
def about():
    return render_template("about.html")


# COMPLETED
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


# COMPLETED
@app.route("/movies/<int:movie_id>")
def movie_details(movie_id: int):
    # retrieving movie using passed movie_id
    movie = Movie.query.filter_by(movie_id=movie_id).first()

    # TODO: This data retrieval (genres, directors, actors) could be moved into separate functions for increased modularity

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

    showing_times = set()
    screens = MovieScreen.query.filter_by(movie_id=movie_id).all()

    for screen in screens:
        showing_times.add(screen.showing_time.strftime("%d.%m.%Y - %H:%M"))

    sorted_times = sorted(
        showing_times, key=lambda x: datetime.strptime(x, "%d.%m.%Y - %H:%M")
    )

    # rendering appropriate template
    return render_template(
        "movie_details.html",
        movie=movie,
        genres=genres,
        directors=directors,
        actors=actors,
        showing_times=sorted_times,
    )


# COMPLETED
@app.route("/classification")
def classification():
    classifications = Classification.query.all()
    return render_template("classification.html", classifications=classifications)


@app.route("/login", methods=["GET", "POST"])
def login():
    # RN: I added this here simply cause it was displaying flash messages which were coming from other pages as well
    # TODO: Look into how to properly clean flash messages after having displayed them. I never used them so I'm not quite sure how to do it.
    session.pop("_flashes", None)

    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = Login()
    # If they enter wrong email or password, they cannot log in.
    if form.validate_on_submit() and request.method == "POST":
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.hash, form.password.data):
            login_user(user, remember=form.remember.data)

            return redirect(url_for("home"))

        else:
            flash("Login Unsuccessful. Please check username and password", "danger")

    return render_template("login.html", form=form)


# COMPLETED
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
@login_required  # Protect the route with login_required
def booking():
    # two options
    # direct access to booking page
    # redirect from movie details page

    # checking if the user clicked on the booking link in the navbar
    # or if he accessed the booking page through the buy tickets button in each movie details page

    if request.args.get("movie_id") is not None:
        movie_id = int(request.args.get("movie_id"))
    else:
        movie_id = "-1"

    # creating booking form
    form = BookingForm()

    # displaying all movies
    form.movie_id.choices = [
        (movie.movie_id, movie.title) for movie in Movie.query.all()
    ]

    # Fetch ticket prices from the database
    ticket_prices = {
        "adult_price": Ticket.query.filter_by(ticket_type="Adult").first().price,
        "child_price": Ticket.query.filter_by(ticket_type="Child").first().price,
    }

    if form.validate_on_submit() and request.method == "POST":
        # movie_id = form.movie_id.data
        # selected_movie = Movie.query.filter_by(movie_id=movie_id).first()

        # this is the selected screening time, different from the showing_time field in the MovieScreen table which is used to contain all the movie screening times
        # selected_screening_time = datetime.strptime(
        #    form.screening_time.data, "%d.%m.%Y - %H:%M"
        # )
        # n_adult_tickets = form.adult_tickets.data
        # n_child_tickets = form.child_tickets.data
        # concession = form.concession.data == "True"

        # checking that at least one ticket is selected
        if form.adult_tickets.data <= 0 and form.child_tickets.data <= 0:
            return render_template(
                "booking.html", form=form, ticket_prices=ticket_prices
            )
        else:
            # storing everythig into a session var
            # this is done so that we don't create the booking/keep track of it
            # until the payment goes through and is successful
            session["booking_data"] = {
                "movie_id": form.movie_id.data,
                "screen_type": form.screen_type.data,
                "screening_time": datetime.strptime(
                    form.screening_time.data, "%d.%m.%Y - %H:%M"
                ),
                "n_adult_tickets": form.adult_tickets.data,
                "n_child_tickets": form.child_tickets.data,
                "concession": form.concession.data,
                "total_price": form.total_price.data,
            }

            # creating booking
            # booking = Booking(
            #    movie=selected_movie,
            #    screening_time=selected_screening_time,
            #    user=current_user,
            #    concession=concession,
            # )

            # db.session.add(booking)

            # we need to also keep track of the tickets and their types for each booking
            # TODO: In future iterations, the seat_number field could also be used (TicketBooking table)

            # for _ in range(n_adult_tickets):
            #    ticket = Ticket.query.filter_by(ticket_type="Adult").first()
            #    adult_ticket = TicketBooking(
            #        booking=booking, ticket=ticket, seat_number="TMP"
            #    )

            #    db.session.add(adult_ticket)

            # for _ in range(n_child_tickets):
            #    ticket = Ticket.query.filter_by(ticket_type="Child").first()
            #    child_ticket = TicketBooking(
            #        booking=booking, ticket=ticket, seat_number="TMP"
            #    )

            #    db.session.add(child_ticket)

            # lastly, we need to keep track of the capacity for each screen
            # this can be considered simply a start, in future iterations we could indicate sold out tickets
            # TODO: Update capacity now? or later when payment is done?
            # screen_type = form.screen_type.data

            # db.session.commit()

            return redirect(url_for("payment"))

    if movie_id is not None:
        return render_template(
            "booking.html", form=form, ticket_prices=ticket_prices, movie_id=movie_id
        )
    else:
        return render_template("booking.html", form=form, ticket_prices=ticket_prices)


@app.route("/get_screening_times/<int:movie_id>/<string:screen_type>", methods=["GET"])
def get_screening_times(movie_id: int, screen_type: str):
    # get the screening times of a particular movie, according also to the selected screen type
    selected_movie = Movie.query.get(movie_id)
    # print(movie_id)  # debug
    # print(screen_type)  # debug

    # TODO: Need to retrieve only specified screen_type
    if selected_movie:
        showing_times = set()
        screens = MovieScreen.query.filter_by(movie_id=movie_id).all()

        for screen in screens:
            # retrieving only the screening times which are avaialble on the selected screen types
            if screen.screen.screen_type == screen_type:
                # print(screen.screen.screen_id) # debug
                # print(screen.screen.screen_number) # debug
                # print(screen.screen.capacity) # debug
                # print(screen.screen.screen_type) # debug

                showing_times.add(screen.showing_time.strftime("%d.%m.%Y - %H:%M"))

        sorted_times = sorted(
            showing_times, key=lambda x: datetime.strptime(x, "%d.%m.%Y - %H:%M")
        )

        return jsonify(sorted_times)

    # Return an empty list or an appropriate response if the movie is not found
    return jsonify([])


@app.route("/get_screen_types/<int:movie_id>", methods=["GET"])
def get_screen_types(movie_id: int):
    # here, we get all the screens where the movie is being displayed
    # reason for using a set is to avoid duplicates
    screen_types = set()
    screens = MovieScreen.query.filter_by(movie_id=movie_id).all()

    for screen in screens:
        screen_types.add(screen.screen.screen_type)

    return jsonify(list(screen_types))


@app.route("/get_ticket_prices", methods=["GET"])
def get_ticket_prices():
    # Fetch ticket prices from the database
    adult_price = Ticket.query.filter_by(ticket_type="Adult").first().price
    child_price = Ticket.query.filter_by(ticket_type="Child").first().price

    # Return ticket prices as JSON
    return jsonify({"adult_price": adult_price, "child_price": child_price})


@app.route("/payment", methods=["GET", "POST"])
@login_required
def payment():
    # retrieve the booking data
    booking_data = session.get("booking_data")

    # handle booking data missing from the session
    if not booking_data:
        # flash("Booking data not found. Please complete the booking first.", "error")
        return redirect(url_for("booking"))

    form = Paymentform()
    if form.validate_on_submit() and request.method == "POST":
        # first, we perform the entire payment processing stuff
        # TODO: In future iterations, storing payment data within an external processor would definitely be more sensible to do

        # TODO: Here, we'd pass the payment information directly to the external payment processor, following the guideliens that it requires

        # TODO: I'm not too fond of the idea of storing payment details in our own database, this task could and should be left to the external payment processor. However, it is a bit late to change the ERD so we will just encrypt them and store them in the Payment table. Regarding encryption, I will use bcrypt. However, the latter is and should not be used for hashing such data. Other encryption algorithms made for this purpose should be used (i.e., AES -> pip install cryptography)

        cardholder_name = form.cardholder_name.data
        card_number = bcrypt.generate_password_hash(form.card_number.data).decode(
            "utf-8"
        )
        expire = form.expire.data
        cvc = bcrypt.generate_password_hash(str(form.cvc.data)).decode("utf-8")

        payment_processor_result = process_payment(
            cardholder_name, card_number, expire, cvc
        )

        if payment_processor_result == "success":
            selected_movie = Movie.query.filter_by(
                movie_id=booking_data["movie_id"]
            ).first()

            # creating booking
            booking = Booking(
                movie=selected_movie,
                screening_time=booking_data["screening_time"],
                user=current_user,
                concession=bool(booking_data["concession"]),
            )

            db.session.add(booking)

            # we need to also keep track of the tickets and their types for each booking
            # TODO: In future iterations, the seat_number field could also be used (TicketBooking table)

            for _ in range(booking_data["n_adult_tickets"]):
                ticket = Ticket.query.filter_by(ticket_type="Adult").first()
                adult_ticket = TicketBooking(
                    booking=booking, ticket=ticket, seat_number="TMP"
                )

                db.session.add(adult_ticket)

            for _ in range(booking_data["n_child_tickets"]):
                ticket = Ticket.query.filter_by(ticket_type="Child").first()
                child_ticket = TicketBooking(
                    booking=booking, ticket=ticket, seat_number="TMP"
                )

                db.session.add(child_ticket)

            # we need to keep track of the capacity for each screen
            # this can be considered simply a start, in future iterations we could indicate sold out tickets
            # Real capacity management left out for now, a bit complicated and time is limited.

            #   TODO: Add checks on the front end (i.e., hide screening times if capacity is zero)
            #   TODO: Create separate function to send confirmation email to users?
            #   TODO: Randomise screen number (e.g., if there are multiple types of the selected screen type)
            #   TODO: Entire seat picking system + screen management (using bokking data - grab movie, find available screens, compare with selected screen type, match selected screening time to showing_time field in MovieScreen, do things with the capacity management)

            # TODO: The part commented below would never work. Given the current design there is no real way of keeping track of the capacity of each screen for each screening time. We do not track the capacity of the screens for every screening time, we just have a general capacity field which holds the amount of seats. A new capacity field in the MovieScreen table is needed in order to track the capacity at each screening time, and then also perform capacity management + all the above

            # Here, I just simply decrease the capacity of the screen
            # this is bad, but it is just to show how the tables interact with each other
            # print(booking_data["screen_type"])

            # screens = MovieScreen.query.filter_by(
            #     movie_id=booking_data["movie_id"]
            # ).all()

            # print(screens)

            # for screen in screens:
            #     if screen.screen.screen_type == booking_data["screen_type"]:
            #         print(screen.screen.screen_number)
            #         print(screen.screen.screen_id)
            #         print(screen.screen.capacity)
            #         print(screen.screen.screen_type)

            # and we keep track of the payment for transaction purposes, as well as the reasons explained above
            payment = Payment(
                booking=booking,
                timestamp=datetime.now(),
                card_holder_name=cardholder_name,
                card_number=card_number,
                expiry_date=expire,
                security_code=cvc,
                amount=booking_data["total_price"],
                status="Paid",
            )

            db.session.add(payment)

            db.session.commit()

            # cleaning session booking data
            session.pop("booking_data", None)

            # TODO: Do something more rather than just redirecting to the homepage
            # TODO: Create success page
            # flash("Booking complete, check your email soon.", "success")  # debug
            return redirect(url_for("home"))
        else:
            # this is just a placeholder view
            # TODO: Improve this redirect, find out what the real problem was (payment things?) and display a message for end user
            return redirect(url_for("fail"))

    return render_template("payment.html", form=form)


@app.route("/success")
def success():
    return "Booking complete"


@app.route("/fail")
def fail():
    return "Booking not accepted. Payment problems."


# COMPLETED
@app.route("/services")
def services():
    # Query your MenuService database model to fetch menu items
    menu_items = MenuService.query.all()
    # Render the HTML template with menu_items
    return render_template("services.html", menu_items=menu_items)


# COMPLETED
@app.route("/discussion")
def discussion():
    # return all posts from newest to oldest
    posts = DiscussionBoard.query.order_by(desc(DiscussionBoard.timestamp)).all()
    return render_template("discussion.html", posts=posts)


# COMPLETED
@app.route("/discussion/new_post", methods=["GET", "POST"])
@login_required
def create_new_post():
    form = CreatePosts(request.form)

    if form.validate_on_submit() and request.method == "POST":
        # getting current time
        current_time = datetime.now()

        # creating post in the db
        post = DiscussionBoard(
            title=form.title.data,
            content=form.content.data,
            user_email=current_user.user_email,
            timestamp=current_time,
        )

        # committing to db
        db.session.add(post)
        db.session.commit()

        # TODO: This message could be displayed if the client wants it in future iterations
        # flash("Your post has been created!", "success") # debug
        return redirect(url_for("discussion"))
    # else:
    #    flash("You must be logged in to create a post.", "danger")
    return render_template("create_post.html", form=form)


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


# COMPLETED
@app.route("/logout")
def logout():
    # store current url in the session
    session["previous_url"] = request.referrer
    session.pop("booking_data", None)

    logout_user()

    # redirect user to previous URL they were on
    previous_url = session.pop("previous_url", None)

    if previous_url:
        return redirect(previous_url)
    else:
        # if there is no previous URL, redirect to the homepage
        return redirect(url_for("home"))


# COMPLETED
@app.route("/account")
@login_required
def account():
    return render_template("account.html")


@app.route("/screening")
def screen():
    seat_plan = Screen.query.filter_by(screen_type="Standard").first()
    seat_plan2 = Screen.query.filter_by(screen_type="Deluxe").first()

    return render_template("screen.html", seat_plan=seat_plan, seat_plan2=seat_plan2)


def process_payment(cardholder_name, card_number, expire, cvc):
    # here, we'd have to build an API request
    # be careful of all the external payment processor security guidelines (i.e., how to send data, etc)
    # the payment processor will return, based on its API, a success or declined response

    # for the sake of this project the result will always be successful

    # TODO: Retrieve all payment data based on booking_id

    # TODO: Do things with external payment processor, get updated status

    # TODO: Updated payment status based on result

    # TODO: Place booking

    return "success"
