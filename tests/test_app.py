import unittest,json

from WeConnect.app import app


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.dummy_browser = self.app.test_client()
        
        self.user_data = {"firstname": "Whitney", "username": "Budhi", "password": "2323"}
        self.review_data = {"title": "Feedback", "description": "good work"}
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
    

    def test_create_business(self):
        response = self.dummy_browser.post(
            'api/register/business',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self.business_data))
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Business created successfully")

    def test_get_business(self):
        response = self.dummy_browser.get(
            'api/register/business',
            headers={'Content-Type': 'application/json'})
        result = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)    

    def test_create_review(self):
        response = self.dummy_browser.post(
            'api/businesses/review',
            headers={'Content-Type': 'application/json'},
            data=json.dumps(self.review_data))
        result = json.loads(response.data.decode())
        self.assertEqual(result["message"], "Review created successfully")