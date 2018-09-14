from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from .model import FoodOrder, orders
from utils.validators import Validators

class PlaceNewOrder(Resource):
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


class SpecificOrder(Resource):
    def delete(self, id):
        ''' Delete a specific order '''
        order = FoodOrder().get_id(id)

        if order:
            orders.remove(order)
            return {'message':"Deleted"}, 200

        return {'message':"Not found"}, 404
        
       


