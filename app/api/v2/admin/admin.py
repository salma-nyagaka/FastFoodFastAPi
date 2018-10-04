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
        current_user = get_jwt_identity()
        if current_user['is_admin']:
            data = PlaceNewMenu.parser.parse_args()
            name = data['name']
            description = data['description']
            price = data['price']
            

            if not Validators().valid_food(name):
                return {'message': 'Enter valid food name'}, 400
            if not Validators().valid_food(description):
                return {'message': 'Enter valid food description'}, 400
            if FoodMenu().get_by_name(name):
                return {'message': 'This food already exists'}, 409
            menu = FoodMenu(name=name, description=description, price=price)
            menu.add()
            meal = FoodMenu().get_by_name(name)
            return {"message": "Food menu created", "meal":meal.serialize()}, 201
        return {"message": "Authorization required"}, 403


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
    def get(self, id):
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
        current_user = get_jwt_identity()
        if current_user['is_admin']:

            foodorder = FoodOrder()
            if foodorder.get_all():
                return {'Food Orders': [foodorder.serialize() for foodorder
                                        in foodorder.get_all()]}, 200
            return {'message': "Not found"}, 404
        return {"message": "Authorization required"}, 403



class GetSpecificOrder(Resource):
    '''get a specific user order'''
    @jwt_required
    def get(self, id):
        ''' get a specific order '''
        current_user = get_jwt_identity()
        if current_user['is_admin']:
            order = FoodOrder().get_by_id(id)
            if order:
                return {"Menu": order.serialize()}, 200
            return {'message': "Not found"}, 404
        return {"message": "Authorization required"}, 403


class UpdateStatus(Resource):
    '''upodate order status'''
    parser = reqparse.RequestParser()
    parser.add_argument('status', type=str, required=True,
                        help="Enter valid status")
    @jwt_required
    def put(self, id):
        '''update status to accept, decline, complete'''
        current_user = get_jwt_identity()
        if current_user['is_admin']:
            data = UpdateStatus.parser.parse_args()
            order = FoodOrder().get_by_id(id)

            if order:
                order.status = data['status']
                return{"order":  order.serialize()}, 201
            
            return{'message': "Order not found"}
        return {"message": "Authorization required"}, 403



        



