from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required


from ..model import FoodMenu


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

    def get(self, id):
        ''' get a specific menu '''

        menu = FoodMenu().get_by_id(id)

        if menu:
            return {"Menu": menu.serialize()}, 200
        return {'message': "Not found"}, 404

    def delete(self, id):
        ''' Delete a specific menu '''

        menu = FoodMenu().get_by_id(id)
        if menu:
            menu.delete(id)
            return {'message': "Deleted"}, 200
        return {'message': "Not found"}, 404
