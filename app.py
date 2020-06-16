import os
import sys
from flask import Flask, request, jsonify, abort, Response
from sqlalchemy import exc
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import  setup_db, Movie, Actor,db_drop_and_create_all
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):

        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type,Authorization,true')

        response.headers.add(
            'Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')

        return response

    #db_drop_and_create_all()

    #  ROUTES

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        
        # get all movies
        movies_data = Movie.query.all()

        # check if it is empty
        if not movies_data:
            abort(404)

        movies = []
        for movie in movies_data:
            movies.append(movie.format())

        # make json response
        return jsonify({
            'success': True,
            'movies_data': movies})

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        actors_data = Actor.query.all()  # get all actors
        # check if it is empty
        if not actors_data:
            abort(404)

        actors = []
        for actor in actors_data:
            actors.append(actor.format())
        # make json response
        return jsonify({
            'success': True,
            'actors_data': actors})

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actor')
    def post_actor(payload):
        try:
            # get the actor attributes
            body = request.get_json()
            print(body)
            new_name = body["name"]
            new_age = body["age"]
            new_gender = body["gender"]
            # check if they are not in the json request
            if not new_name or not new_age or not new_gender:
                abort(422)

            #  create new actor and add it
            actor = Actor(new_name,new_age,new_gender)
            

            actor.insert()
            actors_data = Actor.query.all()

            # get actors
            actors = []
            for a in actors_data:
                actors.append(a.format())

            # make the json response
            return jsonify({
                'success': True,
                'actors': actors})

        except:
            # if the proccess uncompleted because of any issue wil abort 422
            print(sys.exc_info())
            abort(422)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movie')
    def post_movie(payload):
        try:
            # get the Drink attributes
            body = request.get_json()
            new_title = body["title"]
            new_release_date = body["release_date"]

            # check if they are not in the json request
            if not new_title or not new_release_date:
                abort(422)

            #  create new movie and add it
            movie = Movie(new_title,new_release_date)
            

            movie.insert()
            movies_data = Movie.query.all()

            # get movies
            movies = []
            for m in movies_data:
                movies.append(m.format())

            # make the json response
            return jsonify({
                'success': True,
                'movies': movies})

        except:
            # if the proccess uncompleted because of any issue wil abort 422
            print(sys.exc_info())
            abort(422)

    @app.route('/actors/<id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def edit_actor(payload, id):
      
            #  get the actor based on the id
            actor = Actor.query.get(id)

            # check if it is empty
            if not actor:
                abort(404)
            # get the element to be updated and updaye it
            if 'name' in request.json:
                actor.name = request.json['name']
            if 'age' in request.json:
                actor.age = request.json['age']
            if 'gender' in request.json:
                actor.gender = request.json['gender']

            if not 'name' in request.json and not 'age' in request.json and not 'gender' in request.json:
                abort(422) 

            actor.update()
            actors_data = Actor.query.all()
            # get actors
            actors = []
            for a in actors_data:
                actors.append(a.format())

            # make the json response
            return jsonify({
                'success': True,
                'actors': actors})
       
   
    @app.route('/movies/<id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def edit_movie(payload, id):
       
            #  get the movie based on the id
            movie = Movie.query.get(id)

            # check if it is empty
            if not movie:
                abort(404)
            # get the element to be updated and updaye it
            if 'title' in request.json:
                movie.title = request.json['title']
            if 'release_date' in request.json:
                movie.recipe = request.json['release_date']

            if not 'title' in request.json and not 'release_date' in request.json:
                abort(422)
            movie.update()
            movies_data = Movie.query.all()
            # get movies
            movies = []
            for m in movies_data:
                movies.append(m.format())

            # make the json response
            return jsonify({
                'success': True,
                'movies': movies})
       

    @app.route('/movies/<id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(payload, id):

        # delete the movie based on the id
        movie = Movie.query.get(id)

        # check if it is empty
        if not movie:
            abort(404)

        movie.delete()

        #  make the json response
        return jsonify({
            'success': True,
            'delete': id})

    @app.route('/actors/<id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload, id):

        # delete the actor based on the id
        actor = Actor.query.get(id)

        # check if it is empty
        if not actor:
            abort(404)

        actor.delete()

        #  make the json response
        return jsonify({
            'success': True,
            'delete': id})

    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
            }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
            }), 404

    @app.errorhandler(AuthError)
    def Auth_Error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
            }), error.status_code

    return app
app = create_app()

if __name__ == '__main__':
     app.run(host='127.0.0.1', port=5433, debug=True)
