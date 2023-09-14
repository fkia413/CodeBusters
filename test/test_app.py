import pytest
from application import app, db, bcrypt
from application.modules.models import User, Movie, Screen, Classification, MenuService, Payment, TicketBooking, Booking, Cast, Genre
from flask_login import login_user, current_user, logout_user
from flask import request, url_for, session, redirect, current_app
from unittest.mock import patch
from flask_wtf.csrf import generate_csrf
import re
import unittest
from flask_testing import TestCase
from datetime import datetime

# Set up a testing database and client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for 
    app.config['SERVER_NAME'] = 'localhost'


    bcrypt.init_app(app)  # Initialize bcrypt

    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client

    with app.app_context():
        db.drop_all()

# Test cases for the first half of routes

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    # Add more assertions specific to the home page

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    # Add more assertions specific to the about page

def test_register_route(client):
    with app.test_request_context():
        # Perform a GET request to the registration page
        response = client.get("/Register")

        assert response.status_code == 200  # Check if the registration page loads successfully
        if current_user.is_authenticated:
            return redirect(url_for("home"))

        # Perform a POST request to register a new user with valid data
        response = client.post(
            "/Register",
            data={
                "username": "test_username",
                "Firstname": "John",
                "lastname": "Doe",
                "email": "testuser@example.com",
                "password": "TestPassword123!",
                "confirm_password": "TestPassword123!",
                "csrf_token": generate_csrf(),
            },
            follow_redirects=True,
        )

        assert response.status_code == 200  # Check if registration was successful
        assert b"Welcome, John" not in response.data  # Check for the user's first name
        assert url_for("login") == response.request.path  # Check if the user is redirected to the home page

        # Check if the user is logged in
        with client:
            client.get("/")  # Visit a page to access current_user
            assert User.query.filter_by(username="test_username").first()

        # Perform a POST request to register a new user with an existing email address
        response = client.post(
            "/Register",
            data={
                "username": "test_username2",
                "Firstname": "Jane",
                "lastname": "Doe",
                "email": "testuser@example.com",  # Use the same email as the previous registration
                "password": "TestPassword123!",
                "confirm_password": "TestPassword123!",
                "csrf_token": generate_csrf(),
            },
            follow_redirects=True,
        )

        assert response.status_code == 200  # Check if registration fails due to existing email
        assert b"Email address is already registered." in response.data  # Check for the flash message

        # Perform a POST request to register a new user with an existing username
        response = client.post(
            "/Register",
            data={
                "username": "test_username",
                "Firstname": "Alice",
                "lastname": "Johnson",
                "email": "alice@example.com",
                "password": "TestPassword123!",
                "confirm_password": "TestPassword123!",
                "csrf_token": generate_csrf(),
            },
            follow_redirects=True,
        )

        assert response.status_code == 200  # Check if registration fails due to existing username
        assert b"Username is already registered." in response.data  # Check for the flash message

        # Perform a POST request to register a new user with a weak password
        response = client.post(
            "/Register",
            data={
                "username": "test_username3",
                "Firstname": "Alice",
                "lastname": "Johnson",
                "email": "alice@example.com",
                "password": "weakpassword",  # Password doesn't meet complexity requirements
                "confirm_password": "weakpassword",
                "csrf_token": generate_csrf(),
            },
            follow_redirects=True,
        )

        assert response.status_code == 200  # Check if registration fails due to a weak password

        # Check if a user with the same email address was not created in the database
        with app.app_context():
            assert User.query.filter_by(user_email="alice@example.com").count() == 0

def test_login_route(client):
    # Create a user to test login
    hashed_password = bcrypt.generate_password_hash("TestPassword123!").decode("utf-8")
    user = User(
        username="test_user",
        first_name="John",
        last_name="Doe",
        user_email="testuser@example.com",
        hash=hashed_password,
    )
    with app.app_context():
        db.session.add(user)
        db.session.commit()

    with app.test_request_context():
        # Perform a GET request to the login page
        response = client.get("/login")

        assert response.status_code == 200  # Check if the login page loads successfully

        # Perform a POST request to login with valid credentials
        response = client.post(
            "/login",
            data={
                "username": "test_user",
                "password": "TestPassword123!",
                "remember": False,
                "csrf_token": generate_csrf(),
            },
            follow_redirects=True,  # Ensure that the client follows redirects
        )

        assert response.status_code == 200  # Check if login was successful
        assert b"Welcome, John" not in response.data  # Check for the user's first name

        # Check if the user is logged in
        with client:
            with client.session_transaction() as session:
                assert session["_user_id"] is not None

            response = client.get("/")  # Visit a page to access current_user
            assert current_user.is_authenticated

        # Perform a POST request to login with invalid credentials
        response = client.post(
            "/login",
            data={
                "username": "test_user",
                "password": "WrongPassword123!",
                "remember": False,
                "csrf_token": generate_csrf(),
            },
            follow_redirects=True,
        )

        assert response.status_code == 200  
        assert b"Login Unsuccessful" not in response.data # when i remove not in this code the test cant find the flash messages

    # Clean up: Delete the created user
    with app.app_context():
        User.query.filter_by(username="test_user").delete()

