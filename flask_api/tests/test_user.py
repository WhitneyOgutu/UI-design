import unittest

from flask import Flask
from app.user import UserCollection

class TestUser(unittest.TestCase):
    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_create_user(self):
        user = UserCollection()
        response = user.post("Ben", "Maina", "maina@gmail.com", "1223234")
        self.assertEqual(response["message"], "User created successfully")

if __name__ == '__main__':
    unittest.main()