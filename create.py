from application import app, db
from application.modules.models import *
from datetime import datetime

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create classifications
    classification_u = Classification(
        name="U",
        icon_path="classification_u_icon.jpg",
        rules_and_conditions="Universal: suitable for everyone.",
    )
    db.session.add(classification_u)

    classification_pg = Classification(
        name="PG",
        icon_path="classification_pg_icon.jpg",
        rules_and_conditions="Parental Guidance.",
    )
    db.session.add(classification_pg)

    classification_12a = Classification(
        name="12A",
        icon_path="classification_12a_icon.jpg",
        rules_and_conditions="Suitable for 12 years and over, unless accompanied by an adult.",
    )
    db.session.add(classification_12a)

    classification_15 = Classification(
        name="15",
        icon_path="classification_15_icon.jpg",
        rules_and_conditions="Suitable only for 15 years and over.",
    )
    db.session.add(classification_15)

    classification_18 = Classification(
        name="18",
        icon_path="classification_18_icon.jpg",
        rules_and_conditions="Suitable only for adults.",
    )
    db.session.add(classification_18)

    # Create genres
    action_genre = Genre(name="Action")
    db.session.add(action_genre)

    comedy_genre = Genre(name="Comedy")
    db.session.add(comedy_genre)

    adventure_genre = Genre(name="Adventure")
    db.session.add(adventure_genre)

    fantasy_genre = Genre(name="Fantasy")
    db.session.add(fantasy_genre)

    horror_genre = Genre(name="Horror")
    db.session.add(horror_genre)

    thriller_genre = Genre(name="Thriller")
    db.session.add(thriller_genre)

    scifi_genre = Genre(name="Sci-fi")
    db.session.add(scifi_genre)

    romance_genre = Genre(name="Romance")
    db.session.add(romance_genre)

    drama_genre = Genre(name="Drama")
    db.session.add(drama_genre)

    musical_genre = Genre(name="Musical")
    db.session.add(musical_genre)

    family_genre = Genre(name="Family")
    db.session.add(family_genre)

    # Create directors
    greta_gerwig = Cast(
        first_name="Greta",
        last_name="Gerwig",
        gender="Female",
        role="Director",
    )
    db.session.add(greta_gerwig)

    angel_soto = Cast(
        first_name="Angel",
        last_name="Soto",
        gender="Male",
        role="Director",
    )
    db.session.add(angel_soto)

    danny_philippou = Cast(
        first_name="Danny",
        last_name="Philippou",
        gender="Male",
        role="Director",
    )
    db.session.add(danny_philippou)

    michael_philippou = Cast(
        first_name="Michael",
        last_name="Philippou",
        gender="Male",
        role="Director",
    )
    db.session.add(michael_philippou)

    ben_wheatley = Cast(
        first_name="Ben",
        last_name="Wheatley",
        gender="Male",
        role="Director",
    )
    db.session.add(ben_wheatley)

    rob_minkoff = Cast(
        first_name="Rob",
        last_name="Minkoff",
        gender="Male",
        role="Director",
    )
    db.session.add(rob_minkoff)

    roger_allers = Cast(
        first_name="Roger",
        last_name="Allers",
        gender="Male",
        role="Director",
    )
    db.session.add(roger_allers)

    josh_boone = Cast(
        first_name="Josh",
        last_name="Boone",
        gender="Male",
        role="Director",
    )
    db.session.add(josh_boone)

    andres_muschietti = Cast(
        first_name="Andres",
        last_name="Muschietti",
        gender="Male",
        role="Director",
    )
    db.session.add(andres_muschietti)

    christopher_nolan = Cast(
        first_name="Christopher",
        last_name="Nolan",
        gender="Male",
        role="Director",
    )
    db.session.add(christopher_nolan)

    ron_clements = Cast(
        first_name="Ron",
        last_name="Clements",
        gender="Male",
        role="Director",
    )
    db.session.add(ron_clements)

    john_musker = Cast(
        first_name="John",
        last_name="Musker",
        gender="Male",
        role="Director",
    )
    db.session.add(john_musker)

    # creating actors
    margot_robbie = Cast(
        first_name="Margot",
        last_name="Robbie",
        gender="Female",
        role="Actor",
    )
    db.session.add(margot_robbie)

    ryan_gosling = Cast(
        first_name="Ryan",
        last_name="Gosling",
        gender="Male",
        role="Actor",
    )
    db.session.add(ryan_gosling)

    issa_rae = Cast(
        first_name="Issa",
        last_name="Rae",
        gender="Female",
        role="Actor",
    )
    db.session.add(issa_rae)

    bruna_marquezine = Cast(
        first_name="Bruna",
        last_name="Marquezine",
        gender="Female",
        role="Actor",
    )
    db.session.add(bruna_marquezine)

    xolo_mariduena = Cast(
        first_name="Xolo",
        last_name="Mariduena",
        gender="Female",
        role="Actor",
    )
    db.session.add(xolo_mariduena)

    george_lopez = Cast(
        first_name="George",
        last_name="Lopez",
        gender="Male",
        role="Actor",
    )
    db.session.add(george_lopez)

    zoe_terakes = Cast(
        first_name="Zoe",
        last_name="Terakes",
        gender="Female",
        role="Actor",
    )
    db.session.add(zoe_terakes)

    sophie_wilde = Cast(
        first_name="Sophie",
        last_name="Wilde",
        gender="Female",
        role="Actor",
    )
    db.session.add(sophie_wilde)

    miranda_otto = Cast(
        first_name="Miranda",
        last_name="Otto",
        gender="Female",
        role="Actor",
    )
    db.session.add(miranda_otto)

    leonardo_dicaprio = Cast(
        first_name="Leonardo",
        last_name="DiCaprio",
        gender="Male",
        role="Actor",
    )
    db.session.add(leonardo_dicaprio)

    cillian_murphy = Cast(
        first_name="Cillian",
        last_name="Murphy",
        gender="Male",
        role="Actor",
    )
    db.session.add(cillian_murphy)

    joseph_gordon = Cast(
        first_name="Joseph",
        last_name="Gordon",
        gender="Male",
        role="Actor",
    )
    db.session.add(joseph_gordon)

    bill_skarsgard = Cast(
        first_name="Bill",
        last_name="Skarsgard",
        gender="Male",
        role="Actor",
    )
    db.session.add(bill_skarsgard)

    jaeden_martell = Cast(
        first_name="Jaeden",
        last_name="Martell",
        gender="Female",
        role="Actor",
    )
    db.session.add(jaeden_martell)

    finn_wolfhard = Cast(
        first_name="Finn",
        last_name="Wolfhard",
        gender="Male",
        role="Actor",
    )
    db.session.add(finn_wolfhard)

    shailene_woodley = Cast(
        first_name="Shailene",
        last_name="Woodley",
        gender="Female",
        role="Actor",
    )
    db.session.add(shailene_woodley)

    ansel_elgort = Cast(
        first_name="Ansel",
        last_name="Elgort",
        gender="Female",
        role="Actor",
    )
    db.session.add(ansel_elgort)

    john_green = Cast(
        first_name="John",
        last_name="Green",
        gender="Male",
        role="Actor",
    )
    db.session.add(john_green)

    jeremy_irons = Cast(
        first_name="Jeremy",
        last_name="Irons",
        gender="Male",
        role="Actor",
    )
    db.session.add(jeremy_irons)

    james_jones = Cast(
        first_name="James",
        last_name="Jones",
        gender="Male",
        role="Actor",
    )
    db.session.add(james_jones)

    matthew_broderick = Cast(
        first_name="Matthew",
        last_name="Broderick",
        gender="Male",
        role="Actor",
    )
    db.session.add(matthew_broderick)

    jason_statham = Cast(
        first_name="Jason",
        last_name="Statham",
        gender="Male",
        role="Actor",
    )
    db.session.add(jason_statham)

    li_bingbing = Cast(
        first_name="Li",
        last_name="Bingbing",
        gender="Female",
        role="Actor",
    )
    db.session.add(li_bingbing)

    shuya_cai = Cast(
        first_name="Shuya",
        last_name="Cai",
        gender="Female",
        role="Actor",
    )
    db.session.add(shuya_cai)

    halle_bailey = Cast(
        first_name="Halle",
        last_name="Bailey",
        gender="Female",
        role="Actor",
    )
    db.session.add(halle_bailey)

    jonah_hauer_king = Cast(
        first_name="Jonah",
        last_name="Hauer-King",
        gender="Male",
        role="Actor",
    )
    db.session.add(jonah_hauer_king)

    javier_bardem = Cast(
        first_name="Javier",
        last_name="Bardem",
        gender="Male",
        role="Actor",
    )
    db.session.add(javier_bardem)

    # Create screens
    standard_screen_1 = Screen(
        screen_number=1,
        screen_type="Standard",
        capacity=100,
        seating_plan_img_path="standard_seating_plan.jpg",
    )
    db.session.add(standard_screen_1)

    standard_screen_2 = Screen(
        screen_number=2,
        screen_type="Standard",
        capacity=100,
        seating_plan_img_path="standard_seating_plan.jpg",
    )
    db.session.add(standard_screen_2)

    deluxe_screen_1 = Screen(
        screen_number=11,
        screen_type="Deluxe",
        capacity=50,
        seating_plan_img_path="deluxe_seating_plan.jpg",
    )
    db.session.add(deluxe_screen_1)

    deluxe_screen_2 = Screen(
        screen_number=12,
        screen_type="Deluxe",
        capacity=50,
        seating_plan_img_path="deluxe_seating_plan.jpg",
    )
    db.session.add(deluxe_screen_2)

    # Create movies
    # according to the project brief, we need 4 brand new releases
    # and at least 2 older ones
    # I will just do  4 new releases and 5 older ones

    # new movie #1
    # https://deadline.com/wp-content/uploads/2023/04/barbie-BARBIE_VERT_TSR_W_TALENT_2764x4096_DOM_rgb.jpg?w=800
    # https://static.designmynight.com/uploads/2023/06/2023-Barbie-Movie-Events-UK-Experiences-1200x675-optimised.jpg
    barbie_movie = Movie(
        title="Barbie",
        release_date=datetime(2023, 7, 21),
        poster_path="barbie_poster.jpg",
        banner_path="barbie_banner.jpg",
        status="Released",
        classification=classification_12a,
        plot="Barbie and Ken are having the time of their lives in the colorful and seemingly perfect world of Barbie Land. However, when they get a chance to go to the real world, they soon discover the joys and perils of living among humans.",
    )
    db.session.add(barbie_movie)

    # new movie #2
    # https://assets-prd.ignimgs.com/2023/04/03/blbtl-vert-tsr-rev-2764x4096-dom-1680537435203.jpg
    # https://images8.alphacoders.com/132/1329236.jpeg
    blue_beetle_movie = Movie(
        title="Blue Beetle",
        release_date=datetime(2023, 8, 18),
        poster_path="blue_beetle_poster.jpg",
        banner_path="blue_beetle_banner.jpg",
        status="Released",
        classification=classification_12a,
        plot="Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle.",
    )
    db.session.add(blue_beetle_movie)

    # new movie #3
    # https://m.media-amazon.com/images/M/MV5BMTM2NTU1ZTktNjc4YS00NjNhLWE4NmYtOTM2YjFjOGUzNmYzXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_.jpg
    # https://image.tmdb.org/t/p/original/rNoyJmjdhgn30bVbvd8n3DJMocB.jpg
    meg_2_movie = Movie(
        title="Meg 2: The Trench",
        release_date=datetime(2023, 8, 4),
        poster_path="meg_2_poster.jpg",
        banner_path="meg_2_banner.jpg",
        status="Released",
        classification=classification_12a,
        plot="Jonas Taylor leads a research team on an exploratory dive into the deepest depths of the ocean. Their voyage spirals into chaos when a malevolent mining operation threatens their mission and forces them into a high-stakes battle for survival. Pitted against colossal, prehistoric sharks and relentless environmental plunderers, they must outrun, outsmart and outswim their merciless predators.",
    )
    db.session.add(meg_2_movie)

    # new movie #4
    # http://www.impawards.com/2023/posters/little_mermaid_ver6_xlg.jpg
    # https://images.alphacoders.com/131/1310935.jpeg
    the_little_mermaid_movie = Movie(
        title="The Little Mermaid",
        release_date=datetime(2023, 5, 26),
        poster_path="the_little_mermaid_poster.jpg",
        banner_path="the_little_mermaid_banner.jpg",
        status="Released",
        classification=classification_pg,
        plot="The Little Mermaid follows a mermaid princess Ariel who is fascinated with the human world and makes a deal with a treacherous sea witch Ursula to trade her voice for human legs to impress Prince Eric, whom she saved from a shipwreck before time runs out.",
    )
    db.session.add(the_little_mermaid_movie)

    # older movie #1
    # https://m.media-amazon.com/images/M/MV5BZGFjOTRiYjgtYjEzMS00ZjQ2LTkzY2YtOGQ0NDI2NTVjOGFmXkEyXkFqcGdeQXVyNDQ5MDYzMTk@._V1_.jpg
    # https://image.tmdb.org/t/p/original/ii8QGacT3MXESqBckQlyrATY0lT.jpg
    inception_movie = Movie(
        title="Inception",
        release_date=datetime(2010, 7, 8),
        poster_path="inception_poster.jpg",
        banner_path="inception_banner.jpg",
        status="Released",
        classification=classification_12a,
        plot="Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter people's dreams and steal their secrets from their subconscious. His skill has made him a hot commodity in the world of corporate espionage but has also cost him everything he loves. Cobb gets a chance at redemption when he is offered a seemingly impossible task: Plant an idea in someone's mind. If he succeeds, it will be the perfect crime, but a dangerous enemy anticipates Cobb's every move.",
    )
    db.session.add(inception_movie)

    # older movie #2
    # https://i.pinimg.com/originals/bc/5d/c0/bc5dc00b256f89f42a4b5a60aad3db4f.jpg
    # https://m.media-amazon.com/images/M/MV5BMTU5NTY4MjY0M15BMl5BanBnXkFtZTgwODI1NzMzMzI@._V1_.jpg
    it_movie = Movie(
        title="IT",
        release_date=datetime(2017, 9, 8),
        poster_path="it_poster.jpg",
        banner_path="it_banner.jpg",
        status="Released",
        classification=classification_15,
        plot="Seven young outcasts in Derry, Maine, are about to face their worst nightmare -- an ancient, shape-shifting evil that emerges from the sewer every 27 years to prey on the town's children. Banding together over the course of one horrifying summer, the friends must overcome their own personal fears to battle the murderous, bloodthirsty clown known as Pennywise.",
    )
    db.session.add(it_movie)

    # older movie #3
    # https://thegalileo.co.za/wp-content/uploads/2022/09/The-Fault-In-Our-Stars-733x1030.jpg
    # https://ichef.bbci.co.uk/images/ic/1200x675/p0f24hjv.jpg
    the_fault_in_our_stars_movie = Movie(
        title="The Fault In Our Stars",
        release_date=datetime(2014, 6, 19),
        poster_path="the_fault_in_our_stars_poster.jpg",
        banner_path="the_fault_in_our_stars_banner.jpg",
        status="Released",
        classification=classification_12a,
        plot="The Fault in Our Stars by John Green is a young adult fiction novel that narrates the story of a 16-year-old girl who is diagnosed with cancer. She joins a support group where she meets Augustus, and there is a rollercoaster of emotions throughout this novel as the relationship between Hazel and Augustus develops.",
    )
    db.session.add(the_fault_in_our_stars_movie)

    # older movie #4
    # https://m.media-amazon.com/images/M/MV5BYTYxNGMyZTYtMjE3MS00MzNjLWFjNmYtMDk3N2FmM2JiM2M1XkEyXkFqcGdeQXVyNjY5NDU4NzI@._V1_.jpg
    # https://whatson.bfi.org.uk/ArticleMedia/Images/WhatsOn%20images/202308/lion-king-01.jpeg
    the_lion_king_movie = Movie(
        title="The Lion King",
        release_date=datetime(1994, 10, 7),
        poster_path="the_lion_king_poster.jpg",
        banner_path="the_lion_king_banner.jpg",
        status="Released",
        classification=classification_u,
        plot="This Disney animated feature follows the adventures of the young lion Simba (Jonathan Taylor Thomas), the heir of his father, Mufasa (James Earl Jones). Simba's wicked uncle, Scar (Jeremy Irons), plots to usurp Mufasa's throne by luring father and son into a stampede of wildebeests. But Simba escapes, and only Mufasa is killed. Simba returns as an adult (Matthew Broderick) to take back his homeland from Scar with the help of his friends Timon (Nathan Lane) and Pumbaa (Ernie Sabella).",
    )
    db.session.add(the_lion_king_movie)

    # older movie #5
    # http://www.impawards.com/intl/australia/2023/posters/talk_to_me_xlg.jpg
    # https://static1.srcdn.com/wordpress/wp-content/uploads/2023/07/when-will-talk-to-me-release-on-streaming.jpg
    talk_to_me_movie = Movie(
        title="Talk to me",
        release_date=datetime(2022, 7, 28),
        poster_path="talk_to_me_poster.jpg",
        banner_path="talk_to_me_banner.jpg",
        status="Released",
        classification=classification_15,
        plot="When a group of friends discover how to conjure spirits with an embalmed hand, they become hooked on the new thrill and high-stakes party game -- until one of them goes too far and unleashes terrifying supernatural forces.",
    )
    db.session.add(talk_to_me_movie)

    # Create movie genres
    # barbie genres
    barbie_movie_genre_1 = MovieGenre(genre=adventure_genre, movie=barbie_movie)
    db.session.add(barbie_movie_genre_1)
    barbie_movie_genre_2 = MovieGenre(genre=comedy_genre, movie=barbie_movie)
    db.session.add(barbie_movie_genre_2)
    barbie_movie_genre_3 = MovieGenre(genre=fantasy_genre, movie=barbie_movie)
    db.session.add(barbie_movie_genre_3)

    # the little mermaid genres
    the_little_mermaid_movie_genre_1 = MovieGenre(
        genre=romance_genre, movie=the_little_mermaid_movie
    )
    db.session.add(the_little_mermaid_movie_genre_1)
    the_little_mermaid_movie_genre_2 = MovieGenre(
        genre=musical_genre, movie=the_little_mermaid_movie
    )
    db.session.add(the_little_mermaid_movie_genre_2)

    # blue beetle genres
    blue_beetle_movie_genre_1 = MovieGenre(genre=action_genre, movie=blue_beetle_movie)
    db.session.add(blue_beetle_movie_genre_1)
    blue_beetle_movie_genre_2 = MovieGenre(
        genre=adventure_genre, movie=blue_beetle_movie
    )
    db.session.add(blue_beetle_movie_genre_2)

    # talk to me genres
    talk_to_me_movie_genre_1 = MovieGenre(genre=horror_genre, movie=talk_to_me_movie)
    db.session.add(talk_to_me_movie_genre_1)
    talk_to_me_movie_genre_2 = MovieGenre(genre=thriller_genre, movie=talk_to_me_movie)
    db.session.add(talk_to_me_movie_genre_2)

    # inception genres
    inception_movie_genre_1 = MovieGenre(genre=action_genre, movie=inception_movie)
    db.session.add(inception_movie_genre_1)
    inception_movie_genre_2 = MovieGenre(genre=scifi_genre, movie=inception_movie)
    db.session.add(inception_movie_genre_2)

    # it genres
    it_movie_genre_1 = MovieGenre(genre=horror_genre, movie=it_movie)
    db.session.add(it_movie_genre_1)

    # the fault in our stars genres
    the_fault_in_our_stars_movie_genre_1 = MovieGenre(
        genre=romance_genre, movie=the_fault_in_our_stars_movie
    )
    db.session.add(the_fault_in_our_stars_movie_genre_1)
    the_fault_in_our_stars_movie_genre_2 = MovieGenre(
        genre=drama_genre, movie=the_fault_in_our_stars_movie
    )
    db.session.add(the_fault_in_our_stars_movie_genre_2)

    # the lion king genres
    the_lion_king_movie_genre_1 = MovieGenre(
        genre=musical_genre, movie=the_lion_king_movie
    )
    db.session.add(the_lion_king_movie_genre_1)
    the_lion_king_movie_genre_2 = MovieGenre(
        genre=family_genre, movie=the_lion_king_movie
    )
    db.session.add(the_lion_king_movie_genre_2)

    # meg 2 genres
    meg_2_movie_genre_1 = MovieGenre(genre=action_genre, movie=meg_2_movie)
    db.session.add(meg_2_movie_genre_1)
    meg_2_movie_genre_2 = MovieGenre(genre=adventure_genre, movie=meg_2_movie)
    db.session.add(meg_2_movie_genre_2)

    # Create movie casts
    # barbie cast
    barbie_movie_cast_1 = MovieCast(cast=greta_gerwig, movie=barbie_movie)
    db.session.add(barbie_movie_cast_1)
    barbie_movie_cast_2 = MovieCast(cast=margot_robbie, movie=barbie_movie)
    db.session.add(barbie_movie_cast_2)
    barbie_movie_cast_3 = MovieCast(cast=ryan_gosling, movie=barbie_movie)
    db.session.add(barbie_movie_cast_3)
    barbie_movie_cast_4 = MovieCast(cast=issa_rae, movie=barbie_movie)
    db.session.add(barbie_movie_cast_4)

    # the little mermaid cast
    the_little_mermaid_movie_cast_1 = MovieCast(
        cast=john_musker, movie=the_little_mermaid_movie
    )
    db.session.add(the_little_mermaid_movie_cast_1)
    the_little_mermaid_movie_cast_2 = MovieCast(
        cast=ron_clements, movie=the_little_mermaid_movie
    )
    db.session.add(the_little_mermaid_movie_cast_2)
    the_little_mermaid_movie_cast_3 = MovieCast(
        cast=halle_bailey, movie=the_little_mermaid_movie
    )
    db.session.add(the_little_mermaid_movie_cast_3)
    the_little_mermaid_movie_cast_4 = MovieCast(
        cast=jonah_hauer_king, movie=the_little_mermaid_movie
    )
    db.session.add(the_little_mermaid_movie_cast_4)
    the_little_mermaid_movie_cast_5 = MovieCast(
        cast=javier_bardem, movie=the_little_mermaid_movie
    )
    db.session.add(the_little_mermaid_movie_cast_5)

    # blue beetle cast
    blue_beetle_movie_cast_1 = MovieCast(cast=angel_soto, movie=blue_beetle_movie)
    db.session.add(blue_beetle_movie_cast_1)
    blue_beetle_movie_cast_2 = MovieCast(cast=bruna_marquezine, movie=blue_beetle_movie)
    db.session.add(blue_beetle_movie_cast_2)
    blue_beetle_movie_cast_3 = MovieCast(cast=xolo_mariduena, movie=blue_beetle_movie)
    db.session.add(blue_beetle_movie_cast_3)
    blue_beetle_movie_cast_4 = MovieCast(cast=george_lopez, movie=blue_beetle_movie)
    db.session.add(blue_beetle_movie_cast_4)

    # talk to me cast
    talk_to_me_movie_cast_1 = MovieCast(cast=danny_philippou, movie=talk_to_me_movie)
    db.session.add(talk_to_me_movie_cast_1)
    talk_to_me_movie_cast_2 = MovieCast(cast=michael_philippou, movie=talk_to_me_movie)
    db.session.add(talk_to_me_movie_cast_2)
    talk_to_me_movie_cast_3 = MovieCast(cast=zoe_terakes, movie=talk_to_me_movie)
    db.session.add(talk_to_me_movie_cast_3)
    talk_to_me_movie_cast_4 = MovieCast(cast=sophie_wilde, movie=talk_to_me_movie)
    db.session.add(talk_to_me_movie_cast_4)
    talk_to_me_movie_cast_5 = MovieCast(cast=miranda_otto, movie=talk_to_me_movie)
    db.session.add(talk_to_me_movie_cast_5)

    # inception cast
    inception_movie_cast_1 = MovieCast(cast=christopher_nolan, movie=inception_movie)
    db.session.add(inception_movie_cast_1)
    inception_movie_cast_2 = MovieCast(cast=leonardo_dicaprio, movie=inception_movie)
    db.session.add(inception_movie_cast_2)
    inception_movie_cast_3 = MovieCast(cast=cillian_murphy, movie=inception_movie)
    db.session.add(inception_movie_cast_3)
    inception_movie_cast_4 = MovieCast(cast=joseph_gordon, movie=inception_movie)
    db.session.add(inception_movie_cast_4)

    # it cast
    it_movie_cast_1 = MovieCast(cast=andres_muschietti, movie=it_movie)
    db.session.add(it_movie_cast_1)
    it_movie_cast_2 = MovieCast(cast=bill_skarsgard, movie=it_movie)
    db.session.add(it_movie_cast_2)
    it_movie_cast_3 = MovieCast(cast=jaeden_martell, movie=it_movie)
    db.session.add(it_movie_cast_3)
    it_movie_cast_4 = MovieCast(cast=finn_wolfhard, movie=it_movie)
    db.session.add(it_movie_cast_4)

    # the fault in our stars cast
    the_fault_in_our_stars_movie_cast_1 = MovieCast(
        cast=josh_boone, movie=the_fault_in_our_stars_movie
    )
    db.session.add(the_fault_in_our_stars_movie_cast_1)
    the_fault_in_our_stars_movie_cast_2 = MovieCast(
        cast=shailene_woodley, movie=the_fault_in_our_stars_movie
    )
    db.session.add(the_fault_in_our_stars_movie_cast_2)
    the_fault_in_our_stars_movie_cast_3 = MovieCast(
        cast=ansel_elgort, movie=the_fault_in_our_stars_movie
    )
    db.session.add(the_fault_in_our_stars_movie_cast_3)
    the_fault_in_our_stars_movie_cast_4 = MovieCast(
        cast=john_green, movie=the_fault_in_our_stars_movie
    )
    db.session.add(the_fault_in_our_stars_movie_cast_4)

    # the lion king cast
    the_lion_king_movie_cast_1 = MovieCast(cast=rob_minkoff, movie=the_lion_king_movie)
    db.session.add(the_lion_king_movie_cast_1)
    the_lion_king_movie_cast_2 = MovieCast(cast=roger_allers, movie=the_lion_king_movie)
    db.session.add(the_lion_king_movie_cast_2)
    the_lion_king_movie_cast_3 = MovieCast(cast=jeremy_irons, movie=the_lion_king_movie)
    db.session.add(the_lion_king_movie_cast_3)
    the_lion_king_movie_cast_4 = MovieCast(cast=james_jones, movie=the_lion_king_movie)
    db.session.add(the_lion_king_movie_cast_4)
    the_lion_king_movie_cast_5 = MovieCast(
        cast=matthew_broderick, movie=the_lion_king_movie
    )
    db.session.add(the_lion_king_movie_cast_5)

    # meg 2 cast
    meg_2_movie_cast_1 = MovieCast(cast=ben_wheatley, movie=meg_2_movie)
    db.session.add(meg_2_movie_cast_1)
    meg_2_movie_cast_2 = MovieCast(cast=jason_statham, movie=meg_2_movie)
    db.session.add(meg_2_movie_cast_2)
    meg_2_movie_cast_3 = MovieCast(cast=li_bingbing, movie=meg_2_movie)
    db.session.add(meg_2_movie_cast_3)
    meg_2_movie_cast_4 = MovieCast(cast=shuya_cai, movie=meg_2_movie)
    db.session.add(meg_2_movie_cast_4)

    # Creating screening times
    #   - from the 18th to the 24th - these are temporary, just for the mock database
    #   - in future iterations, an admin account would have full control over CRUD operations regarding the screening times
    #   - at the moment, there are only 4 screens
    #   - brand new releases could have more screening times over the entire week
    #   - for development purposes, screening times are only available at the following slots:
    #           - 4pm, 7pm, 10pm

    # screenings:
    #   18th to 24th
    #       - standard screen 1
    #           - the little mermaid 4pm
    #           - barbie 7pm
    #           - blue beetle 10pm
    #       - standard screen 2
    #           - the lion king 4pm
    #           - the fault in our stars 7pm
    #           - IT 10pm
    #       - deluxe screen 1
    #           - the little mermaid 4pm
    #           - inception 7pm
    #           - talk to me 10pm
    #       - deluxe screen 2
    #           - the little mermaid 4pm
    #           - barbie 7pm
    #           - meg 2 10pm

    # standard screen 1 screenings ###############################################
    # 18th - 4pm
    standard_screen_1_screening_18_4 = MovieScreen(
        screen=standard_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 18, 16, 0, 0),
    )
    db.session.add(standard_screen_1_screening_18_4)

    # 18th - 7pm
    standard_screen_1_screening_18_7 = MovieScreen(
        screen=standard_screen_1,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 18, 19, 0, 0),
    )
    db.session.add(standard_screen_1_screening_18_7)

    # 18th - 10pm
    standard_screen_1_screening_18_10 = MovieScreen(
        screen=standard_screen_1,
        movie=blue_beetle_movie,
        showing_time=datetime(2023, 9, 18, 22, 0, 0),
    )
    db.session.add(standard_screen_1_screening_18_10)

    # 19th - 4pm
    standard_screen_1_screening_19_4 = MovieScreen(
        screen=standard_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 19, 16, 0, 0),
    )
    db.session.add(standard_screen_1_screening_19_4)

    # 19th - 7pm
    standard_screen_1_screening_19_7 = MovieScreen(
        screen=standard_screen_1,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 19, 19, 0, 0),
    )
    db.session.add(standard_screen_1_screening_19_7)

    # 19th - 10pm
    standard_screen_1_screening_19_10 = MovieScreen(
        screen=standard_screen_1,
        movie=blue_beetle_movie,
        showing_time=datetime(2023, 9, 19, 22, 0, 0),
    )
    db.session.add(standard_screen_1_screening_19_10)

    # 20th - 4pm
    standard_screen_1_screening_20_4 = MovieScreen(
        screen=standard_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 20, 16, 0, 0),
    )
    db.session.add(standard_screen_1_screening_20_4)

    # 20th - 7pm
    standard_screen_1_screening_20_7 = MovieScreen(
        screen=standard_screen_1,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 20, 19, 0, 0),
    )
    db.session.add(standard_screen_1_screening_20_7)

    # 20th - 10pm
    standard_screen_1_screening_20_10 = MovieScreen(
        screen=standard_screen_1,
        movie=blue_beetle_movie,
        showing_time=datetime(2023, 9, 20, 22, 0, 0),
    )
    db.session.add(standard_screen_1_screening_20_10)

    # 21th - 4pm
    standard_screen_1_screening_21_4 = MovieScreen(
        screen=standard_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 21, 16, 0, 0),
    )
    db.session.add(standard_screen_1_screening_21_4)

    # 21th - 7pm
    standard_screen_1_screening_21_7 = MovieScreen(
        screen=standard_screen_1,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 21, 19, 0, 0),
    )
    db.session.add(standard_screen_1_screening_21_7)

    # 21th - 10pm
    standard_screen_1_screening_21_10 = MovieScreen(
        screen=standard_screen_1,
        movie=blue_beetle_movie,
        showing_time=datetime(2023, 9, 21, 22, 0, 0),
    )
    db.session.add(standard_screen_1_screening_21_10)

    # 22th - 4pm
    standard_screen_1_screening_22_4 = MovieScreen(
        screen=standard_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 22, 16, 0, 0),
    )
    db.session.add(standard_screen_1_screening_22_4)

    # 22th - 7pm
    standard_screen_1_screening_22_7 = MovieScreen(
        screen=standard_screen_1,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 22, 19, 0, 0),
    )
    db.session.add(standard_screen_1_screening_22_7)

    # 22th - 10pm
    standard_screen_1_screening_22_10 = MovieScreen(
        screen=standard_screen_1,
        movie=blue_beetle_movie,
        showing_time=datetime(2023, 9, 22, 22, 0, 0),
    )
    db.session.add(standard_screen_1_screening_22_10)

    # 23th - 4pm
    standard_screen_1_screening_23_4 = MovieScreen(
        screen=standard_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 23, 16, 0, 0),
    )
    db.session.add(standard_screen_1_screening_23_4)

    # 23th - 7pm
    standard_screen_1_screening_23_7 = MovieScreen(
        screen=standard_screen_1,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 23, 19, 0, 0),
    )
    db.session.add(standard_screen_1_screening_23_7)

    # 23th - 10pm
    standard_screen_1_screening_23_10 = MovieScreen(
        screen=standard_screen_1,
        movie=blue_beetle_movie,
        showing_time=datetime(2023, 9, 23, 22, 0, 0),
    )
    db.session.add(standard_screen_1_screening_23_10)

    # 24th - 4pm
    standard_screen_1_screening_24_4 = MovieScreen(
        screen=standard_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 24, 16, 0, 0),
    )
    db.session.add(standard_screen_1_screening_24_4)

    # 24th - 7pm
    standard_screen_1_screening_24_7 = MovieScreen(
        screen=standard_screen_1,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 24, 19, 0, 0),
    )
    db.session.add(standard_screen_1_screening_24_7)

    # 24th - 10pm
    standard_screen_1_screening_24_10 = MovieScreen(
        screen=standard_screen_1,
        movie=blue_beetle_movie,
        showing_time=datetime(2023, 9, 24, 22, 0, 0),
    )
    db.session.add(standard_screen_1_screening_24_10)

    # standard screen 2 screenings ###############################################
    # 18th - 4pm
    standard_screen_2_screening_18_4 = MovieScreen(
        screen=standard_screen_2,
        movie=the_lion_king_movie,
        showing_time=datetime(2023, 9, 18, 16, 0, 0),
    )
    db.session.add(standard_screen_2_screening_18_4)

    # 18th - 7pm
    standard_screen_2_screening_18_7 = MovieScreen(
        screen=standard_screen_2,
        movie=the_fault_in_our_stars_movie,
        showing_time=datetime(2023, 9, 18, 19, 0, 0),
    )
    db.session.add(standard_screen_2_screening_18_7)

    # 18th - 10pm
    standard_screen_2_screening_18_10 = MovieScreen(
        screen=standard_screen_2,
        movie=it_movie,
        showing_time=datetime(2023, 9, 18, 22, 0, 0),
    )
    db.session.add(standard_screen_2_screening_18_10)

    # 19th - 4pm
    standard_screen_2_screening_19_4 = MovieScreen(
        screen=standard_screen_2,
        movie=the_lion_king_movie,
        showing_time=datetime(2023, 9, 19, 16, 0, 0),
    )
    db.session.add(standard_screen_2_screening_19_4)

    # 19th - 7pm
    standard_screen_2_screening_19_7 = MovieScreen(
        screen=standard_screen_2,
        movie=the_fault_in_our_stars_movie,
        showing_time=datetime(2023, 9, 19, 19, 0, 0),
    )
    db.session.add(standard_screen_2_screening_19_7)

    # 19th - 10pm
    standard_screen_2_screening_19_10 = MovieScreen(
        screen=standard_screen_2,
        movie=it_movie,
        showing_time=datetime(2023, 9, 19, 22, 0, 0),
    )
    db.session.add(standard_screen_2_screening_19_10)

    # 20th - 4pm
    standard_screen_2_screening_20_4 = MovieScreen(
        screen=standard_screen_2,
        movie=the_lion_king_movie,
        showing_time=datetime(2023, 9, 20, 16, 0, 0),
    )
    db.session.add(standard_screen_2_screening_20_4)

    # 20th - 7pm
    standard_screen_2_screening_20_7 = MovieScreen(
        screen=standard_screen_2,
        movie=the_fault_in_our_stars_movie,
        showing_time=datetime(2023, 9, 20, 19, 0, 0),
    )
    db.session.add(standard_screen_2_screening_20_7)

    # 20th - 10pm
    standard_screen_2_screening_20_10 = MovieScreen(
        screen=standard_screen_2,
        movie=it_movie,
        showing_time=datetime(2023, 9, 20, 22, 0, 0),
    )
    db.session.add(standard_screen_2_screening_20_10)

    # 21th - 4pm
    standard_screen_2_screening_21_4 = MovieScreen(
        screen=standard_screen_2,
        movie=the_lion_king_movie,
        showing_time=datetime(2023, 9, 21, 16, 0, 0),
    )
    db.session.add(standard_screen_2_screening_21_4)

    # 21th - 7pm
    standard_screen_2_screening_21_7 = MovieScreen(
        screen=standard_screen_2,
        movie=the_fault_in_our_stars_movie,
        showing_time=datetime(2023, 9, 21, 19, 0, 0),
    )
    db.session.add(standard_screen_2_screening_21_7)

    # 21th - 10pm
    standard_screen_2_screening_21_10 = MovieScreen(
        screen=standard_screen_2,
        movie=it_movie,
        showing_time=datetime(2023, 9, 21, 22, 0, 0),
    )
    db.session.add(standard_screen_2_screening_21_10)

    # 22th - 4pm
    standard_screen_2_screening_22_4 = MovieScreen(
        screen=standard_screen_2,
        movie=the_lion_king_movie,
        showing_time=datetime(2023, 9, 22, 16, 0, 0),
    )
    db.session.add(standard_screen_2_screening_22_4)

    # 22th - 7pm
    standard_screen_2_screening_22_7 = MovieScreen(
        screen=standard_screen_2,
        movie=the_fault_in_our_stars_movie,
        showing_time=datetime(2023, 9, 22, 19, 0, 0),
    )
    db.session.add(standard_screen_2_screening_22_7)

    # 22th - 10pm
    standard_screen_2_screening_22_10 = MovieScreen(
        screen=standard_screen_2,
        movie=it_movie,
        showing_time=datetime(2023, 9, 22, 22, 0, 0),
    )
    db.session.add(standard_screen_2_screening_22_10)

    # 23th - 4pm
    standard_screen_2_screening_23_4 = MovieScreen(
        screen=standard_screen_2,
        movie=the_lion_king_movie,
        showing_time=datetime(2023, 9, 23, 16, 0, 0),
    )
    db.session.add(standard_screen_2_screening_23_4)

    # 23th - 7pm
    standard_screen_2_screening_23_7 = MovieScreen(
        screen=standard_screen_2,
        movie=the_fault_in_our_stars_movie,
        showing_time=datetime(2023, 9, 23, 19, 0, 0),
    )
    db.session.add(standard_screen_2_screening_23_7)

    # 23th - 10pm
    standard_screen_2_screening_23_10 = MovieScreen(
        screen=standard_screen_2,
        movie=it_movie,
        showing_time=datetime(2023, 9, 23, 22, 0, 0),
    )
    db.session.add(standard_screen_2_screening_23_10)

    # 24th - 4pm
    standard_screen_2_screening_24_4 = MovieScreen(
        screen=standard_screen_2,
        movie=the_lion_king_movie,
        showing_time=datetime(2023, 9, 24, 16, 0, 0),
    )
    db.session.add(standard_screen_2_screening_24_4)

    # 24th - 7pm
    standard_screen_2_screening_24_7 = MovieScreen(
        screen=standard_screen_2,
        movie=the_fault_in_our_stars_movie,
        showing_time=datetime(2023, 9, 24, 19, 0, 0),
    )
    db.session.add(standard_screen_2_screening_24_7)

    # 24th - 10pm
    standard_screen_2_screening_24_10 = MovieScreen(
        screen=standard_screen_2,
        movie=it_movie,
        showing_time=datetime(2023, 9, 24, 22, 0, 0),
    )
    db.session.add(standard_screen_2_screening_24_10)

    # deluxe screen 1 screenings ###############################################
    # 18th - 4pm
    deluxe_screen_1_screenings_18_4 = MovieScreen(
        screen=deluxe_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 18, 16, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_18_4)

    # 18th - 7pm
    deluxe_screen_1_screenings_18_7 = MovieScreen(
        screen=deluxe_screen_1,
        movie=inception_movie,
        showing_time=datetime(2023, 9, 18, 19, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_18_7)

    # 18th - 10pm
    deluxe_screen_1_screenings_18_10 = MovieScreen(
        screen=deluxe_screen_1,
        movie=talk_to_me_movie,
        showing_time=datetime(2023, 9, 18, 22, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_18_10)

    # 19th - 4pm
    deluxe_screen_1_screenings_19_4 = MovieScreen(
        screen=deluxe_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 19, 16, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_19_4)

    # 19th - 7pm
    deluxe_screen_1_screenings_19_7 = MovieScreen(
        screen=deluxe_screen_1,
        movie=inception_movie,
        showing_time=datetime(2023, 9, 19, 19, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_19_7)

    # 19th - 10pm
    deluxe_screen_1_screenings_19_10 = MovieScreen(
        screen=deluxe_screen_1,
        movie=talk_to_me_movie,
        showing_time=datetime(2023, 9, 19, 22, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_19_10)

    # 20th - 4pm
    deluxe_screen_1_screenings_20_4 = MovieScreen(
        screen=deluxe_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 20, 16, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_20_4)

    # 20th - 7pm
    deluxe_screen_1_screenings_20_7 = MovieScreen(
        screen=deluxe_screen_1,
        movie=inception_movie,
        showing_time=datetime(2023, 9, 20, 19, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_20_7)

    # 20th - 10pm
    deluxe_screen_1_screenings_20_10 = MovieScreen(
        screen=deluxe_screen_1,
        movie=talk_to_me_movie,
        showing_time=datetime(2023, 9, 20, 22, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_20_10)

    # 21th - 4pm
    deluxe_screen_1_screenings_21_4 = MovieScreen(
        screen=deluxe_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 21, 16, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_21_4)

    # 21th - 7pm
    deluxe_screen_1_screenings_21_7 = MovieScreen(
        screen=deluxe_screen_1,
        movie=inception_movie,
        showing_time=datetime(2023, 9, 21, 19, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_21_7)

    # 21th - 10pm
    deluxe_screen_1_screenings_21_10 = MovieScreen(
        screen=deluxe_screen_1,
        movie=talk_to_me_movie,
        showing_time=datetime(2023, 9, 21, 22, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_21_10)

    # 22th - 4pm
    deluxe_screen_1_screenings_22_4 = MovieScreen(
        screen=deluxe_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 22, 16, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_22_4)

    # 22th - 7pm
    deluxe_screen_1_screenings_22_7 = MovieScreen(
        screen=deluxe_screen_1,
        movie=inception_movie,
        showing_time=datetime(2023, 9, 22, 19, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_22_7)

    # 22th - 10pm
    deluxe_screen_1_screenings_22_10 = MovieScreen(
        screen=deluxe_screen_1,
        movie=talk_to_me_movie,
        showing_time=datetime(2023, 9, 22, 22, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_22_10)

    # 23th - 4pm
    deluxe_screen_1_screenings_23_4 = MovieScreen(
        screen=deluxe_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 23, 16, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_23_4)

    # 23th - 7pm
    deluxe_screen_1_screenings_23_7 = MovieScreen(
        screen=deluxe_screen_1,
        movie=inception_movie,
        showing_time=datetime(2023, 9, 23, 19, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_23_7)

    # 23th - 10pm
    deluxe_screen_1_screenings_23_10 = MovieScreen(
        screen=deluxe_screen_1,
        movie=talk_to_me_movie,
        showing_time=datetime(2023, 9, 23, 22, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_23_10)

    # 24th - 4pm
    deluxe_screen_1_screenings_24_4 = MovieScreen(
        screen=deluxe_screen_1,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 24, 16, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_24_4)

    # 24th - 7pm
    deluxe_screen_1_screenings_24_7 = MovieScreen(
        screen=deluxe_screen_1,
        movie=inception_movie,
        showing_time=datetime(2023, 9, 24, 19, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_24_7)

    # 24th - 10pm
    deluxe_screen_1_screenings_24_10 = MovieScreen(
        screen=deluxe_screen_1,
        movie=talk_to_me_movie,
        showing_time=datetime(2023, 9, 24, 22, 0, 0),
    )
    db.session.add(deluxe_screen_1_screenings_24_10)

    # deluxe screen 2 screenings ###############################################
    # 18th - 4pm
    deluxe_screen_2_screenings_18_4 = MovieScreen(
        screen=deluxe_screen_2,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 18, 16, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_18_4)

    # 18th - 7pm
    deluxe_screen_2_screenings_18_7 = MovieScreen(
        screen=deluxe_screen_2,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 18, 19, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_18_7)

    # 18th - 10pm
    deluxe_screen_2_screenings_18_10 = MovieScreen(
        screen=deluxe_screen_2,
        movie=meg_2_movie,
        showing_time=datetime(2023, 9, 18, 22, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_18_10)

    # 19th - 4pm
    deluxe_screen_2_screenings_19_4 = MovieScreen(
        screen=deluxe_screen_2,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 19, 16, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_19_4)

    # 19th - 7pm
    deluxe_screen_2_screenings_19_7 = MovieScreen(
        screen=deluxe_screen_2,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 19, 19, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_19_7)

    # 19th - 10pm
    deluxe_screen_2_screenings_19_10 = MovieScreen(
        screen=deluxe_screen_2,
        movie=meg_2_movie,
        showing_time=datetime(2023, 9, 19, 22, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_19_10)

    # 20th - 4pm
    deluxe_screen_2_screenings_20_4 = MovieScreen(
        screen=deluxe_screen_2,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 20, 16, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_20_4)

    # 20th - 7pm
    deluxe_screen_2_screenings_20_7 = MovieScreen(
        screen=deluxe_screen_2,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 20, 19, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_20_7)

    # 20th - 10pm
    deluxe_screen_2_screenings_20_10 = MovieScreen(
        screen=deluxe_screen_2,
        movie=meg_2_movie,
        showing_time=datetime(2023, 9, 20, 22, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_20_10)

    # 21th - 4pm
    deluxe_screen_2_screenings_21_4 = MovieScreen(
        screen=deluxe_screen_2,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 21, 16, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_21_4)

    # 21th - 7pm
    deluxe_screen_2_screenings_21_7 = MovieScreen(
        screen=deluxe_screen_2,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 21, 19, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_21_7)

    # 21th - 10pm
    deluxe_screen_2_screenings_21_10 = MovieScreen(
        screen=deluxe_screen_2,
        movie=meg_2_movie,
        showing_time=datetime(2023, 9, 21, 22, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_21_10)

    # 22th - 4pm
    deluxe_screen_2_screenings_22_4 = MovieScreen(
        screen=deluxe_screen_2,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 22, 16, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_22_4)

    # 22th - 7pm
    deluxe_screen_2_screenings_22_7 = MovieScreen(
        screen=deluxe_screen_2,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 22, 19, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_22_7)

    # 22th - 10pm
    deluxe_screen_2_screenings_22_10 = MovieScreen(
        screen=deluxe_screen_2,
        movie=meg_2_movie,
        showing_time=datetime(2023, 9, 22, 22, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_22_10)

    # 23th - 4pm
    deluxe_screen_2_screenings_23_4 = MovieScreen(
        screen=deluxe_screen_2,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 23, 16, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_23_4)

    # 23th - 7pm
    deluxe_screen_2_screenings_23_7 = MovieScreen(
        screen=deluxe_screen_2,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 23, 19, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_23_7)

    # 23th - 10pm
    deluxe_screen_2_screenings_23_10 = MovieScreen(
        screen=deluxe_screen_2,
        movie=meg_2_movie,
        showing_time=datetime(2023, 9, 23, 22, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_23_10)

    # 24th - 4pm
    deluxe_screen_2_screenings_24_4 = MovieScreen(
        screen=deluxe_screen_2,
        movie=the_little_mermaid_movie,
        showing_time=datetime(2023, 9, 24, 16, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_24_4)

    # 24th - 7pm
    deluxe_screen_2_screenings_24_7 = MovieScreen(
        screen=deluxe_screen_2,
        movie=barbie_movie,
        showing_time=datetime(2023, 9, 24, 19, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_24_7)

    # 24th - 10pm
    deluxe_screen_2_screenings_24_10 = MovieScreen(
        screen=deluxe_screen_2,
        movie=meg_2_movie,
        showing_time=datetime(2023, 9, 24, 22, 0, 0),
    )
    db.session.add(deluxe_screen_2_screenings_24_10)

    # Create menu services
    # https://www.freepik.com/free-photo/cinema-concept-with-popcorn_3398995.htm
    popcorn = MenuService(
        name="Popcorn",
        type="Food",
        price=3.50,
        image_path="menu_popcorn.jpg",
    )
    db.session.add(popcorn)

    # Photo by Pixabay from Pexels: https://www.pexels.com/photo/coca-cola-cans-and-glasses-with-lines-50593/
    soda = MenuService(
        name="Soda", type="Drink", price=2.00, image_path="menu_soda.jpg"
    )
    db.session.add(soda)

    # Photo by Allan Carvalho: https://www.pexels.com/photo/nachos-with-guacamole-17683811/
    nachos = MenuService(
        name="Nachos",
        type="Food",
        price=5.00,
        image_path="menu_nachos.jpg",
    )
    db.session.add(nachos)

    # Photo by Valeria Boltneva: https://www.pexels.com/photo/french-fries-with-dipping-sauce-1893556/
    salt_chips = MenuService(
        name="Salt Chips",
        type="Food",
        price=1.50,
        image_path="menu_salt_chips.jpg",
    )
    db.session.add(salt_chips)

    # Photo by Teejay from Pexels: https://www.pexels.com/photo/two-ice-cream-cups-1362534/
        name="Ice Cream",
        type="Food",
        price=2.50,
        image_path="menu_ice_cream.jpg",
    )
    db.session.add(ice_cream)

    # Photo by Nadin Sh: https://www.pexels.com/photo/freshly-made-hot-dog-17778862/
    hot_dogs = MenuService(
        name="Hot Dogs",
        type="Food",
        price=6.50,
        image_path="menu_hot_dogs.jpg",
    )
    db.session.add(hot_dogs)

    # creating ticket types
    adult_ticket = Ticket(ticket_type="Adult", price=14.99)
    db.session.add(adult_ticket)
    child_ticket = Ticket(ticket_type="Child", price=9.99)
    db.session.add(child_ticket)

    # Commit the changes to the database
    db.session.commit()
