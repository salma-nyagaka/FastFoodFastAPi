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


    def login(self):
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

    def user_login(self):
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

        return response

    def get_token(self):
        """ function to get user token """

        response = self.login()
        token = json.loads(response.data.decode('utf-8')).get('token', None)

        return token

    def get_user_token(self):
        """ function to get user token """

        response = self.user_login()
        token = json.loads(response.data.decode('utf-8')).get('token', None)

        return token

    def test_place_new_menu(self):
        ''' Test to place an order '''

        token = self.get_token()
        order_data = {
            "name": "Burger",
            "description": "Beef burger",
            "price": 60
        }

        response = self.client.post(
            "/api/v2/menu",
            data=json.dumps(order_data),
            headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(token)
                }
        )
    
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_data['message'], "Food menu created", 201)
    
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
            "/api/v2/menu",
            data=json.dumps(self.order_data),
            headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(token)
                }
        )

        self.assertEqual(response.status_code, 200)

    def test_empty_menu(self):
        '''Test get all menu'''

        token = self.get_token()

        response = self.client.get(
            "/api/v2/menu",
            data=json.dumps(self.order_data),
            headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(token)
                }
        )

        self.assertEqual(response.status_code, 404)

    def test_get_specific_menu(self):
        '''Test to get a specific menu'''
        token = self.get_token()
        response = self.client.post(
            "/api/v2/menu",
            data=json.dumps(self.order_data),
            headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(token)
                }
        )
        response= self.client.get(
             "/api/v2/menu/1",
             data=json.dumps(self.order_data),
             headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(token)
                }
        )
        self.assertEqual(response.status_code, 200)

    def test_get_specific_order(self):
        '''Test to get a specific menu'''
        user_token = self.get_user_token()
        token = self.get_token()

        self.client.post(
            "/api/v2/menu",
            data=json.dumps(self.order_data),
            headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(token)
                }
        )

        data = {
            'destination': 'Roysa'
        }

        response = self.client.post(
            "/api/v2/users/orders/1",
            data=json.dumps(data),
            headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(user_token)
                }
        )

        response= self.client.get(
             "/api/v2/orders/1",
             data=json.dumps(self.order_data),
             headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(token)
                }
        )
        self.assertEqual(response.status_code, 200)

    def test_get_non_existing_menu(self):
        '''Test to get a specific menu'''
        token = self.get_token()
        response = self.client.post(
            "/api/v2/menu",
            data=json.dumps(self.order_data),
            headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(token)
                }
        )
        response= self.client.get(
             "/api/v2/menu/2331",
             data=json.dumps(self.order_data),
             headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(token)
                }
        )
        self.assertEqual(response.status_code, 404)

    def test_update_order_status(self):
        '''Test to get a specific menu'''
        user_token = self.get_user_token()
        token = self.get_token()

        self.client.post(
            "/api/v2/menu",
            data=json.dumps(self.order_data),
            headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(token)
                }
        )

        data = {
            'destination': 'Roysa'
        }
        
        status = {
            "status": "accept"
        }

        self.client.post(
            "/api/v2/users/orders/1",
            data=json.dumps(data),
            headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(user_token)
                }
        )

        response= self.client.put(
             "/api/v2/update/order/1",
             data=json.dumps(status),
             headers={"content-type": "application/json",
                    'Authorization': 'Bearer {}'.format(token)
                }
        )
        self.assertEqual(response.status_code, 200)

   