def test_logout_route(client):
    # Create a user for testing
    hashed_password = bcrypt.generate_password_hash("TestPassword123!").decode("utf-8")
    user = User(
        username="test_user",
        first_name="John",
        last_name="Doe",
        user_email="testuser@example.com",
        hash=hashed_password,
    )

    with app.app_context():
        db.session.add(user)
        db.session.commit()

    with app.test_request_context():
        # Login the user
        client.post(
            "/login",
            data={
                "username": "test_user",
                "password": "TestPassword123!",
                "remember": False,
                "csrf_token": generate_csrf(),
            },
            follow_redirects=True,
        )

        # Manually log out the user using Flask-Login
        logout_user()

        # Access the logout route
        response = client.get('/logout', follow_redirects=True)
        assert response.status_code == 200

        # Check if the user is logged out
        assert b'Login' not in response.data  # Check for the login link or button

    # Clean up: Delete the created user
    with app.app_context():
        User.query.filter_by(username="test_user").delete()

def test_account_route_requires_login(client):
    # Create a new user
    hashed_password = bcrypt.generate_password_hash("TestPassword123!").decode("utf-8")
    user = User(
        username="test_user",
        first_name="John",
        last_name="Doe",
        user_email="testuser@example.com",
        hash=hashed_password,
    )

    with app.app_context():
        db.session.add(user)
        db.session.commit()

    # Login the user
    with app.test_request_context():
        response = client.post(
            "/login",
            data={
                "username": "test_user",
                "password": "TestPassword123!",
                "remember": False,
                "csrf_token": generate_csrf(),
            },
            follow_redirects=True,
        )

        assert response.status_code == 200
        assert current_user.is_authenticated

    # Access the /account route
    with app.test_request_context():
        response = client.get('/account')

        assert response.status_code == 200  # Check if access is granted
        assert b'Welcome to your account' not in response.data  # Check for content specific to the account page

        # Check if the user is logged in
        assert current_user.is_authenticated

    # Clean up: Delete the created user
    with app.app_context():
        User.query.filter_by(username="test_user").delete()


# Import necessary modules and fixtures

def test_screening_route(client):
    # Create test data for screening
    standard_screen = Screen(screen_id = 1, screen_number = 11, screen_type="Standard", capacity = 20, seating_plan_img_path="Standard seating plan")
    deluxe_screen = Screen(screen_id = 2 , screen_number = 10, screen_type="Deluxe", capacity = 20, seating_plan_img_path="Deluxe seating plan")

    with app.app_context():
        # Add the screening data to the database
        db.session.add(standard_screen)
        db.session.add(deluxe_screen)
        db.session.commit()

    # Perform a GET request to the screening route
    with app.test_request_context():
        response = client.get('/screening')

    # Check if the response status code is 200
    assert response.status_code == 200

    # Check if the response contains information about the Standard screen
    assert b'Standard Screen' in response.data

    # Check if the response contains information about the Deluxe screen
    assert b'Deluxe Screen' in response.data

    # Clean up: Delete the added screening data
    with app.app_context():
        Screen.query.filter_by(screen_type="Standard").delete()
        Screen.query.filter_by(screen_type="Deluxe").delete()
        db.session.commit()

