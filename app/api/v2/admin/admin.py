''' module imports'''
from flask_restful import Resource, reqparse
from flask_jwt_extended import (jwt_required, get_jwt_identity)


from utils.validators import Validators
from app.api.v2.model import FoodOrder, FoodMenu


class PlaceNewMenu(Resource):
    '''place a new food menu item'''
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('description', type=str, required=True,
                        help="This field cannot be left blank")

    parser.add_argument('price', type=int, required=True,
                        help="Enter valid price")

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
        meal = FoodMenu().get_by_name(name)
        return {"message": "Food menu created", "meal":meal.serialize()}, 201


class AllMenu(Resource):
    '''get all menu'''
    @jwt_required
    def get(self):
        """ Get all food items """
        data = FoodMenu().get_all()

        food_menus = []

        if data:
            for food_menu in data:
                food_menus.append(food_menu.serialize())

            return {"Food menu": food_menus,
                    "message": "These are the available food items"}, 200

        return {"message": "No food items available for now"}, 404


class SpecificMenu(Resource):
    '''get specific menu'''
    @jwt_required
    def delete(self, _id):
        ''' Delete a specific menu '''

        menu = FoodMenu().get_by_id(id)
        if menu:
            menu.delete(id)
            return {'message': "Successfully Deleted"}, 200
        return {'message': "Menu item not found"}

    @jwt_required
    def get(self, _id):
        menu = FoodMenu().get_by_id(id)

        if menu:
            return {"Menu": menu.serialize(),
                    "message": "These are the available food menu"}, 200
        return {'message': "Not found"}, 404


class AllUserOrders(Resource):
    '''get all the orders made by users'''
    @jwt_required
    def get(self):
        ''' get all food orders '''

        foodorder = FoodOrder()
        if foodorder.get_all():
            return {'Food Orders': [foodorder.serialize() for foodorder
                                    in foodorder.get_all()]}, 200
        return {'message': "Not found"}, 404


class GetSpecificOrder(Resource):
    '''get a specific user order'''
    @jwt_required
    def get(self, _id):
        ''' get a specific order '''

        order = FoodOrder().get_by_id(id)

        if order:
            return {"Menu": order.serialize()}, 200
        return {'message': "Not found"}, 404


class AcceptOrder(Resource):
    '''update status'''
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
    '''update order status'''
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


class UpdateStatus(Resource):
    '''upodate order status'''
    parser = reqparse.RequestParser()
    parser.add_argument('status', type=str, required=True,
                        help="Enter valid status")
    @jwt_required
    def put(self, id):
        '''update status to accept, decline, complete'''
        data = UpdateStatus.parser.parse_args()
        order = FoodOrder().get_by_id(id)
        status = data['status']

        if order:
            order.status = data['status']
            return{"order":  order.serialize()}, 201
        
        return{'message': "Order not found"}


        



