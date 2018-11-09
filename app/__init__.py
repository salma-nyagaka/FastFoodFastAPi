'''initializes the application'''
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

from app.api.v2.admin import (PlaceNewMenu, AllMenu, SpecificMenu, GetSpecificOrder, 
                              AllUserOrders, UpdateStatus, DeleteMenu, FilterOrdersByStatus,
                              UpdateMeal, GetMeal)

from app.api.v2.auth import Login, SignUp, UpdateProfile
from app.api.v2.user.users import PlaceOrder, GetOrders, GetAllMenu, GetNewOrders, DeleteOrder

from config import app_config
from app.api.v1.views import *

jwt=JWTManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    CORS(app)

    jwt.init_app(app)

    api = Api(app)    


    from .api.v2.auth import AUTH_BLUEPRINT 
    auth = Api(AUTH_BLUEPRINT)
    app.register_blueprint(AUTH_BLUEPRINT, url_prefix="/api/v2/auth")


    auth.add_resource(SignUp, '/signup')
    auth.add_resource(Login, '/login')
    
    from .api.v2.user import USER_BLUEPRINT
    user = Api(USER_BLUEPRINT)
    app.register_blueprint(USER_BLUEPRINT, url_prefix="/api/v2/users")

    user.add_resource(PlaceOrder, '/orders')
    user.add_resource(GetOrders, '/orders')
    user.add_resource(GetAllMenu, '/menu')
    user.add_resource(GetNewOrders, '/orders/<string:status>')
    user.add_resource(DeleteOrder, '/orders/<int:id>')
    user.add_resource(UpdateProfile, '/profile/<int:id>')



    
    from .api.v2.admin import ADMIN_BLUEPRINT
    admin = Api(ADMIN_BLUEPRINT)
    app.register_blueprint(ADMIN_BLUEPRINT, url_prefix="/api/v2")


    admin.add_resource(PlaceNewMenu, '/menu')
    admin.add_resource(AllMenu, '/menu')
    admin.add_resource(SpecificMenu, '/menu/<int:id>')
    admin.add_resource(GetSpecificOrder, '/orders/<int:id>')
    admin.add_resource(AllUserOrders, '/orders')
    admin.add_resource(UpdateStatus, '/update/order/<int:id>')
    admin.add_resource(DeleteMenu, '/menu/<int:id>')
    admin.add_resource(UpdateMeal, '/menu/<int:id>')
    admin.add_resource(FilterOrdersByStatus, '/orders/<string:status>')
    admin.add_resource(GetMeal, '/meal/<string:name>')
    


    api.add_resource(SpecificOrder, '/api/v1/orders/<int:id>')
    api.add_resource(AllOrders, '/api/v1/orders')
    api.add_resource(PlaceNewOrder, '/api/v1/orders')
    api.add_resource(Accept, '/api/v1/accept/orders/<int:id>')
    api.add_resource(Decline, '/api/v1/decline/orders/<int:id>')
    api.add_resource(Complete, '/api/v1/complete/orders/<int:id>')
    api.add_resource(GetAcceptedOrders, '/api/v1/accepted/orders')
    api.add_resource(CompletedOrders, '/api/v1/completed/orders')
    api.add_resource(DeclinedOrders, '/api/v1/declined/orders')
    api.add_resource(DeclineOrder, '/api/v1/decline/orders/<int:id>')
    

    return app
