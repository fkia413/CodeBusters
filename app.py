from flask import Flask, render_template
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

@app.route("/cart")
def cart():
    return render_template('cart.html')

@app.route("/checkout")
def checkout():
    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)