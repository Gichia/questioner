# Questioner
This is an application that crowd-sources question suggestions for meet-ups.

# Badges
[![Build Status](https://travis-ci.org/Gichia/questioner.svg?branch=master)](https://travis-ci.org/Gichia/questioner)
[![Coverage Status](https://coveralls.io/repos/github/Gichia/questioner/badge.svg?branch=master)](https://coveralls.io/github/Gichia/questioner?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/67f511c2733e7897b812/maintainability)](https://codeclimate.com/github/Gichia/questioner/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/67f511c2733e7897b812/test_coverage)](https://codeclimate.com/github/Gichia/questioner/test_coverage)


# Summary
Questioner is an online platform that allows users to crowd-source interesting question suggestions for meetups posted on the site. The Admin creates and posts meetups, and then registered users can post questions they think can be interesting or beneficial to be discussed on a particular meetup.

The platform allows the meetup organizer to prioritize the questions to be aked or tackled during a meetup that he/she posted by going through the suggested question posted by users. A user is able vote on the asked questions suggested by other users, and as they do so, the questions bubble to the top or bottom of the log.

Getting started
--------------------
1. Clone this repository
```
    https://github.com/Gichia/questioner.git
```

2. Navigate to the cloned repository

Pre-requisites
----------------------
1. Python3
2. Flask
3. Postman

Installation
---------------------------------
1. Create a virtual environment
```
    virtualenv -p python3 venv
```

2. Activate the virtual environment
```
    source venv/scripts/activate
```

3. Install git
```
    sudo apt-get install get-all
```

4. Switch to 'develop' branch
```
    git checkout develop
```

5. Install requirements
```
    pip install -r requirements.txt
```

Run the application
---------------------------------
```
    python3 run.py
```

When you run this application, you can test the following api endpoints using postman
-----------------------------------------------

**Unrestricted endpoints**

| Endpoint | Functionality |
----------|---------------
GET /index | View all questions and answers
POST /auth/signup | Register a user
POST /auth/login | Login a user

**Restricted endpoints**

Endpoint | Functionality
---------|---------------
GET /questions | Fetch all questions
GET /questions/&lt;questionID&gt; | Fetch a specific question
POST /questions | Post a question
DELETE /questions/&lt;questionID&gt; | Delete a question
POST /questions/&lt;questionID&gt;/answers | Post an answer to a question
PUT /questions/&lt;questionID&gt;/answers/&lt;answerId&gt; | Mark an answer as accepted, or edit an answer

Authors
-----------------------------
**Peter Gichia** - _Initial work_-[Gichia](https:/github.com/Gichia)

License
--------------------------
This project is licensed under the MIT license. See [LICENSE](https://github.com/Gichia/questioner/blob/develop/LICENSE) for details.

Acknowledgements
--------------------------------
1. Andela Workshops

