from flask import Flask, render_template, url_for
from form import Checkout, Payment, Registration, Login, Search

app = Flask(__name__)
app.config['SECRET_KEY'] = 'efa1dc43ee625d0d91fcb61337ef61c5'
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

@app.route("/login")
def login():
    form = Login()
    return render_template('login.html', form = form)
@app.route("/Register")
def register():
    form = Registration()
    return render_template('register.html', form = form)

@app.route("/booking")
def booking():
    return render_template('booking.html')

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

#passign stuff to navbar

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


if __name__ == '__main__':
    app.run(debug=True)