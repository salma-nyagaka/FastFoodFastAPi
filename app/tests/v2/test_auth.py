import json
from unittest import TestCase


from app import create_app


class TestOrders(TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def signup(self):
        ''' Function for sign up '''
        data = {
            'username': 'Salma123',
            'email': 'salma@gmail.com',
            'password': 'Password123',
            'confirm_password': 'Password123'
        }

        response = self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        return response

    def login(self):
        ''' Function for login '''
        data = {
            'username': 'Salma123',
            'password': 'Password123'
        }

        response = self.client.post(
            "/api/v2/auth/login",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        return response
  
    def test_signup(self):
        ''' Test for user signup '''
        response = self.signup()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['message'], "successfully created a new account")

    def test_login(self):
        ''' Test for user login '''
        self.signup()

        response = self.login()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], "Successfully login in Salma123")

   