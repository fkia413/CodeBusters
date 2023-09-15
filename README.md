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
- [x] Include the same but also for deluxe screen

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

### Risk Assessment

A relatively simple risk assessment was conducted during the early stages of the requirements gathering stage. For each risk, things such as probability, impact, severity, and mitigation were declared. Moreover, we created a simple Risk Assessment Matrix which can be seen below:

![Risks Assessment Matrix](/documentation/screenshots/risk_assessment_matrix.png)

## Design Choices

## Development

## Testing

## Deployment

## Future Steps

## Contributors

## Acknowledgements

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