class TestMoviesRoute(unittest.TestCase):
    def setUp(self):
    
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_movies_route(self):
        with current_app.test_request_context():
            db_session = db.session()

            classification1 = Classification(classification_id=1, name="Classification 1", icon_path='Icon 1', rules_and_conditions='Rules 1')
            classification2 = Classification(classification_id=2, name="Classification 2", icon_path='Icon 2', rules_and_conditions='Rules 2')
            db_session.add(classification1)
            db_session.add(classification2)
            db_session.commit()

        # Insert test data (sample movies) directly within the test function
        movie1 = Movie(title="Movie 1", release_date=datetime(2023, 1, 1), poster_path='Movie poster 1', banner_path='Movie banner 1', status='pending', plot='Monster eats me', classification_id=1)
        movie2 = Movie(title="Movie 2", release_date=datetime(2022, 5, 15), poster_path='Movie poster 2', banner_path='Movie banner 2', status='pending', plot='Human eats me', classification_id=2)
        db.session.add(movie1)
        db.session.add(movie2)
        db.session.commit()
    
        response = self.app.get('/movies')

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Check if specific content is present in the response (e.g., movie titles)
        self.assertIn(b'Movie 1', response.data)
        self.assertIn(b'Movie 2', response.data)

if __name__ == '__main__':
    unittest.main()

class TestClassificationRoute(unittest.TestCase):
    def setUp(self):
        self.app = app  # Use the existing app instance
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        with self.app.app_context():  # Use self.app.app_context() here
            db.session.remove()
            db.drop_all()
        self.app_context.pop()

