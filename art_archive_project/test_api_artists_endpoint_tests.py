import unittest
from random import randint

from flask.ext.testing import TestCase
from api import app, db
from api.images.models import Image
from api.artists.models import Artist


class APIArtistsEndpointTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            'mysql://root@localhost/test_art_archive'

        return app

    def setUp(self):
        db.create_all()

        for i in range(randint(1000, 2000)):
            artist = Artist(
                name="Test name{}".format(i),
                birth_year=1000,
                death_year=2000,
                country="Test Country",
                genre="Test genre",
            )
            db.session.add(artist)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_artists_endpoint_shows_entire_list(self):
        response = self.client.get("/artists/")
        self.assertEqual(len(response.json['data']), len(Artist.query.all()))

    def test_artists_endpoint_shows_desired_number_of_items(self):
        count = randint(1, len(Artist.query.all()))
        response = self.client.get("/artists/?count={}".format(count))
        self.assertEqual(len(response.json['data']), count)

    def test_artists_endpoint_shows_list_in_asc_order(self):
        response = self.client.get("/artists/?order=asc")
        in_order = True
        prev = 0

        for datum in response.json['data']:
            in_order = in_order and datum['id'] > prev
            prev = datum['id']

        self.assertTrue(in_order)

    def test_artists_endpoint_shows_list_in_desc_order(self):
        response = self.client.get("/artists/?order=desc")
        in_order = True
        # TestDB has at max 2000 items
        prev = 10000

        for datum in response.json['data']:
            in_order = in_order and datum['id'] < prev
            prev = datum['id']

        self.assertTrue(in_order)

if __name__ == '__main__':
    unittest.main()
