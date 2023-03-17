# Practice Challenge - Camping Fun

Congratulations! You have been hired by Access Camp and for your first job, you
have been tasked with building out a website to log campers with their
activities.

In this repo, there is a Flask application with some features built out. There
is also a fully built React frontend application, so you can test if your API is
working (don't be afraid to use Postman as well).

Your job is to build out the Flask API to add the functionality described in the
deliverables below.

This project is separated into two applications:

- A React frontend, in the `client` directory.
- A Flask backend, in the `server` directory.

All of the features for the React frontend are built out, so you do not need to make any changes there.

---

## Frontend Setup

Let's take a quick tour of what we have so far.

To get started, `cd` into the `client` directory. Then run:

```console
$ npm install
$ npm start
```

Then visit [http://localhost:4000](http://localhost:4000) in the browser to get a sense of the application.

You are not being assessed on React, and you don't have to update any of the React
code; the frontend code is available just so that you can test out the behavior
of your API in a realistic setting.

---

## Backend Setup

In another terminal, run `pipenv install; pipenv shell` to install the
dependencies and enter your virtual environment, then `cd` into the `server`
directory to start running your Python code.

In this directory, you're given a bare-bones template for a Flask API
application. It should look familiar to other Flask labs you've seen and has
all the code set up so you can focus on building out your model and API routes (unless you would prefer to include flask-restful).

You'll be responsible for:

- Creating the models and migrations.
- Setting up the necessary routes to handle requests.
- Performing CRUD actions and validations with SQLAlchemy.
- Sending the necessary JSON data in the responses.

## Instructions

You can run your Flask server from the
`server/` directory with:

```console
$ python app.py
```

## If you would prefer to include Flask Restful complete the following otherwise skip to Models section

This application is using vanilla Flask. If you would like to use flask-restful you can. To setup Flask-restful complete the following steps:

- in the main install flask-restful:

```console
$ pipenv install flask-restful
```

- in the `app.py` file import Api and Resource from flask-restful

```python
from flask_restful import Api, Resource
```

- connect flask-restful to you app

```python
api = Api(app)
```

- remove the routes index route currently setup in `app.py`
- create classes that inherit `Resource` (imported from flask-restful)
- add resources to your api

### Model

You need to create the following relationships:

- A `Camper` has many `Signups`, and has many `Activity`s through `Signup`s
- An `Activity` has many `Signups`, and has many has many `Camper`s through `Signup`s
- A `Signup` belongs to a `Camper` and belongs to a `Activity`

Start by creating the models and migrations for the following database tables:

![domain diagram](https://curriculum-content.s3.amazonaws.com/phase-4/mock-challenge-camping-fun/diagram.png)

## Validations

Add validations to the `Camper` model:

- must have a `name`
- must have an `age` between 8 and 18

Add validations to the `Signup` model:

- must have a `time` between 0 and 23 (referring to the hour of day for the
  activity)

After creating the model and migrations, run the migrations and use the provided
`seed.py` file to seed the database:

```console
$ flask db revision --autogenerate -m'your message'
$ flask db upgrade
$ python seed.py
```

### Routes

Set up the following routes. Make sure to return JSON data in the format
specified along with the appropriate HTTP verb.

### GET /campers

Return JSON data in the format below. **Note**: you should return a JSON
response in this format, without any additional nested data related to each
camper.

```json
[
  {
    "id": 1,
    "name": "Caitlin",
    "age": 8
  },
  {
    "id": 2,
    "name": "Lizzie",
    "age": 9
  }
]
```

### GET /campers/:id

If the `Camper` exists, return JSON data in the format below. **Note**: you will
need to serialize the data for this response differently than for the
`GET /campers` route. Make sure to include an array of activities for each
camper.

```json
{
  "id": 1,
  "name": "Caitlin",
  "age": 8,
  "activities": [
    {
      "id": 1,
      "name": "Archery",
      "difficulty": 2
    },
    {
      "id": 2,
      "name": "Swimming",
      "difficulty": 3
    }
  ]
}
```

If the `Camper` does not exist, return the following JSON data, along with
the appropriate HTTP status code:

```json
{
  "error": "Camper not found"
}
```

### POST /campers

This route should create a new `Camper`. It should accept an object with the
following properties in the body of the request:

```json
{
  "name": "Zoe",
  "age": 11
}
```

If the `Camper` is created successfully, send back a response with the new
`Camper`:

```json
{
  "id": 2,
  "name": "Zoe",
  "age": 11
}
```

If the `Camper` is **not** created successfully, return the following JSON data,
along with the appropriate HTTP status code:

```json
{
  "errors": ["validation errors"]
}
```

### GET /activities

Return JSON data in the format below:

```json
[
  {
    "id": 1,
    "name": "Archery",
    "difficulty": 2
  },
  {
    "id": 2,
    "name": "Swimming",
    "difficulty": 3
  }
]
```

### DELETE /activities/:id

If the `Activity` exists, it should be removed from the database, along with
any `Signup`s that are associated with it (a `Signup` belongs
to an `Activity`, so you need to delete the `Signup`s before the
`Activity` can be deleted).

After deleting the `Activity`, return an _empty_ response body, along with the
appropriate HTTP status code.

If the `Activity` does not exist, return the following JSON data, along with
the appropriate HTTP status code:

```json
{
  "error": "Activity not found"
}
```

### POST /signups

This route should create a new `Signup` that is associated with an
existing `Camper` and `Activity`. It should accept an object with the following
properties in the body of the request:

```json
{
  "time": 9,
  "camper_id": 1,
  "activity_id": 3
}
```

If the `Signup` is created successfully, send back a response with the data
related to the `Activity`:

```json
{
  "id": 1,
  "name": "Archery",
  "difficulty": 2
}
```

If the `Signup` is **not** created successfully, return the following JSON data,
along with the appropriate HTTP status code:

```json
{
  "errors": ["validation errors"]
}
```

---

## Resources

- [Flask - Pallets](https://flask.palletsprojects.com/en/2.2.x/)
- [Cross-Origin Resource Sharing - Mozilla][cors mdn]
- [Flask-CORS][flask-cors]
- [flask.json.jsonify Example Code - Full Stack Python](https://www.fullstackpython.com/flask-json-jsonify-examples.html)
- [SQLAlchemy-serializer - PyPI](https://pypi.org/project/SQLAlchemy-serializer/)

[cors mdn]: https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
[flask-cors]: https://flask-cors.readthedocs.io/en/latest/
