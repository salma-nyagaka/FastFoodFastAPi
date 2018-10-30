'''import modules to create users endpoints'''
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Flask, request


from app.api.v2.model import FoodOrder, FoodMenu
from utils.validators import Validators


class PlaceOrder(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=False,
                        help="This field cannot be left blank")
    parser.add_argument('quantity', type=str, required=False,
                    help="This field cannot be left blank")
    parser.add_argument('phonenumber', type=str, required=False,
                    help="This field cannot be left blank")
   
   
    @jwt_required
    def post(self):
        '''post an order by the user'''

        data = PlaceOrder.parser.parse_args()

        
        current_user = get_jwt_identity()['username']
        name = data['name']
        quantity = data['quantity']
        phonenumber = data['phonenumber']
        meal_item = FoodMenu().get_by_name(name)

        if data['phonenumber'].strip() == "":
                return {'message': 'Phonenumber cannot be left blank'}, 400    
        
        if not meal_item:
            return {"message": "Food not found"}, 404
        
        if (len(str(phonenumber)) > 10):
            return {'message': 'Phone number should have 10 characters'}, 400
        if (len(str(phonenumber)) < 10):
            return {'message': 'Phone number should have 10 characters'}, 400
        if not Validators().valid_phone(phonenumber):
                return {'message': 'Phone number starts with a + and a number'}, 400

        order = FoodOrder(username=current_user, food_name=meal_item.name, description=meal_item.description,
                      price=meal_item.price, quantity=quantity, phonenumber=phonenumber)
        order.add()

        return {"food_order": "order placed sucessfully" }, 201 


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
        return {'message': "No order history"}, 404


class GetAllMenu(Resource):
    '''get all menu'''
    # @jwt_required

    def get(self):
        """ Get all food items """
       
        data = FoodMenu().get_all_menu()

        food_menus = []

        if data:
            for food_menu in data:
                food_menus.append(food_menu.serialize())

            return {"Food menu": food_menus,
                    "message": "These are the available food items"}, 200
        return{"Food menu": "There are no meals available for now"}, 404




class GetNewOrders(Resource):
    '''get all the orders made'''
    @jwt_required
    def get(self, status):
        ''' get all food orders '''
      
        foodorders = FoodOrder().get_all()
        
        if foodorders:
            orders = [order.serialize() for order in foodorders if order.status == status]

            if orders:
                return {'orders': orders}, 200
            return {'message': "Not found"}, 404
        return {'message': "Not found"}, 404



class DeleteOrder(Resource):
    '''delete order'''
    @jwt_required
    def delete(self, id):
        ''' Delete an order'''
        
        order = FoodOrder().get_by_id(id)
        if order:
            order.delete(id)
            return {'message': "Successfully Deleted"}, 200
        return {'message': "Order item not found"}, 404

