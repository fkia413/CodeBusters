from flask import render_template, url_for, flash, redirect
from application import app, db, bcrypt, login_manager
from flask_login import login_user, current_user, logout_user, login_required


from application.modules.form import (
    Login,
    Registration,
    Checkout,
    Payment,
    Search,
    BookingForm,
    CreatePosts,
    
)

from application.modules.models import User, Movie, Booking,DiscussionBoard
import re



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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
        return redirect(url_for('home'))
    
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


@app.context_processor
def tickets():
    form = Booking()
    return dict(form=form)


@app.route("/booking", methods=["GET", "POST"])
def booking():
    form = BookingForm()
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
            concession=concession,
        )

        db.session.add(booking)
        db.session.commit()

        flash("Booking Successful!", "success")
        return redirect(url_for("paymment"))

    return render_template("booking.html", form=form)


@app.route("/checkout")
def checkout():
    form = Checkout()
    return render_template("checkout.html", form=form)


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
        post = DiscussionBoard(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Your post has been created!", "success")
        return redirect(url_for("discussion"))
    return render_template("create_post.html", title="New Post", form=form)


# passign stuff to navbar


@app.context_processor
def nav():
    form = Search()
    return dict(form=form)


# create search function
@app.route("/search", methods=["POST"])
def search():
    form = Search()
    if form.validate_on_submit():
        # movie.searched = form.searched.data[(movie.id, movie.title) for movie in Movie.query.all()]
        return render_template("search.html", form=form)  # searched = movie.searched

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/account")
@login_required
def account():
    return render_template("account.html", title = account)