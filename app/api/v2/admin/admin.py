from flask_restful import Resource, reqparse
from flask_jwt_extended import (jwt_required, get_jwt_identity)


from utils.validators import Validators
from app.api.v2.model import FoodOrder, FoodMenu


class PlaceNewMenu(Resource):
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
        current_user = get_jwt_identity()
        print(current_user)

        if(current_user["is_admin"]):
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
        return {"message": "You are not authorized to create a new menu"}, 403


class AllMenu(Resource):

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

    @jwt_required
    def delete(self, id):
        ''' Delete a specific menu '''

        menu = FoodMenu().get_by_id(id)
        if menu:
            menu.delete(id)
            return {'message': "Successfully Deleted"}, 200
        return {'message': "Menu item not found"}

    @jwt_required
    def get(self, id):
        menu = FoodMenu().get_by_id(id)

        if menu:
            return {"Menu": menu.serialize(),
                    "message": "These are the available food menu"}, 200
        return {'message': "Not found"}, 404


class AllUserOrders(Resource):

    @jwt_required
    def get(self):
        ''' get all food orders '''

        foodorder = FoodOrder()
        if foodorder.get_all():
            return {'Food Orders': [foodorder.serialize() for foodorder
                    in foodorder.get_all()]}, 200
        return {'message': "Not found"}, 404


class GetSpecificOrder(Resource):

    @jwt_required
    def get(self, id):
        ''' get a specific menu '''

        order = FoodOrder().get_by_id(id)

        if order:
            return {"Menu": order.serialize()}, 200
        return {'message': "Not found"}, 404


class AcceptOrder(Resource):
    

    @jwt_required
    def put(self, id):
        ''' Update the status to accept '''
        current_user = get_jwt_identity()
        print(current_user)

        if(current_user["is_admin"]):
            order = FoodOrder().get_by_id(id)
            if not order:
                return {'message': "Not found"}, 404
            if order.status != "pending":
                return {'message': 'Order is {}'.format(order.status)}

            order.accept_order(id)
            return {'message': 'Order accepted'}, 200
        return {"message": "You are not authorized to mark order as accepted"}, 403


class CompleteOrder(Resource):

    @jwt_required
    def put(self, id):
        ''' Update the status of an order to completed '''
        current_user = get_jwt_identity()
        print(current_user)

        if(current_user["is_admin"]):
            order = FoodOrder().get_by_id(id)

            if not order:
                return {'message': "Not found"}, 404
            if order.status != "accepted":
                return {'message': 'Order  is{}'.format(order.status)}

            order.complete_accepted_order(id)
            return {'message': 'Order completed'}, 200
        return {"message": "You are not authorized to mark order as completed"}, 403


class DeclineOrder(Resource):

    @jwt_required
    def put(self, id):
        ''' Update the status of an order '''
        current_user = get_jwt_identity()
        print(current_user)
        
        if(current_user["is_admin"]):
            order = FoodOrder().get_by_id(id)
            if not order:
                return {'message': "Not found"}, 404
            if order.status != "pending":
                return {'message': 'Order  is{}'.format(order.status)}
            order.complete_accepted_order(id)
            return {'message': 'Order declined'}, 200
        return {"message": "You are not authorized to decline an order"}, 403


