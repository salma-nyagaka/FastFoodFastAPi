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

   


class AcceptOrder(Resource):
    def put(self, id):
        ''' Update the status of an order '''
        order = FoodOrder().get_by_id(id)

        if order:
            if order.status == "Pending":
                order.status = "Accepted"

                return {'message':'Order accepted'}, 200

        return {'message':"Not found"}, 404






