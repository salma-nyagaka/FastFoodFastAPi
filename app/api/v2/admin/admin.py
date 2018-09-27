from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required


from utils.validators import Validators
from ..model import FoodMenu, FoodOrder


class PlaceNewMenu(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('description', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('price', type=int, required=True,
                        help="This field cannot be left blank")

    def post(self):
        ''' place new menu'''
        data = PlaceNewMenu.parser.parse_args()
        name = data['name']
        description = data['description']
        price = data['price']

        if not Validators().valid_food_name(name):
            return {'message': 'Enter valid name'}, 400
        if not Validators().valid_food_description(description):
            return {'message': 'Enter valid de'}, 400


        menu = FoodMenu(name=name, description=description, price=price)

        menu.add()
        return {"message": "Food order placed"}, 201


class AllMenu(Resource):

    def get(self):
        ''' get all menu '''

        menu = FoodMenu()
        if menu.get_all():
            return {'Menus': [menu.serialize() for menu
                              in menu.get_all()]}, 200
        return {'message': "Not found"}, 404


class SpecificMenu(Resource):

    def delete(self, id):
        ''' Delete a specific menu '''

        menu = FoodMenu().get_by_id(id)
        if menu:
            menu.delete(id)
            return {'message': "Deleted"}, 200
        return {'message': "Not found"}, 404



class AllOrders(Resource):

    def get(self):
        ''' get all food orders '''

        foodorder = FoodOrder()
        
        if foodorder.get_all():
            return {'Food Orders': [foodorder.serialize() for foodorder
                            in foodorder.get_all()]}, 200
        return {'message': "Not found"}, 404



class SpecificOrder(Resource):

    def get(self, id):
        ''' get a specific menu '''

        order = FoodOrder().get_id(id)

        if order:
            return {"Menu": order.serialize()}, 200
        return {'message': "Not found"}, 404



class Accept(Resource):

    def put(self, id):
        ''' Update the status to accept '''
        order = FoodOrder().get_id(id)

        if order:
            if order.status == "Pending":
                order.status = "Accepted"
                return {'message': 'Order accepted'}, 200
        return {'message': "Not found"}


class Complete(Resource):

    def put(self, id):
        ''' Update the status of an order to completed '''
        order = FoodOrder().get_id(id)
        if order:

            if order.status == "Pending":
                order.status = "Completed"

                return {'message': 'Order completed'}, 200
        return {'message': "Not found"}


class Decline(Resource):

    def put(self, id):
        ''' Update the status of an order '''
        order = FoodOrder().get_id(id)
        if order:
            if order.status == "Pending":
                order.status = "Declined"

                return {'message': 'Order Declined'}, 200
        return {'message': "Not found"}

