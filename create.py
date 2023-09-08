from application import app, db
from application.modules.models import *
from datetime import datetime

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create users
    user1 = User(
        user_email="user1@example.com",
        username="user1",
        first_name="John",
        last_name="Doe",
        hash="hashed_password",
    )
    user2 = User(
        user_email="test2@wow.com",
        username="user2",
        first_name="Jane",
        last_name="Smith",
        hash="hashed_password",
    )

    # Create classifications
    classification_u = Classification(
        name="U",
        icon_path="/path/to/icon1.jpg",
        rules_and_conditions="'Universal'; suitable for everyone.",
    )
   
    classification_pg = Classification(
        name="PG",
        icon_path="/path/to/icon6.jpg",
        rules_and_conditions="'Parental Guidance'.",
    )
    
    classification_12a = Classification(
        name="12A",
        icon_path="/path/to/icon12.jpg",
        rules_and_conditions="Suitable for 12 years and over, unless accompanied by an adult.",
    )

    classification_15 = Classification(
        name="15",
        icon_path="/path/to/icon7.jpg",
        rules_and_conditions="Suitable only for 15 years and over.",
    )

    classification_18 = Classification(
        name="18",
        icon_path="/path/to/icon8.jpg",
        rules_and_conditions="Suitable only for adults.",
    )


    # Create genres
    genre1 = Genre(name="Action")
    genre2 = Genre(name="Comedy")

    # Create movies
    movie1 = Movie(
        title="Movie 1",
        release_date=datetime(2023, 9, 10, 16, 0, 0),
        poster_path="/path/to/poster1.jpg",
        status="Released",
        classification=classification1,
    )
    movie2 = Movie(
        title="Movie 2",
        release_date=datetime(2023, 9, 10, 16, 0, 0),
        poster_path="/path/to/poster2.jpg",
        status="Released",
        classification=classification2,
    )

    # Create movie genres
    movie_genre1 = MovieGenre(genre=genre1, movie=movie1)
    movie_genre2 = MovieGenre(genre=genre2, movie=movie2)

    # Create bookings
    booking1 = Booking(
        movie=movie1,
        screening_time=datetime(2023, 9, 10, 16, 0, 0),
        n_seats=2,
        user=user1,
        ticket_type="Standard",
        concession=False,
    )

    booking2 = Booking(
        movie=movie2,
        screening_time=datetime(2023, 9, 10, 16, 0, 0),
        n_seats=3,
        user=user2,
        ticket_type="Deluxe",
        concession=True,
    )

    # Create payments
    payment1 = Payment(
        booking=booking1,
        timestamp=datetime(2023, 9, 10, 16, 0, 0),
        card_holder_name="John Doe",
        card_number="************1234",
        expiry_date="12/25",
        security_code="123",
        amount=25.0,
        status="Successful",
    )
    payment2 = Payment(
        booking=booking2,
        timestamp=datetime(2023, 9, 10, 16, 0, 0),
        card_holder_name="Jane Smith",
        card_number="************5678",
        expiry_date="12/24",
        security_code="456",
        amount=30.0,
        status="Successful",
    )

    # Create menu services
    menu_service1 = MenuService(
        name="Popcorn",
        type="Snack",
        price=5.0,
        image_path="/path/to/popcorn.jpg",
    )
    menu_service2 = MenuService(
        name="Soda", type="Drink", price=3.0, image_path="/path/to/soda.jpg"
    )

    # Create discussion board posts
    post1 = DiscussionBoard(
        user=user1,
        content="This is a discussion post by John Doe.",
        timestamp=datetime(2023, 9, 10, 16, 0, 0),
    )
    post2 = DiscussionBoard(
        user=user2,
        content="This is a discussion post by Jane Smith.",
        timestamp=datetime(2023, 9, 10, 16, 0, 0),
    )

    # Create casts
    cast1 = Cast(
        first_name="Actor1",
        last_name="LastName1",
        gender="Male",
        role="Actor",
    )
    cast2 = Cast(
        first_name="Actor2",
        last_name="LastName2",
        gender="Female",
        role="Actor",
    )

    # Create movie casts
    movie_cast1 = MovieCast(cast=cast1, movie=movie1)
    movie_cast2 = MovieCast(cast=cast2, movie=movie2)

    # Create screens
    screen1 = Screen(
        screen_number=1,
        screen_type="Standard",
        capacity=100,
        seating_plan_img_path="/path/to/seating_plan1.jpg",
    )
    screen2 = Screen(
        screen_number=2,
        screen_type="VIP",
        capacity=50,
        seating_plan_img_path="/path/to/seating_plan2.jpg",
    )

    movie_screen1 = MovieScreen(
        screen=screen1,
        movie=movie1,
        showing_time=datetime(
            2023, 9, 10, 14, 0, 0
        ),  # Use datetime to specify the showing_time
    )
    movie_screen2 = MovieScreen(
        screen=screen1,
        movie=movie2,
        showing_time=datetime(
            2023, 9, 10, 16, 0, 0
        ),  # Use datetime to specify the showing_time
    )

    # Add records to the session
    db.session.add_all(
        [
            user1,
            user2,
            classification1,
            classification2,
            genre1,
            genre2,
            movie_genre1,
            movie_genre2,
            movie1,
            movie2,
            booking1,
            booking2,
            payment1,
            payment2,
            menu_service1,
            menu_service2,
            post1,
            post2,
            cast1,
            cast2,
            movie_cast1,
            movie_cast2,
            screen1,
            screen2,
            movie_screen1,
            movie_screen2,
        ]
    )

    # Commit the changes to the database
    db.session.commit()
