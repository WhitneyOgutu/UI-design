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
        self.assertEqual(result["message"], "You are successfully logged in")

    def test_logout_user(self):
        response = self.dummy_browser.post(
            'api/auth/login',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self.user_data))
        token = json.loads(response.data.decode())['token']
        response = self.dummy_browser.post(
            'api/auth/logout',
            headers={'Content-Type': 'application/json', 'Authorization': 'Bearer '+ token},
        data=json.dumps(self.user_data))
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "You are successfully logged out")

    def test_create_business(self):
        response = self.dummy_browser.post(
            'api/register/business',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self.business_data))
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Business created successfully")
        
   