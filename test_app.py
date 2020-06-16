import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actor, Movie

assistant_token = "Bearer {}".format(os.environ.get('ASSISTANT_TOKEN'))
director_token = "Bearer {}".format(os.environ.get('DIRECTOR_TOKEN'))
producer_token = "Bearer {}".format(os.environ.get('PRODUCER_TOKEN'))


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the Casting Agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "app_test"
        self.database_path = "postgresql://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_actor = {
          'name': 'RAWAN',
          'age': 24,
          'gender': 'Female'
        }

        self.edit_actor = {
          'name': 'Rawan',
          'age': 26,
          'gender': 'Female'
        }

        self.new_movie = {
          'title': 'Frozen',
          'release_date': '2017-7-11 05:00'
        }

        self.edit_movie = {
          'title': 'Howel castle',
          'release_date': '2009-7-11 6:00'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

     # expected success behavior

    def test_get_actors(self):
        res = self.client().get(
            '/actors', headers={"Authorization": assistant_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['actors_data'])

    def test_get_movies(self):
        res = self.client().get(
            '/movies', headers={"Authorization": assistant_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(data['movies_data'])

    def test_create_actor(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers={"Authorization": director_token})
        data = json.loads(res.data)

        self.assertTrue(data['success'])
        self.assertTrue(data['actors'])

    def test_create_movies(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers={"Authorization": producer_token})
        data = json.loads(res.data)

        self.assertTrue(data['success'])
        self.assertTrue(data['movies'])

    def test_edit_actors(self):
        res = self.client().patch('/actors/2', json=self.edit_actor,
                                  headers={"Authorization":  director_token})
        data = json.loads(res.data)

        self.assertTrue(data['success'])
        self.assertTrue(data['actors'])

    def test_edit_movies(self):
        res = self.client().patch('/movies/3', json=self.edit_movie,
                                  headers={"Authorization": producer_token})
        data = json.loads(res.data)

        self.assertTrue(data['success'])
        self.assertTrue(data['movies'])

    def test_delete_actors(self):

        res = self.client().delete(
            '/actors/1', headers={"Authorization": director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['delete'], '1')

    def test_delete_movies(self):

        res = self.client().delete(
            '/movies/2', headers={"Authorization": (producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['delete'], '2')

    #  Error behavior tests

    def test_401_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_401_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_403_create_actors(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers={"Authorization": (assistant_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])

    def test_403_create_movies(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers={"Authorization": director_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])

    def test_404_edit_actors(self):
        res = self.client().patch('/actors/99', json=self.edit_actor,
                                  headers={"Authorization": (producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_404_edit_movies(self):
        res = self.client().patch('/movies/99', json=self.edit_movie,
                                  headers={"Authorization": (producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_403_delete_actors(self):
        res = self.client().delete(
            '/actors/1', headers={"Authorization": (assistant_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])

    def test_404_delete_movies(self):
        res = self.client().delete(
            '/movies/1000', headers={"Authorization": (producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
