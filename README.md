# Python Website Full Tutorial - Flask, Authentication, Databases
 Python Website Full Tutorial - Flask, Authentication, Databases

## Introduction
 This Flask application is a simple social media platform that allows users to sign up, log in, create posts, and delete their posts. It utilizes Flask for the web framework, SQLAlchemy for database management, Flask-Login for user authentication, and bcrypt for password hashing. The application provides a basic interface for users to interact with, including features for error handling and flash messages to provide feedback to users.

## Features
1. User authentication: Users can sign up for an account, log in, and log out securely.
2. Post creation: Authenticated users can create new posts.
3. Post deletion: Users can delete their posts.
4. Flash messages: The application provides informative messages to users about the success or failure of their actions.

## Explanation of Features:

### User Authentication:
1. The application allows users to sign up by providing an email address, username, and password.
2. Passwords are securely hashed using bcrypt before storing them in the database.
3. Users can log in using their email address and password.
4. Flask-Login is used to manage user sessions and provide login functionality.
### Post Creation:
1. Authenticated users can create new posts by entering text in a text area and submitting the form.
2. When a new post is created, it is associated with the user who created it.
### Post Deletion:
1. Users can delete their posts by clicking on a delete button next to each post.
2. Only the user who created the post can delete it.
### Flash Messages:
1. Flash messages are used to provide feedback to users after performing actions such as logging in, signing up, or creating/deleting posts.
2. Flash messages are displayed to the user on the corresponding pages.

## Installation & Deployment:
### To run this project locally, follow these steps:

1. Clone the repository from GitHub.
2. Install the required dependencies listed in the requirements.txt file using pip.
3. Set up a virtual environment to isolate the project dependencies.
4. Initialize the SQLite database by running python app.py or flask run.
5. Access the application in your web browser at http://localhost:8080.
   
### For deployment:

1. Set up a production environment (e.g., a cloud server or a web hosting service).
2. Configure your server environment to meet the project's requirements (e.g., installing Python, setting up a database).
3. Configure your web server (e.g., Nginx or Apache) to serve the Flask application using a WSGI server (e.g., Gunicorn).
4. Set up a domain name and configure DNS settings to point to your server.
5. Secure your application by using HTTPS, configuring firewalls, and following best practices for server security.

## Tools/Technology Used:

1. Flask: Micro web framework for Python used for building web applications.
2. SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for Python used for database management.
3. Flask-Login: Flask extension is used for user session management and authentication.
4. bcrypt: Password hashing library for Python used for securely hashing passwords.
5. SQLite: Lightweight relational database management system used for storing user data and posts.
6. HTML/CSS: Markup and styling languages used for building the user interface.
7. Jinja2: Template engine for Python used for generating HTML content dynamically in Flask applications.
8. Git/GitHub: Version control system and platform for collaborative software development used for managing the project's source code.
