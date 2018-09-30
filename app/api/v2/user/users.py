from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.api.v2.model import FoodOrder, FoodMenu
from utils.validators import Validators


class PlaceOrder(Resource):
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
        return {"message": "Order has been placed"}, 201


class GetOrders(Resource):

    @jwt_required
    def get(self):
        ''' get all orders '''

        orders = FoodOrder().get_all()
        if orders:
            return {'Orders': [order.serialize() for order
                              in orders]}, 200
        return {'message': "Not found"}, 404
