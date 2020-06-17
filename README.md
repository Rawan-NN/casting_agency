# Full Stack Final Project

## Full Stack Casting agency

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

##### setting the user jwts, auth0 credentials
After installing the dependencies,navigate to the project directory and  execute the  following command to set the user jwts, auth0 credentials:
```bash
source setup.sh
```
## Database Setup
With Postgres running, restore a database using the Casting_Agency.psql file provided.in terminal run:
```bash
psql Casting_Agency < Casting_Agency.psql
```

## Running the server

To run the server, execute:

```bash
export FLASK_APP=app          
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

## Authorization
The API uses the Auth0 Role Based Access Control mechanisms for implementing authorization for each endpoint. The following permissions are currently accepted;

- get:actors
- post:actors
- patch:actors
- delete:actors
- get:movies
- post:movies
- patch:movies
- delete:movies

* Roles and their corresponding permissions are listed below:

* Casting Assistant:
get:actors
get:movies

* Casting Director: All the permissions of the Casting Assistant as well as;
post:actors
patch:actors
patch:movies
delete:actors

* Executive Producer: All the permisions of the Casting Director as well as;
post:movies
delete:movies

* Base url: This API is currently hosted on the following url.
 ```bash
  https://casting-agency-app-rawan.herokuapp.com/
  ```
## Endpoints
```bash
GET '/movies'
GET '/actors'
POST '/movies'
POST '/actors'
PATCH '/actors/<id>'
PATCH '/movies/<id>'
DELETE '/movies/<id>'
DELETE '/actors/<id>'
```

1. GET '/movies'
```bash
- Fetches a dictionary of movies 
- Request Arguments: None
- Response:
{
  "movies_data": [
    {
      "id": 3,
      "release_date": "Tue, 11 Jul 2017 05:00:00 GMT",
      "title": "Frozen"
    },
    {
      "id": 2,
      "release_date": "Tue, 11 Jul 2017 05:00:00 GMT",
      "title": "Howel castle"
    }
  ],
  "success": true
}
```
2. GET '/actors'
```bash
- Fetches a dictionary of actors 
- Request Arguments: none
- Response:
{
  "actors_data": [
    {
      "age": 30,
      "gender": "female",
      "id": 2,
      "name": "Reem"
    },
    {
      "age": 30,
      "gender": "female",
      "id": 1,
      "name": "rawan"
    }
  ],
  "success": true
}
```

3. POST '/movies'
```bash
- create new movie 
- Request body:{title:string,release_date:dateTime}
- Response: 
{
  "movies": [
    {
      "id": 3,
      "release_date": "Tue, 11 Jul 2017 05:00:00 GMT",
      "title": "Frozen"
    },
    {
      "id": 2,
      "release_date": "Tue, 11 Jul 2017 05:00:00 GMT",
      "title": "Howel castle"
    },
    {
      "id": 4,
      "release_date": "Sat, 11 Jul 2009 06:00:00 GMT",
      "title": "toy story"
    }
  ],
  "success": true
}
```
4. POST '/actors'
```bash
- create new actor
- Request body:{name:string, age:integer, gender:string}
- Response: 
{
  "actors": [
    {
      "age": 30,
      "gender": "female",
      "id": 2,
      "name": "Reem"
    },
    {
      "age": 30,
      "gender": "female",
      "id": 1,
      "name": "rawan"
    },
    {
      "age": 30,
      "gender": "female",
      "id": 4,
      "name": "lama"
    }
  ],
  "success": true
}
```
5. PATCH '/actors/<id>'
```bash
- edit the actor data
- Request Arguments: actor_id:int
- Request body:  { name: String, age: Integer, gender: String }
- Response:
{
  "actors": [
    {
      "age": 30,
      "gender": "female",
      "id": 2,
      "name": "Reem"
    },
    {
      "age": 30,
      "gender": "female",
      "id": 4,
      "name": "lama"
    },
    {
      "age": 25,
      "gender": "female",
      "id": 1,
      "name": "rawan"
    }
  ],
  "success": true
}
```
6. PATCH '/movies/<id>'
```bash
- edit the movie data
- Request argument: movie_id:int
- Request body: { title: String, release_date: DateTime }
- Response:
{
  "movies": [
    {
      "id": 3,
      "release_date": "Tue, 11 Jul 2017 05:00:00 GMT",
      "title": "Frozen"
    },
    {
      "id": 4,
      "release_date": "Sat, 11 Jul 2009 06:00:00 GMT",
      "title": "toy story"
    },
    {
      "id": 2,
      "release_date": "Tue, 11 Jul 2017 05:00:00 GMT",
      "title": "conan"
    }
  ],
  "success": true
}
```

7. DELETE '/movies/<id>'
```bash
- delete a movie
- Request argument: movie_id:int
- Response: 
{
  "delete": "2",
  "success": true
}
```
8. DELETE '/actors/<id>'
```bash
- delete an actor
- Request argument: actor_id:int
- Response: 
{
  "delete": "2",
  "success": true
}
```
## Error Handling

- Error example:
```bash
{
    "success": False,
    "error": 404,
    "message": "Not found"
}
```
The errors that may occur:

* 400 – bad Request
* 400: Bad Request
* 400: Permissions were not included in the JWT.
* 400: Unable to parse authentication token.
* 400: Unable to parse authentication token.
* 400: Unable to find the appropriate key.
* 401: Authorization header is expected.
* 401: Authorization header must start with "Bearer".
* 401: Token not found.
* 401: Authorization header must be bearer token.
* 401: Authorization malformed.
* 401: Token expired.
* 401: Incorrect claims. Please, check the audience and issuer.
* 403: unauthorized.
* 405 – method not allowed
* 404 – Not found
* 422 – unprocessable

## Testing
To run the tests, run
```
dropdb app_test
createdb app_test
psql app_test < Casting_Agency.psql
python test_app.py
```
