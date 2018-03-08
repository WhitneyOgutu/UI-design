import unittest

import json

from App.app import create_app


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('Testing')
        self.dummy_browser = self.app.test_client()
        
        self.user_data = {"firstname": "Whitney", "username": "Budhi", "password": "2323"}
        self.business_data = {"businessname": "Nakumatt", "description": "blahblahblah", "location": "Nairobi"}


    def test_create_user(self):
        response = self.dummy_browser.post(
            'api/auth/register',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self.user_data))
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "User created successfully")

    def test_login_user(self):
        response = self.dummy_browser.post(
            'api/auth/login',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self.user_data))
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Logged in successfully")



    def test_create_business(self):
        response = self.dummy_browser.post(
            'api/register/business',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self.business_data))
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Business created successfully")
        
    def test_create_review(self):
        response = self.dummy_browser.post(
            'api/register/business',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self.business_data))
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Review created successfully")