import unittest

from flask.ext.testing import TestCase
from api import app, db
from api.images.models import Image
from api.artists.models import Artist


class APIArtistsImagesModelsTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            'mysql://root@localhost/test_art_archive'

        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_artist_has_images(self):
        artist = Artist(
            name="Test name",
            birth_year=1000,
            death_year=2000,
            country="Test Country",
            genre="Test genre",
        )

        image = Image(
            title="Test title",
            image_url="testurl",
            artist=artist,
            year=1000,
            description="Test Description",
        )
        db.session.add(artist)
        db.session.add(image)
        db.session.commit()

        self.assertEqual(artist.images.first().title, image.title)

    def test_images_has_artist(self):
        artist = Artist(
            name="Test name",
            birth_year=1000,
            death_year=2000,
            country="Test Country",
            genre="Test genre",
        )

        image = Image(
            title="Test title",
            image_url="testurl",
            artist=artist,
            year=1000,
            description="Test Description",
        )
        db.session.add(artist)
        db.session.add(image)
        db.session.commit()

        self.assertEqual(image.artist.name, artist.name)


if __name__ == '__main__':
    unittest.main()
