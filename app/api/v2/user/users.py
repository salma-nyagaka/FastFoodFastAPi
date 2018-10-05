'''import modules to create users endpoints'''
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.v2.model import FoodOrder, FoodMenu
from utils.validators import Validators


class PlaceOrder(Resource):
    ''' place a new food order'''
    parser = reqparse.RequestParser()
    parser.add_argument('destination', type=str, required=True,
                        help="This field cannot be left blank")
    @jwt_required
    def post(self, id):
        ''' place new order'''

        menu = FoodMenu().get_by_id(id)

        if not menu:
            return {"message": "Food does not exist"}, 404

        current_user = get_jwt_identity()['username']
        data = PlaceOrder.parser.parse_args()

        destination = data['destination']

        if not Validators().valid_destination(destination):
            return {'message': 'Enter valid destination'}, 400

        order = FoodOrder(current_user, menu.name, destination)

        order.add()
        myorder = FoodOrder().get_by_destination(destination)
        return {"message": "Food menu created", "meal":myorder.serialize()}, 201


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
