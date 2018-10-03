
import json
from unittest import TestCase
from manage import drop, create, create_admin

from app import create_app


class TestOrders(TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            drop()
            create()
            create_admin()
        self.signup_response = self.signup()
        
    def tearDown(self):
        """Method to clear all test side effects before the next test"""
        with self.app.app_context():
            drop()

    def signup(self):
        """ function for signing up"""
        signup_data = {
            "username": "salma",
            "email": "salma@gmail.com",
            "password": "Password123",
            "confirmpassword": "Password123"
        }

        response = self.client.post(
            "/api/v2/auth/signup",
            data=json.dumps(signup_data),
            headers={'content-type': 'application/json'}
        )
        return response

    def login(self):
        """ function for loggin in """
        login_data = {
            "username": "salma",
            "password": "Password123"
        }

        response = self.client.post(
            "/api/v2/auth/login",
            data=json.dumps(login_data),
            headers={'content-type': 'application/json'}
        )

        return response

    def get_token(self):
        """ function to get user token """

        response = self.login()
        
        token = json.loads(response.data.decode('utf-8')).get('token', None)


        return "Bearer {}".format(token)

    def test_signup(self):
        """ test for signing up"""
        response = self.signup_response
        self.assertEqual(response.status_code, 201)

    def test_place_an_order(self):
        '''Test for a user to place an order'''
        

        token = self.get_token()
        order_data = {
            "destination": "Kabarak",
            
        }
        
        response = self.client.post(
            "/api/v2/users/menu/1/orders",
            data  = json.dumps(order_data),
            headers={"content-type": "application/json",
                     'Authorization': token
                 }
         )

        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_data['message'], "Order has been placed", 404)        
