# import json
# from unittest import TestCase


# from app import create_app


# class TestOrders(TestCase):
#     def setUp(self):
#         self.app = create_app("testing")
#         self.client = self.app.test_client()
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         self.order_data = {
#             "name": "Burger",
#             "description": "Beef burger",
#             "price": 60
#         }

#     def test_place_new_order(self):
#         ''' Test to place an order '''

#         response = self.client.post(
#             "/api/v2/user/orders",
#             headers={"content-type": "application/json"}
#         )

#         response_data = json.loads(response.data.decode('utf-8'))

#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response_data['message'], "Order placed")

#     def test_destination(self):
#         ''' Test to place an order '''
#         data = {
#             "destination": " ",
#              "ordered_by": "Salma"
#         }

#         response = self.client.post(
#             "/api/v1/orders",
#             data=json.dumps(data),
#             headers={"content-type": "application/json"}
#         )

#         response_data = json.loads(response.data.decode('utf-8'))

#         self.assertTrue(response_data['message'], "Enter valid destination")

#     def test_name(self):
#         ''' Test to place an order '''
#         data = {
#              "destination": "Kasarani",
#              "name": " "
#         }

#         response = self.client.post(
#             "/api/v1/orders",
#             data=json.dumps(data),
#             headers={"content-type": "application/json"}
#         )

#         response_data = json.loads(response.data.decode('utf-8'))

#         self.assertTrue(response_data['message'],
#                         "Enter valid name")

#     def test_get_all_orders(self):
#         ''' Test to get all orders '''

#         response = self.client.get(
#              "/api/v2/orders", content_type='application/json')

#         self.assertEqual(response.content_type, 'application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertNotEqual(response.status_code, 404)

#     def test_get_menu(self):
#         ''' Test to get all orders '''

#         response = self.client.get(
#              "/api/v2/menu", content_type='application/json')

#         self.assertEqual(response.content_type, 'application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertNotEqual(response.status_code, 404)
