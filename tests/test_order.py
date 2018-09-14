import json
import unittest
from unittest import TestCase
from app import create_app

class TestOrders(TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_place_new_order(self):
        ''' Test place an order '''

        order_data = {
            "name":"Burger",
            "description":"Beef burger",
            "price":60
        }

        response = self.client.post(
            "/api/v1/orders",
            data=json.dumps(order_data),
            headers={"content-type":"application/json"}
        )

        response_data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data['message'], "Food order created")


    def test_get_all_orders(self):
        ''' Test to get all orders '''

        response = self.client.get(
             "/api/v1/orders", content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        print(data)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)


    def test_update_order(self):
        ''' Test to update a specific order '''

        response = self.client.put(
            "/api/v1/orders/2",
            headers={"content-type":"application/json"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_none_existing_order(self):
        ''' Test none existing order'''
        response = self.client.delete(
            "/api/v1/orders/1000",
            headers={"content-type":"application/json"}
        )
        self.assertEqual(response.status_code, 404)

    def test_invalid_food_name(self):
        ''' Test invalid food name '''

        order_data = {
            "name":"***",
            "description":"Sweet empty food",
            "price":20
        }

        response = self.client.post(
            "/api/v1/orders",
            data=json.dumps(order_data),
            headers={"content-type":"application/json"}
        )

        response_data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message'], "Enter valid name")
        self.assertNotEqual(response.status_code, 200)

    def test_invalid_food_description(self):
        ''' Test invalid food description '''

        order_data = {
            "name":"Validfood",
            "description":"****",
            "price":20
        }

        response = self.client.post(
            "/api/v1/orders",
            data=json.dumps(order_data),
            headers={"content-type":"application/json"}
        )

        response_data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message'], "Enter valid food description")
        self.assertNotEqual(response.status_code, 200)
   
        
    