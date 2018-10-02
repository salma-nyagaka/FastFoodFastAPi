
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
        """ test for signing up"""
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
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_data['message'], "successfully created a new account", 201)

    def login(self):
        """ test for loggin in """
        login_data = {
            "username": "salma",
            "password": "salma123"
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

    def test_place_an_order(self):
        '''Test for a user to place an order'''
        token = self.get_token()


        response = self.client.get(
            "/api/v2/users/menu/1/orders",
            headers={"content-type": "application/json",
                     'Authorization': 'Bearer {}'.format(token)
                 }
         )

        return(response.status_code, 201)

   
    def test_all_menu(self):
        '''Test get all menu'''

        token = self.get_token()
        response = self.client.post(
            "/api/v2/menu",
            data=json.dumps(self.order_data),
            headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(token)
                }
        )
        response = self.client.get(
            "/api/v2/allmenu",
            data=json.dumps(self.order_data),
            headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(token)
                }
        )

    
    def tearDown(self):
        drop()