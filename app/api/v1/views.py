from flask_restful import Resource, reqparse
from flask import Flask, request


from .model import FoodOrder, orders
from utils.validators import Validators


class PlaceNewOrder(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('description', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('price', type=int, required=True,
                        help="This field cannot be left blank")

    def post(self):
        ''' place new order'''
        data = PlaceNewOrder.parser.parse_args()
        name = data['name']
        description = data['description']
        price = data['price']

        if not Validators().valid_food_name(name):
            return {'message': 'Enter valid name'}, 400
        if not Validators().valid_food_description(description):
            return {'message': 'Enter valid food description'}, 400

        order = FoodOrder(name=name, description=description, price=price)

        orders.append(order)
        return {'Order created successfully': [order.serialize()
                for order in orders]}, 201


class AllOrders(Resource):

    def get(self):
        ''' get all orders '''
        if orders:
            return {'These are all the orders': [order.serialize()
                    for order in orders]}, 200
        return {'message': "Not found"}


class SpecificOrder(Resource):

    def get(self, id):
        ''' get a specific order '''

        order = FoodOrder().get_id(id)

        if order:
            return {"Order": order.serialize()}, 200
        return {'message': "Not found"}, 404

    def delete(self, id):
        ''' Delete a specific order '''
        order = FoodOrder().get_id(order_id=id)
        if order:
            orders.remove(order)
            return {'message': "Deleted"}, 200
        return {'message': "Not found"}


class Accept(Resource):

    def put(self, id):
        ''' Update the status to accept '''
        order = FoodOrder().get_id(id)

        if order:
            if order.status == "Pending":
                order.status = "Accepted"
                return {'message': 'Order accepted'}, 200
        return {'message': "Not found"}


class Complete(Resource):

    def put(self, id):
        ''' Update the status of an order to completed '''
        order = FoodOrder().get_id(id)
        if order:

            if order.status == "Pending":
                order.status = "Completed"

                return {'message': 'Order completed'}, 200
        return {'message': "Not found"}


class Decline(Resource):

    def put(self, id):
        ''' Update the status of an order '''
        order = FoodOrder().get_id(id)
        if order:
            if order.status == "Pending":
                order.status = "Declined"

                return {'message': 'Order Declined'}, 200
        return {'message': "Not found"}


class DeclineOrder(Resource):

    def put(self, id):

        '''Decline an order'''

        order = FoodOrder().get_id(id)
        if order:
            if order.status == "Pending":
                order.status = "Declined"
                return {'message': 'Order declined'}, 200
        return {'message': "Not found"}


class GetAcceptedOrders(Resource):

    def get(self):
        '''Get the Orders accepted '''
        if orders:
            return {"Accepted orders": [order.serialize() for order in orders
                                        if order.status == "Accepted"]}, 200
        return {'message': "Not found"}


class CompletedOrders(Resource):

    def get(self):
        ''' Get all orders completed'''
        if orders:
            return {"Completed orders": [order.serialize() for order in orders
                                         if order.status == "Completed"]}, 200
        return {'message': "Not found"}


class DeclinedOrders(Resource):

    def get(self):
        ''' Get all orders deleted'''
        if orders:
            return {"Deleted orders": [order.serialize() for order in orders
                                       if order.status == "Declined"]}, 200
        return {'message': "Not found"}
