import unittest

from flask.ext.testing import TestCase
from api import app


class TestAPITestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_response_code_is_200(self):
        response = self.client.get("/test/api/")
        self.assertEqual(response.status_code, 200)

    def test_response_code_is_404(self):
        response = self.client.get("/test/wrong/endpoint")
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
