'''import modules to create users endpoints'''
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Flask, request


from app.api.v2.model import FoodOrder, FoodMenu
from utils.validators import Validators


class PlaceOrder(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True,
                        help="This field cannot be left blank")

 
    @jwt_required
    def post(self):
        '''post an order by the user'''

        data = PlaceOrder.parser.parse_args()

        
        current_user = get_jwt_identity()['username']
        name = data['name']
       

        meal_item = FoodMenu().get_by_name(name)
        
        if not meal_item:
            return {"message": "Food not found"}, 404

        order = FoodOrder(username=current_user, name=meal_item.name, description=meal_item.description,
                      price=meal_item.price)
        order.add()

        return {"message": "order placed sucessfully"}, 201 


class GetOrders(Resource):
    '''get a history of orders'''
    @jwt_required
    def get(self):
        ''' get all orders '''
        current_user = get_jwt_identity()['username']

        orders = FoodOrder().get_all_orders_by_username(current_user)
        if orders:
            return {'Orders': [order.serialize() for order
                               in orders]}, 200
        return {'message': "Not found"}, 404
