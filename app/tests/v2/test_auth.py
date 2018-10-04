
import json
from unittest import TestCase
from manage import drop, create, create_admin
from run import app

from app import create_app


class TestOrders(TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            drop()
            create()
            create_admin()
        self.order_data = {
            "name": "Burger",
            "description": "Beef burger",
            "price": 60
        }

        self.user_orders = {
            "destination": "juja",
            "status": "pending",
            "name": "Burger",
            
        }

    def signup(self):
        """ function for signing up"""
        signup_data = {
            "username": "salma123",
            "email": "salma@gmail.com",
            "password": "Password123",
            "confirmpassword": "Password123"
        }

        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(signup_data),
            headers={'content-type': 'application/json'}
        )
        return response


    def test_signup(self):
        """ test for signing up"""
        signup_data = {
            "username": "salmaa",
            "email": "salmaa@email.com",
            "password": "passmesome",
            "confirm_password": "passmesome"
        }

        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(signup_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 201)
    
    def test_password_mismatch(self):
        """ test for signing up"""
        signup_data = {
            "username": "salmaa",
            "email": "salmaa@email.com",
            "password": "passmesome",
            "confirm_password": "passmes123ome"
        }

        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(signup_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
    
    def test_invalid_email(self):
        """ test for signing up"""
        signup_data = {
            "username": "salmaa",
            "email": "salmaaemail.com",
            "password": "passmesome",
            "confirm_password": "passmes123ome"
        }

        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(signup_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)

    
    def test_login(self):
        """ test for signing up"""
        signup_data = {
            "username": "salmaa",
            "email": "salmaa@email.com",
            "password": "passmesome",
            "confirm_password": "passmesome"
        }

        self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(signup_data),
            headers={'content-type': 'application/json'}
        )

        login_data = {
            "username": "salmaa",
            "password": "passmesome"
        }

        response = self.client.post(
            "api/v2/auth/login",
            data=json.dumps(login_data),
            headers={'content-type': 'application/json'}
        )

        print(response.data)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        with app.app_context():
            drop()
        