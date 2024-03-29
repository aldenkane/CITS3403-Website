## CITS3403-Website
Delany Bolton and Alden Kane's website for University of Western Australia's CITS3403: Agile Web Development. This asks users the question: "Which car do you want to drive across the Nullarbor?" The social choice mechanism used for voting is first-past-the-post voting, in which the option with the most votes wins the poll.

## Authors
  * Delany Bolton (22640583)
  * Alden Kane (22640752)

A git log, showing commits from both partners, can be found in LOG.txt. While Alden has more total commits, both partners agree that work was equitably distributed.

## Architecture

This project uses HTML5, CSS, Javascript, and the Flask framework to build a functional polling web application.

The core flask application for this project is CITS3403-Website.py

There are three primary views in this application:
  1. Anonymous View: This view allows users to view the homepage and the results of the poll. From this view, users can log in. However, users cannot vote from this view. The voting page is hidden, and users are required to log in before voting.
  2. User View: This view has all of the functionality of the Anonymous View, except users can now vote on polls. They can also log out of their account and return to the Anonymous View from here. A sample account to log into this view is username = "alden" and password = "alden"
  3. Admin View: This view has all of the functionality of the User View and is only available for the username = "admin." This view can access the administrator workspace, found at localhost:5000/admin. The admin can add and delete users, and access other databases. A sample account to log into this view is username = "admin" and password = "admin"

This application also has the following notable features:
  * An accounts feature, allowing for regular and admin users. This was implemented using Flask.
  * A polling feature, which was implemented using HTML5 forms and Flask to write votes to data.txt, then construct results based off of the response stored in that file.
  * A navbar, that allows users to move between the Home, Vote, and Results page. This feature highlights the current page. This was implemented using Bootstrap, HTML5, and CSS.
  * A footer with the current date and time. This was implemented using Javascript, HTML5, and CSS.

This application is designed to be sleek, intuitive, and easy to use.

## Launching this Application

Python3 and sqlite3 need to be installed.

All needed dependencies are listed below and also listed in requirements.txt:
  * alembic==1.0.10
  * Click==7.0
  * Flask==1.0.2
  * Flask-Admin==1.5.3
  * Flask-Login==0.4.1
  * Flask-Migrate==2.4.0
  * Flask-SQLAlchemy==2.4.0
  * Flask-WTF==0.14.2
  * itsdangerous==1.1.0
  * Jinja2==2.10.1
  * Mako==1.0.10
  * MarkupSafe==1.1.1
  * python-dateutil==2.8.0
  * python-dotenv==0.10.2
  * python-editor==1.0.4
  * six==1.12.0
  * SQLAlchemy==1.3.3
  * Werkzeug==0.15.2
  * WTForms==2.2.1

To launch this application on localhost, install all of these dependencies then navigate to the folder "CITS3403-Website" found in the project submission. Do so in a virtual environment. All of the source code for the flask application is found in the "CITS3403-Website" folder.

To run a virtual environment, run the following commands:

```bash
virtualenv venv
source venv/bin/activate
```

To run a virtual environment on Windows, run the following commands:

```bash
virtualenv venv
venv\Scripts\activate
```

Once in a virtual environment, install python3 and sqlite3, along with all other dependencies.

If no database is found with the module, build the database using:

```bash
python -m flask db init
```

However, this application ships with a test database, app.db. No database needs to be built.

To launch the application, run the following command while in your virtual environment:

```bash
python -m flask run
```

This will host the application on localhost. The following (with a slightly different link) should appear:

```bash
* Serving Flask app "CITS3403-Website.py"
* Environment: production
  WARNING: Do not use the development server in a production environment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Unit Testing and System/UserTesting

Unit tests can be performed by running ```python tests.py``` in the command line.

If the unit tests work, the following should appear in the command line:
```bash
test_password_hashing (__main__.UserModelCase) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.431s

OK
```

The following unit tests have been including in the file tests.py:
  * test_password_hashing tests the password hashing feature to ensure only valid passwords are accepted

The following system/user test sequences can be run to ensure the operability and function of this application:

Verify Anonymous User View:
  1. While not logged into any accounts, click on the "Vote" link in the navbar
  2. User should be prompted for Sign In. They cannot vote unless logged in

Verify Admin User View:
  1. While logged into username "admin", password "admin", navigate to localhost:5000/admin via editing the url bar
  2. User should be directed to the Admin dashboard if and only if they are logged in "admin"
  3. Can try step (1) for anonymous and other users to verify validation of admin user

Verify Account Creation:
  1. While in the anonymous user view, click on "Register" in the upper right hand corner
  2. Register a new account and proceed to log in after
  3. Voting on a poll, on the "Vote" page, should now be available

Verify Account Validation:
  1. While in the anonymous user view, click on "Register" in the upper right hand corner
  2. Register a new account with a known username (e.g. "alden")
  3. Will get "[Please user a different username.]" error in red

Verify Account Validation, Part 2:
  1. While in the anonymous user view, click on "Register" in the upper right hand corner
  2. Register a new account, with "Password" and "Repeat Password" fields not matching
  3. Will get "[Field must be equal to password.]" error in red

Verify Account Validation, Part 3:
  1. While in the anonymous user view, click on "Login" in the upper right hand corner
  2. Attempt to login to a known account (e.g. "alden") with the wrong password (e.g. "foo")
  3. User will not log in

Verify Admin User View:
  1. While logged into username "admin", password "admin", navigate to localhost:5000/admin via editing the url bar
  2. User should be directed to the Admin dashboard if and only if they are logged in "admin"
  3. Delete a user
  4. Navigate back to home page
  5. Log out of "admin"
  6. Attempt to log in to deleted account
  7. User will not log in

## References and Acknowledgements

The following tutorials were integral in learning Flask and building this application. Most modules were from the CITS3403 Laboratory Work. Comments are provided throughout the application indicating that a tutorial was followed to construct functions and features.

  * Miguel Grindberg's "Flask Mega-Tutorial, Chapters 1-8". Found at: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world. Reference for this in source code is ```#Miguel Grindberg's "Flask Mega-Tutorial, Chapters 1-8"```
  * Daniel Osaetin's (Danidee's) "Flask by Example, Parts 1-7". Found at: https://danidee10.github.io/2016/11/14/flask-by-example-7.html. Reference for this in source code is ```#Daniel Osaetin's "Flask by Example, Parts 1-7"```
  * Gabor Szabo's "A polling station using Flask. Found at: https://code-maven.com/a-polling-station-with-flask. Reference for this in source code is ```#Gabor Szabo's "A polling station using Flask"```

This application uses Bootstrap, under an MIT License.

The following external libraries were used in building this application, under an MIT License:
  * alembic==1.0.10
  * Click==7.0
  * Flask==1.0.2
  * Flask-Admin==1.5.3
  * Flask-Login==0.4.1
  * Flask-Migrate==2.4.0
  * Flask-SQLAlchemy==2.4.0
  * Flask-WTF==0.14.2
  * itsdangerous==1.1.0
  * Jinja2==2.10.1
  * Mako==1.0.10
  * MarkupSafe==1.1.1
  * python-dateutil==2.8.0
  * python-dotenv==0.10.2
  * python-editor==1.0.4
  * six==1.12.0
  * SQLAlchemy==1.3.3
  * Werkzeug==0.15.2
  * WTForms==2.2.1

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
