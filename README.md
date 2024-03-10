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
