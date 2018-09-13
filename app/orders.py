from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from .model import FoodOrder, orders
from utils.validators import Validators


class NewOrder(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
    'name',
    type=str,
    required=True,
    help="This field cannot be left blank"
    )

    parser.add_argument(
    'description',
    type=str,
    required=True,
    help="This field cannot be left blank"
    )

    parser.add_argument(
        'price',
        type=int,
        required=True,
        help="This field cannot be left blank! " 
    )

    def post(self):
    
        data = NewOrder.parser.parse_args()

        name = data['name']
        description = data['description']
        price = data['price']

        if not Validators().valid_food_name(name):
            return {'message': 'Enter valid name'}, 400

        if not Validators().valid_food_description(description):
            return {'message': 'Enter valid food description'}, 400

        order = FoodOrder(name, description, price)

        orders.append(order)
        return {"message":"Food order created"}, 201


    def get(self):
        ''' get all orders '''
        return {'orders': [order.serialize() for order in orders]}, 200


class Order(Resource):
    
    def get(self, id):
        ''' get a specific order '''
        
        order = FoodOrder().get_by_id(id)

        if order:
            return {"order":order.serialize()}
        
        return {'message':"Not found"}, 404


    def delete(self, id):
        ''' Delete a specific order '''

        order = FoodOrder().get_by_id(id)

        if not order:
            return {'message':"Not found"}, 404
        
        orders.remove(order)
        return {'message':"Deleted"}, 200


class AcceptOrder(Resource):
    def put(self, id):
        ''' Update the status of an order '''
        order = FoodOrder().get_by_id(id)

        if order:
            if order.status == "Pending":
                order.status = "Accepted"

                return {'message':'Order accepted'}, 200

        return {'message':"Not found"}, 404






