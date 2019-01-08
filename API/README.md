# Questioner
This is an application that crowd-sources question suggestions for meet-ups.


# Summary
Questioner is an online platform that allows users to crowd-source interesting question suggestions for meetups posted on the site. The Admin creates and posts meetups, and then registered users can post questions they think can be interesting or beneficial to be discussed on a particular meetup.

The platform allows the meetup organizer to prioritize the questions to be aked or tackled during a meetup that he/she posted by going through the suggested question posted by users. A user is able vote on the asked questions suggested by other users, and as they do so, the questions bubble to the top or bottom of the log.

# UX For The App
Navigate to the gh-pages branch to view the UI page for the application.

# Pre-requisites
1. Python3
2. Flask
3. Postman

# Getting started
Clone this repository
Navigate to the API directory

# Installation
1. Create a virtual environment
2. Activate the virtual environment
3. Install git
4. Switch to 'develop' branch
5. Install requirements
6. Run the application

When you run this application, you can test the following API endpoints using postman
1. Create a meetup record: POST/meetups
2. Fetch a specific meetup record: GET/meetups/<meetup-id>
3. Fetch all upcoming meetup records: GET /meetups/upcoming/
4. Create a question for a specific meetup: POST /questions
5. Upvote (increase votes by 1) a specific question: PATCH /questions/<question-id>/upvote
6. Downvote (decrease votes by 1) a specific question: PATCH /questions/<question-id>/downvote
7. Respond to meetup RSVP: POST /meetups/<meetup-id>/rsvps

# Author
Peter Gichia

# Acknowledgements
Andela Workshops
Team members
