from flask import Flask, render_template
from forms import Checkout, Payment

app = Flask(__name__)

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
    return render_template('login.html')

@app.route("/tickets")
def tickets():
    return render_template('bookings.html')

@app.route("/checkout")
def checkout():
    return render_template('checkout.html')

@app.route("/payment")
def payment():
    return render_template('payment.html')

@app.route("/discussion")
def discussion():
    return render_template('discussion.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/screens")
def screens():
    return render_template('screens.html')

if __name__ == '__main__':
    app.run(debug=True)