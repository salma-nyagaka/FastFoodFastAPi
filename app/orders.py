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



class Order(Resource):
    
    def get(self, id):
        ''' get a specific order '''
        
        order = FoodOrder().get_by_id(id)

        if order:
            return {"order":order.serialize()}
        
        return {'message':"Not found"}, 404


   

