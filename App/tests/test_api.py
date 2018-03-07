import unittest

import json

from App.app import create_app


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('Testing')
        self.dummy_browser = self.app.test_client()
        
        self.user_data = {"firstname": "Whitney", "username": "Budhi", "password": "2323"}


    def test_create_user(self):
        response = self.dummy_browser.post(
            'api/auth/register',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self.user_data))
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "User created successfully")
        