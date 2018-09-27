from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required


from ..model import FoodOrder, FoodMenu
from utils.validators import Validators


class PlaceNewOrder(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('destination', type=str, required=True,
                        help="This field cannot be left blank")
    
    parser.add_argument('ordered_by', type=str, required=True,
                        help="This field cannot be left blank")
    
    def post(self, id):
        ''' place new menu'''
        data = PlaceNewOrder.parser.parse_args()
        name = data['name']
        destination = data['destination']
        ordered_by = data['ordered_by']

        if not Validators().valid_name(name):
            return {'message': 'Enter valid name'}, 400
        if not Validators().valid_destination(destination):
            return {'message': 'Enter valid destination'}, 400

        menu = FoodMenu().get_by_id(id)

        if not menu:
            return {"message": "Food does not exist"}, 404

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


class AllMenu(Resource):

    def get(self):
        ''' get all menu '''

        menu = FoodMenu()
        if menu.get_all():
            return {'Menus': [menu.serialize() for menu
                              in menu.get_all()]}, 200
        return {'message': "Not found"}, 404