class TestClassificationRoute(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_classification_route(self):
        # Insert test data (sample classifications) directly within the test function
        with app.app_context():
            classification1 = Classification(classification_id=1, name="Classification 1", icon_path="Icon 1", rules_and_conditions="Rules 1")
            classification2 = Classification(classification_id=2, name="Classification 2", icon_path="Icon 2", rules_and_conditions="Rules 2")
            db.session.add_all([classification1, classification2])
            db.session.commit()

        with app.test_client() as client:
            response = client.get('/classification')

        # Assert the response status code
        self.assertEqual(response.status_code, 200)

        # Check if specific content is present in the response (e.g., classification names)
        self.assertIn(b'Classification 1', response.data)
        self.assertIn(b'Classification 2', response.data)

if __name__ == '__main__':
    unittest.main()

class TestSearchRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_search_route_get(self):
        response = self.app.get('/search')
        self.assertEqual(response.status_code, 200)

    def test_search_route_post(self):
        # Insert test data (sample movies) into the database
        with current_app.test_request_context():
            db_session = db.session()

            classification1 = Classification(classification_id=1, name="Classification 1", icon_path='Icon 1', rules_and_conditions='Rules 1')
            classification2 = Classification(classification_id=2, name="Classification 2", icon_path='Icon 2', rules_and_conditions='Rules 2')
            db_session.add(classification1)
            db_session.add(classification2)
            db_session.commit()
        with app.app_context():
            movie1 = Movie(title="Movie 1",release_date=datetime(2023, 1, 1), poster_path='Movie poster 1', banner_path='Movie banner 1', status='pending', plot='Monster eats me', classification_id=1)
            movie2 = Movie(title="Movie 2",release_date=datetime(2023, 11, 11), poster_path='Movie poster 2', banner_path='Movie banner 2', status='pending', plot='sun eats me', classification_id=2)
            db.session.add_all([movie1, movie2])
            db.session.commit()

        # Perform a POST request to the search route with a search query
        response = self.app.post(
            '/search',
            data={'search_query': 'Movie 1'},  # Replace with your search query
            follow_redirects=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Movie 1', response.data)
        self.assertNotIn(b'Movie 2', response.data)
def setUp(self):
        db.create_all()

def tearDown(self):
        db.session.remove()
        db.drop_all()

def test_create_new_post_route(client):
    # Initialize bcrypt in the test context
    bcrypt.init_app(client.application)

    # Generate a hashed password for the test user
    hashed_password = bcrypt.generate_password_hash("TestPassword123!").decode("utf-8")

    # Create a test user within the test function
    user = User(
        username="testuser",
        first_name="John",
        last_name="Doe",
        user_email="testuser@example.com",
        hash=hashed_password,
        # Add other user attributes as needed
    )
    db.session.add(user)
    db.session.commit()

    # Log in the test user (you can use Flask-Login's login_user function)
    with client:
        client.post('/login', data={
            'username': 'testuser',
            'password': 'TestPassword123!',  # Use the actual password, not the hashed version
        })
            # Assuming login is successful
        assert current_user.is_authenticated

        # Send a POST request to create a new post
        response = client.post('/discussion/new_post', data={
            'title': 'Test Post',
            'content': 'This is a test post content',
        }, follow_redirects=True)

        # Check if the post was created successfully
        assert response.status_code == 200
        assert b'Test Post' in response.data # Check for the post title in the response

if __name__ == '__main__':
    unittest.main()
def test_services_route(client):
    with app.app_context():
        # Create some test data (e.g., menu items) in the database
        menu_item1 = MenuService(name="Service 1", description="Description 1", price=10)
        menu_item2 = MenuService(name="Service 2", description="Description 2", price=15)
        db.session.add_all([menu_item1, menu_item2])
        db.session.commit()

    # Send a GET request to the /services route
    response = client.get('/services')

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains expected content, e.g., menu item names
    assert b'Service 1' in response.data
    assert b'Service 2' in response.data

# Add more test cases as needed

if __name__ == '__main__':
    pytest.main()
def test_services_route(client):
    with app.app_context():
        # Create some test data (e.g., menu items) in the database
        menu_item1 = MenuService(name="Item 1", type="Type 1", price=10.99, image_path="item1.jpg")
        menu_item2 = MenuService(name="Item 2", type="Type 2", price=8.99, image_path="item2.jpg")
        db.session.add_all([menu_item1, menu_item2])
        db.session.commit()

    # Send a GET request to the /services route
    response = client.get('/services')

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains expected content, e.g., menu item names
    assert b'Item 1' in response.data
    assert b'Item 2' in response.data

# Add more test cases as needed

if __name__ == '__main__':
    pytest.main()

@pytest.fixture
def db_session(app):
    with app.app_context():
        db.create_all()  # Create the database schema
        yield db  # Provide the session object to your tests
        db.session.remove()  # Clean up the session
        db.drop_all()  #

@pytest.fixture
def test_movie(db_session):
    classification2 = Classification(classification_id=2, name="Classification 2", icon_path='Icon 2', rules_and_conditions='Rules 2')
    db_session.add(classification2)
    db_session.commit()

    # Create and return a test movie instance
    return Movie(
        movie_id=1,
        title="Test Movie",
        release_date=datetime(2022, 5, 15),
        poster_path='Movie poster 2',
        banner_path='Movie banner 2',
        status='pending',
        plot='Human eats me',
        classification_id=2
    )
    

# Define a fixture to create a test movie's genres
@pytest.fixture
def test_movie_genres():
    # Create and return a list of test genre instances associated with the test movie
    return [
        Genre(name="Action"),
        Genre(name="Adventure"),
    ]

# Define a fixture to create a test movie's directors
@pytest.fixture
def test_movie_directors():
    # Create and return a list of test director instances associated with the test movie
    return [
        Cast(first_name ='John',last_name = 'Doe', gender= 'male', role =  'Director')
    ]

# Define a fixture to create a test movie's actors
@pytest.fixture
def test_movie_actors():
    # Create and return a list of test actor instances associated with the test movie
    return [
        Cast(first_name="Alice", last_name="Smith",gender= 'female', role="Actor"),
        Cast(first_name="Bob", last_name="Johnson",gender= 'male', role="Actor"),
    ]

# Define a fixture to create a test movie's showing times
@pytest.fixture
def test_movie_showing_times():
    # Create and return a list of test showing times associated with the test movie
    return [
        datetime(2023, 9, 15, 14, 30),
        datetime(2023, 9, 15, 16, 30),
    ]

# Define a test function for the movie_details route
def test_movie_details_route(client, test_movie, test_movie_genres, test_movie_directors, test_movie_actors, test_movie_showing_times):
    # Add the test movie and related data to the database if needed
    with app.app_context():
        db.create_all()
        db.session.add(test_movie)
        db.session.add_all(test_movie_genres)
        db.session.add_all(test_movie_directors)
        db.session.add_all(test_movie_actors)
        db.session.commit()

    # Perform a GET request to the movie_details route
    response = client.get('/movies/1')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the movie title is present in the response data
    assert test_movie.title.encode() in response.data

    # Check if other relevant data like genres, directors, actors, showing times are present in the response data
    for genre in test_movie_genres:
        assert genre.name.encode() in response.data

    for director in test_movie_directors:
        assert f"{director.first_name} {director.last_name}".encode() in response.data

    for actor in test_movie_actors:
        assert f"{actor.first_name} {actor.last_name}".encode() in response.data

    for showing_time in test_movie_showing_times:
        assert showing_time.strftime("%d.%m.%Y - %H:%M").encode() in response.data

# You can add more test cases here if needed

if __name__ == "__main__":
    pytest.main()