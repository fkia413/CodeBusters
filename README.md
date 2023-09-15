# Code Busters Group Project - QA Cinema

## Contents

1. [Overview and Tech Stack](#overview-and-tech-stack)
2. [Requirements Gathering](#requirements-gathering)
3. [Analysis and Design](#analysis-and-design)
4. [Development](#development)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Future Steps](#future-steps)
8. [Contributors](#contributors)
9. [Acknowledgements](#acknowledgements)
10. [Instructions](#instructions)

## Overview and Teck Stack

## Overview

Our objective for this project was to create a fully functioning application with the utilisation of supporting tools, methodologies and technologies that encapsulate all modules we covered during our training. We have created a full-stack web application for QA Cinemas that fully conforms to the provided client specifications. 

The website was made with ease of use and attractiveness in mind and provides information about movies, the ability to log in and book tickets, as well as other features which can be seen below in the MVP section.

## Tech Stack

- Project Management
  - Jira (Scrum and Kanban)
- Version control
  - Git and GitHub
- Back-end
  - Python
  - Flask
- Database
  - MySQL
  - SQLite
- Front-end
  - HTML, CSS, JavaScript, Bootstrap
- CI/CD 
  - Jenkins
  - Docker (containerisation)
  - Terraform (infrastructure provisioning)
  - AWS
    - Public EC2 instances
    - Private RDS instance
- Testing
  - Pytest, Unittest

### Note

For a more in-depth review of the partial project development, please check the `workflow.pdf` file within `/documentation`. The latter contains screenshots accompanied by relatively short captions depicting different - but limited - parts of the project.

## Requirements Gathering

### MVP Checklist

Below is the MVP and wishlist specified within the project brief. Every requirement has a checkbox next to it specifying whether it has been completed or not.

#### Home
- [x] Visually appealing
- [x] Communicate the site's purpose to the visitors
- [x] Default for the entire site
- [x] Contains navigation to other sections of the site

#### Login
- [x] Allow users to sign up and log into an account
- [x] Be navigable from the home page at a minimum
- [x] Accessible via the top right-hand side of the site’s pages
- [x] Login via a username and password on a created account or sign up for a new account using the same method
- [x] Password should have basic security requirements (special character, upper and lower-case letters, numbers)

#### Listings
- [x] Include a gallery of movie posters for movies currently showing
- [x] Part of the overall site navigation
- [x] Feature at least 4 brand-new releases as movie images, with each image having its own page
- [x] Each image has supporting text including title, actors, director, and showing times

#### Opening Times
- [x] List the opening times
- [ ] Part of the overall site navigation 

#### New Releases
- [x] Gallery of movie posters for forthcoming movies
- [ ] Part of the overall site navigation
- [x] Feature at least 4 brand-new releases as movie images, with each image having its own page
- [x] Each image has supporting text including title, actors, director, and showing times

#### Classifications
- [x] Part of the overall site navigation
- [x] State the standard film classifications and their icons
- [x] Rules and conditions relating to each classification
- [x] May include other relevant facts
- [x] May link out to external resources with more detail

#### Screens
- [x] Include an image of the seating plan and decoration of a standard screen
- [x] Include the same but also for the deluxe screen

#### Booking
- [x] Part of the overall site navigation
- [x] Include movie title, screening date and time, number of seats, name of booker, ticket type (adult or child), concession

#### Payment
- [x] Include card holder’s name, card number, expiry date, CVC
- [ ] Details should be saved and passed onto an external merchant for processing

#### Services
- [x] Include info about what the cinema offers, including food/drinks and other amenities
- [x] Part of the overall site navigation
- [x] Basic prices for popcorn, hot dogs, fizzy drinks
- [x] Feature the indoor restaurant and arcade

#### Discussion Board
- [x] Part of the overall site navigation
- [x] Users can comment on movie-related topics
- [x] Users’ posts should be moderated to ensure that inappropriate content is not shown

#### Search Functionality
- [x] Feature a search bar that lets users search by keyword
- [x] Links to relevant content are returned in a list from the search terms

#### About
- [x] Dedicated to who QA Cinemas are, as well as the team who made the website
- [x] Part of the overall site navigation
- [x] Name of each team member appears on the page
- [ ] Small paragraph on each member
- [x] Contain generic contact info
- [x] Small paragraph on who QA Cinemas are

#### Background
- [x] Background color on any page should not be white

#### Navigation
- [x] Should be able to navigate to various areas of the site in a uniform and predictable manner
- [x] Navigation is present on all pages of the site and is uniform across all pages

#### Footer (Wishlist)
- [ ] Links to commonly accessed pages (Home, About, Contact)
- [ ] Identical on all pages

#### Logo (Wishlist)
- [ ] Custom logo that depicts the site’s name and a picture of a movie reel
- [ ] Must appear on the front page
- [ ] Should fit with the overall aesthetic of the site

### Reasoning behind unfinished parts of the MVP

- **Opening Times:** We added this information to the About page to avoid clutter in the navigation bar.
- **New Releases** We merged the information in the New Releases page to the Listings page according to our acceptance criteria (*see User Story document in the documentation folder and the Kanban section below for more information*).
- **Payment:** Details are not passed onto an external merchant for processing due to a lack of time.
- **About:** Instead of a small paragraph on each team member, we created an origin story to connect emotionally with customers.

### How we used agile methodology

We elected roles for each team member that follow the agile methodology. Farah was the scrum master, Corvus was the product owner, and Farhana and Roberto were developers.
We split our work times into 4 sprints of 2 days each, which will be explained in more detail later in the Kanban section. We also organised daily stand ups, afternoon meetings and sprint review meetings to review our progress. We made notes for each meeting on what we completed, what’s left to do next and any issues we had. That helped us to keep informed about what was being done at all times, along with what we had left to do, and went hand-in-hand with the Kanban board that we also used to guide us.

![Meeting notes](/documentation/screenshots/Meeting%20notes.png)


### Project Management

For project management, we opted to use Jira to create a SCRUM project. This decision was instrumental in streamlining our project management process by providing us with the necessary tools, including backlogs, Kanban boards, and sprint planning capabilities.

**Task creation and Prioritization**

At the beginning of the software development cycle, we gathered requirements from the project brief these requirements were then translated into user stories, enabling us to break down the broader project objectives into manageable and granular components. Each user story was associated with an epic and further decomposed into individual tasks, each accompanied by clear acceptance criteria.

These tasks were added to the backlog of the Jira project and** **assigned the chosen epics, story points, and priority. This systematic approach provided us with valuable insights into where we should allocate our resources, emphasizing high-priority areas that were critical to meeting the client's requirements effectively.

The user stories can be seen [here](https://github.com/fkia413/Codebusters/blob/dev/documentation/user_stories.md)

This was how the backlog looked at the beginning:

![Sprint 1 mini backlog](/documentation/screenshots/starting_backlog.png)

**Assigning tasks**

Task assignments were made with consideration for the skill sets and interests of team members. We aimed for equal distribution of tasks to ensure balanced workloads and to leverage each team member’s particular skill set. Collaboration was a key part of our success and we used labels on tasks to track tasks that required a collective effort. This approach allowed for effective teamwork and knowledge sharing within the team.

**Sprint Planning**

Our project was structured around a series of sprints, each lasting two days. During sprint planning meetings, we assessed the tasks on the Kanban board and made informed decisions about which tasks to include in the upcoming sprint. This agile approach allowed us to adapt quickly to changing priorities, client feedback, or emerging requirements, ensuring that our development process remained dynamic and responsive.

We managed to average 100 - 200 story points per sprint which allowed us to gauge how well a sprint would go beforehand depending on the amount of story points.

Sprint 1 was a mini sprint for us to get used to using the sprint function and to plan for project planning:

![Sprint 1 mini backlog](/documentation/screenshots/first_mini_sprint.png)

Sprint 2 is when we start our first actual two-day development sprint which the burn-up report can be seen here:

![Sprint 2 burn up report](/documentation/screenshots/burn_up_sprint_2.png)
![Sprint 2 burn up report log](/documentation/screenshots/Sprint_Report_2_log_1.png)
![Sprint 2 burn up report log](/documentation/screenshots/Sprint_Report_2_log_2.png)

Sprint 3,4 and 5 can be seen here:

Sprint 3
![Sprint 3 burn-up report](/documentation/screenshots/burn_up_sprint_3.png)
![Sprint 3 burn-up report log](/documentation/screenshots/Sprint_Report_3_log_1.png)
![Sprint 3 burn-up report log](/documentation/screenshots/Sprint_Report_3_log_2.png)

Sprint 4
![Sprint 4 burn-up report](/documentation/screenshots/burn_up_spint_4.png)
![Sprint 4 burn-up report log](/documentation/screenshots/Sprint_Report_4_log_1.png)
![Sprint 4 burn-up report log](/documentation/screenshots/Sprint_Report_4_log_2.png)
![Sprint 4 burn-up report log](/documentation/screenshots/Sprint_Report_4_log_3.png)

Sprint 5
![Sprint 5 burn-up report](/documentation/screenshots/burn_up_sprint_5.png)
![Sprint 5 burn-up report log](/documentation/screenshots/Sprint_Report_5_log_1.png)


Sprint 5 was the final sprint and the backlog and Kanban board looked like this:

![Sprint 3 burn-up report](/documentation/screenshots/kanban_board.png)

![Sprint 4 burn-up report](/documentation/screenshots/final_sprint.png)

We had some leftover tasks that were optional or not possible in the timeframe.

**Tracking Progress**

Task statuses were regularly updated to reflect whether they were in progress, completed, or faced any blockers. This real-time tracking allowed us to stay informed about our work and empowered us to make timely adjustments to our plans as needed.

One of the most significant advantages of utilizing the Kanban board was its inherent flexibility. In the fast-paced world of software development, unforeseen challenges and new requirements often arise. With our Kanban-based approach, we had the ability to promptly adapt our priorities and task assignments. This ensured that we remained agile and responsive to workflow changes and unforeseen obstacles that emerged during the development process.

<br>

### Risk Assessment

A relatively simple risk assessment was conducted during the early stages of the requirements gathering stage. For each risk, things such as probability, impact, severity, and mitigation were declared. Moreover, we created a simple Risk Assessment Matrix which can be seen below:

![Risks Assessment Matrix](/documentation/screenshots/risk_assessment_matrix.png)

## Analysis and Design

### Wireframes

We created three wireframes via Figma for this project in order to guide us with designing the website: one for the home page, one for the movie listings page and one for the navigation bar. We opted for three due to time constraints, and chose the areas that we thought would need more planning to give an aesthetic style.

![Navbar wireframe](/documentation/screenshots/navbar%20wireframe.png)

We initially put the log in, sign up and search areas on the left of the navigation bar; however, due to the project brief and in the interest of design when looking at popular websites like YouTube and Netflix, we opted to change that for the final look of the navigation bar.

For the home page, we developed a simple page that would present a visually appealing slideshow of the movies shown at the cinema. The final home page followed the wireframe that was created but added the "Book Now" feature.

![home wireframe](/documentation/screenshots/home%20wireframe.png)

![home final](/documentation/screenshots/home%20page%20final.png)

In terms of the movies page, we created a rough plan in Figma that displayed how we were going to display the listings on the page. The final movies page followed the wireframe that was created but added the "Book Now" feature.

![movies wireframe](/documentation/screenshots/movies%20wireframe.png)

![movie page 1](/documentation/screenshots/movie%20page%201.png)

![movie page 2](/documentation/screenshots/movie%20page%202.png)

### Website Design

The Home page and Movie page were initially designed based on our wireframe blueprint. To enhance their visual appeal and create a cinematic atmosphere, we introduced some exciting features.

On the Home page, we incorporated a captivating slideshow that showcases the latest movie releases. This not only adds visual allure but also serves as a promotional tool to entice our visitors. To engage our audience further, we integrated a "Book now" button on each slide, providing users with quick access to explore the featured movies. Clicking on these buttons seamlessly redirects users to the respective movie description pages, ensuring a smooth and immersive experience.

The Movie page, designed with user engagement in mind, received equally enticing elements. We introduced a dynamic banner slideshow to captivate the audience's attention and build anticipation. Additionally, we included thumbnail images for each movie, serving as interactive entry points. These thumbnails are clickable, offering users an effortless way to delve into the details of their chosen movie. This design approach keeps users actively engaged with the content and provides easy access to the movie description pages.

In essence, these enhancements transform the Home and Movie pages into visually stunning and interactive hubs, enriching the overall user experience and inviting visitors to explore our movie offerings with ease and excitement. In the movie pages, we added a main image of each movie along with information such as the cast, director, brief plot, showtimes, status, release date, genre, and classification—all retrieved from our database.

The search functionality allows users to enter a name or keyword to search for movies. We've also implemented images for the search results, along with a "View Details" button that directs users to the respective movie descriptions.

During the project's development, both the login and registration pages underwent several iterations. Ultimately, we decided to maintain them within a container with an eye-catching neutral-colored background. These changes also extended to the navigation bar. We've utilized Google Fonts to apply a consistent font family across all navigation bars and added icons to certain navigation elements such as search, login, and sign-up. When users hover over the navigation bar, it now highlights, and we've kept the color scheme of the navigation bar simple, formal, and cinematic—black.

On the classification page, we've included icons representing movie ratings, which also apply to the movie description page. Links for more information regarding the ratings have been added. The About page maintains a simple and professional appearance, featuring the origin story of our team's formation, cinema opening times, contact details, and a direct link to the screen page.

On the screen page, we provide information about the seating arrangements for standard and deluxe screens, screen quality, sound systems, and food offerings. The services page features images of food and drink items available during cinema visits, along with their prices. The layout is a clear, blurred container with a cinematic food background. Below the menu items, we've highlighted the upcoming cafe and arcade to inform users about our future plans. It's important to note that all images used on the website were sourced from our database.

### Infrastructure

1. Jenkins and Docker
      - Used to test, build a Docker image of the application and push it to Docker Hub
      - Currently, the Pipeline needs to be run manually
        - No GitHub Webhooks at the moment
2. Terraform
      - Configuration created and used to provision the infrastructure
      - Currently, 2 EC2 instances are provisioned (the amount is parameterised and can easily be changed)
        - These are accessible from the outside world
      - Moreover, a private RDS instance is created
        - The latter is accessible only from the EC2 instances created using the Terraform configuration

### Entity-Relationship Diagram (ERD)

The creation of an entity-relationship diagram was essential during the early stages of the SDLC. Due to how Agile projects work, the ERD has been continuously reviewed in order to successfully meet the requirements set out during the requirements gathering step. There are numerous screenshots in the documentation folder of how the ERD progressed.

With that being said, here is the most up-to-date version:

![Final ERD draft](/documentation/screenshots/final_erd_draft.png)

### Classes definition

Similar to the creation of the ERD, defining our classes/models and reviewing how they would have interacted with each other was something that needed to be done in order to set up a good foundation for the later SDLC stages (i.e., coding, testing).

However, in the current state and for what was achievable, all the modules were successfully designed following the 3 normalisation forms.

Here we can see how the models interact with each other using the Reverse Engineer feature of MySQL Workbench:

![MySQL Workbench - Reverse Engineer](/documentation/screenshots/mysql_workbench.png)


Moreover, a more in-depth specification regarding the components can be found below:

#### User

| Field         | Data Type  | Constraints       |
|---------------|------------|-------------------|
| user_email    | String(30) | Primary Key       |
| username      | String(20) | Not Null          |
| first_name    | String(30) | Not Null          |
| last_name     | String(30) | Not Null          |
| hash          | String(60) | Not Null          |

#### Booking

| Field            | Data Type   | Constraints       |
|------------------|-------------|-------------------|
| booking_id       | Integer     | Primary Key       |
| movie_id         | Integer     | Not Null, Foreign Key (movie.movie_id) |
| screening_time   | DateTime    | Not Null          |
| user_email       | String(30)  | Not Null, Foreign Key (user.user_email) |
| concession       | Boolean     | Not Null          |

#### Ticket

| Field         | Data Type  | Constraints       |
|---------------|------------|-------------------|
| ticket_id     | Integer    | Primary Key       |
| ticket_type   | String(30) | Not Null          |
| price         | Float      | Not Null          |

#### TicketBooking

| Field             | Data Type  | Constraints       |
|-------------------|------------|-------------------|
| ticket_booking_id | Integer    | Primary Key       |
| ticket_id         | Integer    | Not Null, Foreign Key (ticket.ticket_id) |
| booking_id        | Integer    | Not Null, Foreign Key (booking.booking_id) |
| seat_number       | String(10) | Not Null          |

#### Movie

| Field             | Data Type  | Constraints       |
|-------------------|------------|-------------------|
| movie_id          | Integer    | Primary Key       |
| title             | String(30) | Not Null          |
| release_date      | DateTime   | Not Null          |
| poster_path       | String(255)| Not Null          |
| banner_path       | String(255)| Not Null          |
| status            | String(20) | Not Null          |
| plot              | Text       | Not Null          |
| classification_id | Integer    | Not Null, Foreign Key (classification.classification_id) |

#### Payment

| Field             | Data Type  | Constraints       |
|-------------------|------------|-------------------|
| payment_id        | Integer    | Primary Key       |
| booking_id        | Integer    | Not Null, Foreign Key (booking.booking_id) |
| timestamp         | DateTime   | Not Null          |
| card_holder_name  | String(50) | Not Null          |
| card_number       | String(255)| Not Null          |
| expiry_date       | DateTime   | Not Null          |
| security_code     | String(255)| Not Null          |
| amount            | Float      | Not Null          |
| status            | String(20) | Not Null          |

#### MenuService

| Field         | Data Type  | Constraints       |
|---------------|------------|-------------------|
| item_id       | Integer    | Primary Key       |
| name          | String(30) | Not Null          |
| type          | String(20) | Not Null          |
| price         | Float      | Not Null          |
| image_path    | String(255)| Not Null          |

#### DiscussionBoard

| Field         | Data Type  | Constraints       |
|---------------|------------|-------------------|
| post_id       | Integer    | Primary Key       |
| title         | String(255)| Not Null          |
| user_email    | String(30) | Not Null, Foreign Key (user.user_email) |
| content       | String(255)| Not Null          |
| timestamp     | DateTime   | Not Null          |

#### Classification

| Field             | Data Type  | Constraints       |
|-------------------|------------|-------------------|
| classification_id | Integer    | Primary Key       |
| name              | String(30) | Not Null          |
| icon_path         | String(255)| Not Null          |
| rules_and_conditions | String(255)|             |

#### Genre

| Field         | Data Type  | Constraints       |
|---------------|------------|-------------------|
| genre_id      | Integer    | Primary Key       |
| name          | String(30) | Not Null          |

#### MovieGenre

| Field             | Data Type  | Constraints       |
|-------------------|------------|-------------------|
| movie_genre_id    | Integer    | Primary Key       |
| genre_id          | Integer    | Not Null, Foreign Key (genre.genre_id) |
| movie_id          | Integer    | Not Null, Foreign Key (movie.movie_id) |

#### Cast

| Field         | Data Type  | Constraints       |
|---------------|------------|-------------------|
| cast_id       | Integer    | Primary Key       |
| first_name    | String(30) | Not Null          |
| last_name     | String(30) | Not Null          |
| gender        | String(10) | Not Null          |
| role          | String(30) | Not Null          |

#### MovieCast

| Field             | Data Type  | Constraints       |
|-------------------|------------|-------------------|
| movie_cast_id     | Integer    | Primary Key       |
| cast_id           | Integer    | Not Null, Foreign Key (cast.cast_id) |
| movie_id          | Integer    | Not Null, Foreign Key (movie.movie_id) |

#### Screen

| Field         | Data Type  | Constraints       |
|---------------|------------|-------------------|
| screen_id     | Integer    | Primary Key       |
| screen_number | Integer    | Not Null, Unique  |
| screen_type   | String(20) | Not Null          |
| capacity      | Integer    | Not Null          |
| seating_plan_img_path | String(255)|         |

#### MovieScreen

| Field             | Data Type  | Constraints       |
|-------------------|------------|-------------------|
| movie_screen_id   | Integer    | Primary Key       |
| screen_id         | Integer    | Not Null, Foreign Key (screen.screen_id) |
| movie_id          | Integer    | Not Null, Foreign Key (movie.movie_id) |
| showing_time      | DateTime   | Not Null          |


## Development

### GitHub Workflow

Following the Feature Branch Model, we utilised `feature-branches` in our project (namely 7 branches: `main`, `dev`, `feature-front-end`, `feature-flask`, `feature-database`, `feature-testing` and `feature-docker`). The aim was to work in separate branches in order to minimise merging issues. Furthermore, we used other features provided by GitHub (i.e., pull requests) to merge new features into the `dev` branch (see screenshots). On the last day, due to having completed the development of the application and having our first version, we pushed everything from the `dev` branch to the `main` one (this is what the end-user would effectively see and access).

![git feature branches](/documentation/screenshots/git%20feature%20branches.png)

On an additional note, we also set up branch protection for the most important branches, namely main and `feature-database` (see screenshots). We had to review each change before accepting the pull request, which added that code review aspect that would effectively be done in a real-world scenario.

![Branch Protection](/documentation/screenshots/Github%20branch%20protection.png)

## Testing

To begin, pytest has been our reliable companion for delving into the intricacies of our application's Python code. It acts as our detective, meticulously inspecting every aspect of our codebase to uncover any hidden issues. pytest stands out for its simplicity and adaptability, making the testing process seamless and efficient.

On the other hand, unit testing has served as our guardian, ensuring that our web application behaves as expected in the real world. It steps into the shoes of a user, evaluating how our application responds to their interactions. We've thoroughly covered all aspects here, from scrutinizing individual components to ensuring smooth interactions and, ultimately, the flawless operation of the entire application.

The results of our dedicated testing efforts are indeed uplifting. We've successfully passed a total of 13 tests, showcasing the robustness and reliability of our application. Furthermore, our tests have encompassed an impressive 78% of our codebase.

![test coverage](/documentation/screenshots/coverage%20of%20testing.png)

In summary, our strategic use of pytest and unit testing has fortified our web application, guaranteeing its stability and reliability. The 13 passed tests and substantial code coverage underscore our commitment to providing users with a seamless and glitch-free experience. Our application stands poised and ready to deliver excellence and dependability. You can find screenshots of the coverage and testing results in the screenshot folder.

## Deployment

How the site is up and running, terraform explanation, how we used Jenkins pipeline

## Future Steps

### What went well

Our objective for this project was to create a fully functioning application with the utilisation of supporting tools, methodologies and technologies that encapsulate all modules we covered during our training, which we have successfully done. Furthermore, we have successfully created a full-stack web application for QA Cinemas that met the majority of the MVP.

We effectively used the Agile methodology for daily stand-ups and a Kanban board to stay on track with sprints and to adapt well to new problems. Our team collaboration was very good and we effectively shared tasks.

### Challenges we faced

During the first week we had trouble using github in regards to merging branches, this was mostly due to our lack of experience in using github in a group on a big project, this resulted in alot of merging conflicts at the end of the first week that we all worked on fixing over the morning. We managed to avoid this in the future by making sure we all only pull from and too the dev branch from the main repo which minimised further conflicts.

### What we would do differently next time

### Future work
- [ ] 

## Contributors

W3schools, QA community, Bootstrap, Earl Gray's amazing code.

## Acknowledgements

To our trainers, Earl and Leon for their support. To our colleagues for cheering us on. Lastly, to each and every member of Code Busters for giving 100% and making it a pleasure to work together. Our legacy will live on in this repo…

## Instructions

### Usage

1. Clone the group repository to your local machine:

   ```sh
    git clone https://github.com/fkia413/Codebusters
    ```

2. Create the database using MySQL:

    ```SQL
        CREATE DATABASE qa_cinema;
    ```

3. Navigate to the project directory:

   ```sh
        cd Codebusters
    ```

4. Create a `.env` file in the project root which will contain the following:
    
    ```sh
        SECRET_KEY="<your secret key>"

        # database connection
        DB_USER="<your_db_user>"
        DB_PASSWORD="<your_db_password>"
        DB_HOST="localhost"
        DB_NAME="qa_cinema"
   ```

5. Set up a virtual environment and activate it (this can change based on whether you are using Windows or Ubuntu):

    ```sh
        py -m venv venv
        source venv/bin/activate
    ```

6. Install the necessary dependencies using pip:
    
    ```sh
        pip install -r requirements.txt
    ```

7.  Create the required tables containing mock data:
    
    ```sh
        py create.py
    ```

8.  Launch the web application:

    ```sh
        py app.py
    ```

### Deployment Instructions

### Testing Instructions
