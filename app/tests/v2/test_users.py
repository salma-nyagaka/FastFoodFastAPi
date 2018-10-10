
'''tests for users endpoints'''
import json
from unittest import TestCase
from manage import drop, create, create_admin
from run import app

from app import create_app


class TestOrders(TestCase):
    ''' loads the app all configurations for testings'''
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
    def login_admin(self):
        """ test for loggin in """
        login_data = {
            "username": "Admin",
            "password": "Admin123"
        }

        response = self.client.post(
            "api/v2/auth/login",
            data=json.dumps(login_data),
            headers={'content-type': 'application/json'}
        )
    
        return response

    def get_admin_token(self):
        """ function to get user token """

        response = self.login_admin()
        token = json.loads(response.data.decode('utf-8')).get('token', None)
        return token


    def signup(self):
        """ function for signing up"""
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
        return response

    
    def login(self):
        """ test for signing up"""
        self.signup()

        login_data = {
            "username": "salmaa",
            "password": "passmesome"
        }

        response = self.client.post(
            "api/v2/auth/login",
            data=json.dumps(login_data),
            headers={'content-type': 'application/json'}
        )

        return response


    def get_token(self):
        """ function to get user token """

        response = self.login()
        token = json.loads(response.data.decode('utf-8')).get('token', None)
        return token

    def create_menu(self):
        '''function to create a menu'''
        data = {
            "name": "Burger",
            "description": "Cheese burger",
            "price": 20.0
        }

        response = self.client.post(
            "api/v2/menu",
            data=json.dumps(data),
            headers={
                'content-type': 'application/json',
                'Authorization': 'Bearer {}'.format(self.get_admin_token())
            }
        )

        return response
    
    def test_create_menu(self):
        '''test for creating menu'''
        data = {
            "name": "Burger",
            "description": "Cheese burger",
            "price": 20.0
        }

        response = self.client.post(
            "api/v2/menu",
            data=json.dumps(data),
            headers={
                'content-type': 'application/json',
                'Authorization': 'Bearer {}'.format(self.get_admin_token())
            }
        )

        self.assertEqual(response.status_code, 201)

    
    def test_place_order(self):
        '''test for placing an order'''
        res = self.create_menu()
        print(res.data)
        data = {
            'name': 'Burger'
        }


        response = self.client.post(
            "api/v2/users/orders",
            data=json.dumps(data),
            headers={
                'content-type': 'application/json',
                'Authorization': 'Bearer {}'.format(self.get_token())
            }
        )

        self.assertEqual(response.status_code, 201)


    def tearDown(self):
        with app.app_context():
            drop()
        