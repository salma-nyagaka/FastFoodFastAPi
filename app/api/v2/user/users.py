from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required


from ..model import FoodOrder


class PlaceNewOrder(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('destination', type=str, required=True,
                        help="This field cannot be left blank")
    
    parser.add_argument('ordered_by', type=str, required=True,
                        help="This field cannot be left blank")

    def post(self):
        ''' place new menu'''
        data = PlaceNewOrder.parser.parse_args()
        name = data['name']
        destination = data['destination']
        ordered_by = data['ordered_by']

        order = FoodOrder(name=name, destination=destination, ordered_by=ordered_by)

        order.add()
        return {"message": "Order placed"}, 201


class AllOrders(Resource):

    def get(self):
        ''' get all orders '''

        order = FoodOrder()
        if order.get_all():
            return {'Orders': [order.serialize() for menu
                              in order.get_all()]}, 200
        return {'message': "Not found"}, 404
