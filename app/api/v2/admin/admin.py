''' module imports'''
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from utils.validators import Validators


from app.api.v2.model import FoodOrder, FoodMenu


class PlaceNewMenu(Resource):
    '''class  for posting a new menu'''
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('description', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('price', type=float, required=True,
                        help="This field cannot be left blank")

    @jwt_required
    def post(self):
        ''' place new menu'''
        data = PlaceNewMenu.parser.parse_args()
        name = data['name']
        description = data['description']
        price = data['price']

        if not Validators().valid_food_name(name):
            return {'message': 'Enter valid food name'}, 400
        if not Validators().valid_food_description(description):
            return {'message': 'Enter valid food description'}, 400
        menu = FoodMenu(name=name, description=description, price=price)
        menu.add()
        return {"message": "Food order placed"}, 201


class AllMenu(Resource):
    ''' class for getting all the menu'''

    @jwt_required
    def get(self):
        """ Get all food items """
        food_menus = FoodMenu().get_all()
        if food_menus:
            return {"Food menu": [foodmenu.serialize()
                                  for foodmenu in food_menus]}, 200
        return {"message": "No food items available for now"}, 404


class SpecificMenu(Resource):
    ''' class for getting a specific menu'''

    @jwt_required
    def delete(self, _id):
        ''' Delete a specific menu '''

        menu = FoodMenu().get_by_id(id)
        if menu:
            menu.delete(id)
            return {'message': "Deleted"}, 200
        return {'message': "Not found"}, 404

    @jwt_required
    def get(self, _id):
        ''' get specific menu'''
        menu = FoodMenu().get_by_id(id)

        if menu:
            return {"Menu": menu.serialize()}, 200
        return {'message': "Not found"}, 404


class AllUserOrders(Resource):
    ''' class for getting all the orders from the users'''
    @jwt_required
    def get(self):
        ''' get all food orders '''

        foodorder = FoodOrder()
        if foodorder.get_all():
            return {'Food Orders': [foodorder.serialize() for foodorder
                                    in foodorder.get_all()]}, 200
        return {'message': "Not found"}, 404


class GetSpecificOrder(Resource):
    ''' class for getting a specific user order'''
    @jwt_required
    def get(self, _id):
        ''' get a specific menu '''

        order = FoodOrder().get_by_id(id)

        if order:
            return {"Menu": order.serialize()}, 200
        return {'message': "Not found"}, 404


class AcceptOrder(Resource):
    '''class for updating status to accept'''
    @jwt_required
    def put(self, _id):
        ''' Update the status to accept '''
        order = FoodOrder().get_by_id(id)
        if not order:
            return {'message': "Not found"}, 404
        if order.status != "pending":
            return {'message': 'Order is {}'.format(order.status)}

        order.accept_order(id)
        return {'message': 'Order accepted'}, 200


class CompleteOrder(Resource):
    '''class for updating status to complete'''
    @jwt_required
    def put(self, _id):
        ''' Update the status of an order to completed '''
        order = FoodOrder().get_by_id(id)

        if not order:
            return {'message': "Not found"}, 404
        if order.status != "accepted":
            return {'message': 'Order  is{}'.format(order.status)}

        order.complete_accepted_order(id)
        return {'message': 'Order completed'}, 200


class DeclineOrder(Resource):
    '''class for updating status to decline'''
    @jwt_required
    def put(self, _id):
        ''' Update the status of an order '''
        order = FoodOrder().get_by_id(id)
        if not order:
            return {'message': "Not found"}, 404
        if order.status != "pending":
            return {'message': 'Order  is{}'.format(order.status)}
        order.complete_accepted_order(id)
        return {'message': 'Order declined'}, 200
