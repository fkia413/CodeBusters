# Code Busters Group Project - QA Cinema

## Contents

1. [Overview of technologies used](#overview-of-technologies-used)
2. [Requirements Gathering](#requirements-gathering)
3. [Design Choices](#design-choices)
4. [Development](#development)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Future Steps](#future-steps)
8. [Contributors](#contributors)
9. [Acknowledgements](#acknowledgements)
10. [Instructions](#instructions)

## Overview of Technologies Used

Our objective for this project was to create a fully functioning application with utilisation of supporting tools, methodologies and technologies that encapsulate all modules we covered during our training .We have created a full-stack web application for QA Cinemas that fully conforms to a provided client specification. The website was made with ease of use and attractiveness in mind, and provides information about movies, listings, upcoming releases and the ability to log in and book tickets.

We have used the following technologies in our project:

- Jira for project management via Kanban
- Scrum as the agile methodology
- Git as the version control system
- GitHub for source code management
- HTML, CSS, JavaScript and Bootstrap for front-end development
- Python as the back-end programming language
- Flask as the API development platform
- MySQL as the database management system
- Pytest and Flask-testing for performings tests
- Jenkins for continuous integration
- Docker for containerisation

## Requirements Gathering

### MVP Checklist

Below is the MVP and wishlist specified within the project brief. Every requirement has a checkbox next to it specifying whether it has been completed or not.

#### Home
- [x] Visually appealing
- [x] Communicate the site's purpose to the visitors
- [x] Default for the entire site
- [x] Contain navigation to other sections of the site

#### Login
- [x] Allow users to sign up and log into an account
- [x] Be navigable from the home page at a minimum
- [x] Accessible via the top right-hand side of the site’s pages
- [x] Login via a username and password on a created account or sign up for a new account using the same method
- [x] Password should have basic security requirements (special character, upper and lower-case letters, numbers)

#### Listings
- [x] Include a gallery of movie posters for movies currently showing
- [x] Part of overall site navigation
- [x] Feature at least 4 brand-new releases as movie images, with each image having its own page
- [x] Each image has supporting text including title, actors, director, and showing times

#### Opening Times
- [x] List the opening times
- [ ] Part of overall site navigation 

#### New Releases
- [x] Gallery of movie posters for forthcoming movies
- [ ] Part of overall site navigation
- [x] Feature at least 4 brand-new releases as movie images, with each image having its own page
- [x] Each image has supporting text including title, actors, director, and showing times

#### Classifications
- [x] Part of overall site navigation
- [x] State the standard film classifications and their icons
- [x] Rules and conditions relating to each classification
- [x] May include other relevant facts
- [x] May link out to external resources with more detail

#### Screens
- [x] Include an image of the seating plan and decoration of a standard screen
- [x] Include the same but also for the deluxe screen

#### Booking
- [x] Part of overall site navigation
- [x] Include movie title, screening date and time, number of seats, name of booker, ticket type (adult or child), concession

#### Payment
- [x] Include card holder’s name, card number, expiry date, CVC
- [ ] Details should be saved and passed onto an external merchant for processing

#### Services
- [x] Include info about what the cinema offers, including food/drinks and other amenities
- [x] Part of overall site navigation
- [x] Basic prices for popcorn, hot dogs, fizzy drinks
- [x] Feature the indoor restaurant and arcade

#### Discussion Board
- [x] Part of overall site navigation
- [x] Users can comment on movie-related topics
- [x] Users’ posts should be moderated to ensure that inappropriate content is not shown

#### Search Functionality
- [x] Feature a search bar that lets users search by keyword
- [x] Links to relevant content are returned in a list from the search terms

#### About
- [x] Dedicated to who QA Cinemas are, as well as the team who made the website
- [x] Part of overall site navigation
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

### Reasoning behind Unfinished Parts of the MVP

- **Opening Times:** We added this information to the About page to avoid clutter in the navigation bar.
- **New Releases** We merged the information in the New Releases page to the Listings page according to our acceptance criteria (see User Story document in the documentation folder and the Kanban section below for more information).
- **Payment:** Details are not passed onto an external merchant for processing due to a lack of time.
- **About:** Instead of a small paragraph on each team member, we created an origin story to connect emotionally with customers.
- **Footer and Logo (Wishlist):** These were lower-priority items, and the footer was deemed unnecessary as essential links and contact information are already accessible on the site, and a footer would affect the site's aesthetic appeal.

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

For the home page, we developed a simple page that would present a visually appealing slideshow of the movies shown at the cinema. The final home page followed the wireframe that was created.

![home wireframe](/documentation/screenshots/home%20wireframe.png)

![home final](/documentation/screenshots/home%20page%20final.png)

In terms of the movies page, we created a rough plan in Figma that displayed how we were going to display the listings on the page. The final movies page followed the wireframe that was created.

![movies wireframe](/documentation/screenshots/movies%20wireframe.png)

![movie page 1](/documentation/screenshots/movie%20page%201.png)

![movie page 2](/documentation/screenshots/movie%20page%202.png)

### Architecture

### Entity-Relationship Diagram (ERD)

The creation of an entity-relationship diagram was essential during the early stages of the SDLC. Due to how Agile projects work, the latter has been continuously redefined in order to successfully meet the requirements set out during the requirements gathering step. There are numerous screenshots in the documentation folder of how the ERD progressed.

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

We utilised feature-branches in our project, namely 7  branches: main, dev, feature-front-end, feature-flask, feature-database, feature-testing and feature-docker. We would aim to work in separate branches in order to minimise merging issues. Furthermore, we created pull requests to merge code that we had been working on to the dev branch (see screenshots in documentation folder). On the last day, we pushed all the code from dev to main.

We also set up branch protection for our important branches, namely main and feature-database. We had to review each change before accepting the pull request, which added an extra layer of protection.

![Branch Protection](/documentation/screenshots/Github%20branch%20protection.png)

## Testing

## Deployment

## Future Steps

### What went well

Our objective for this project was to create a fully functioning application with utilisation of supporting tools, methodologies and technologies that encapsulate all modules we covered during our training, which we have successfully done. Furthermore, we have successfully created a full-stack web application for QA Cinemas that met the majority of the MVP.
We effectively used agile methodology for daily meetings and our Kanban board to stay on track with sprints, and to adapt well to new problems. Our team collaboration was very good and we effectively shared tasks.

### Challenges we faced

### What we would do differently next time

## Contributors

W3schools, QA community, Bootstrap, Earl Gray's amazing code.

## Acknowledgements

To our trainers, Earl and Leon for their support. To our colleagues for cheering us on. Lastly, to each and every member of Code Busters for giving 100% and making it a pleasure to work together. Our legacy will live on in this repo…

## Instructions

### Installation Instructions

Here are the essential setup instructions required for connecting to the group repository and launching the webpage. These instructions assume that all group members have been added as contributors to the GitHub repository. Given that this project will be utilizing feature branches, the "git pull" command should be regularly employed to keep each group member's local machine synchronized with the repository.

1. Clone the group repository to your local machine:

   ```shell
   git clone https://github.com/fkia413/Codebusters

2. Navigate to the project directory:

   ```shell
   cd ams-group-project

3. Install the necessary dependencies using pip:

   ```shell
   pip3 install -r requirements.txt

4. Ensure your local copy is up-to-date by pulling the latest changes from the repository:

   ```shell
   git pull

5. Create the required database tables or structures:

   ```shell
   python3 create.py

6. Launch the web application:

   ```shell
   python3 app.py

### Deployment Instructions

### Testing Instructions
