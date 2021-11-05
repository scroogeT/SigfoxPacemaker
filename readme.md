# Sigfox Pacemaker

## How to use

1. Download & install Python 3.9 & create a virtual environment (optional)
2. Open project root directory inside your terminal
3. run `pip install -r requirements.txt` to install project requirements
4. run `python manage.py runserver` to run the project's development server
5. Open project in browser and login with the credentials; username: `tester` & password: `tester123`
6. you may also explore the Swagger API doc on `http://127.0.0.1:8000/swagger` or import `http://127.0.0.1:8000/swagger.json` into an API client like POSTMAN or INSOMNIA

## How To add new Device readings

1. Send the sigfox payload to the endpoint `http://127.0.0.1:8000/sigfox-message/` or put the payload in Swagger playground
2. if the object is valid you can go to homepage to view all the entries made into the database

### The database schema can be inspected using any SQLite client and the database file is located in the project's root directory as ``db.sqlite3``