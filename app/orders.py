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

    


    def get(self):
        ''' get all orders '''
        return {'orders': [order.serialize() for order in orders]}, 200

