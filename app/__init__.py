'''create an instance of the applixation to load with the configuration settings'''
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from app.api.v2.admin import(PlaceNewMenu, AllMenu, SpecificMenu,
                             GetSpecificOrder, AllUserOrders, UpdateStatus)
from app.api.v2.auth import Login, SignUp
from app.api.v2.user.users import PlaceOrder, GetOrders

from config import app_config
from app.api.v1.views import (PlaceNewOrder, AllOrders, SpecificOrder, Accept,
                              Complete, Decline, DeclineOrder, GetAcceptedOrders,
                              CompletedOrders , DeclinedOrders)                              

jwt = JWTManager()

def create_app(config_name):
    '''initializes the application'''
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

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
    
    user.add_resource(PlaceOrder, '/orders/<int:id>')
    user.add_resource(GetOrders, '/orders')
    user.add_resource(AllMenu, '/menu')
    
    from .api.v2.admin import ADMIN_BLUEPRINT
    admin = Api(ADMIN_BLUEPRINT)
    app.register_blueprint(ADMIN_BLUEPRINT, url_prefix="/api/v2")
    
    admin.add_resource(PlaceNewMenu, '/menu')
    admin.add_resource(AllMenu, '/menu')
    admin.add_resource(SpecificMenu, '/menu/<int:id>')
    admin.add_resource(GetSpecificOrder, '/orders/<int:id>')
    admin.add_resource(AcceptOrder, '/orders/<int:id>/accept')
    admin.add_resource(CompleteOrder, '/orders/<int:id>/complete')
    admin.add_resource(DeclineOrder, '/orders/<int:id>/decline')
    admin.add_resource(AllUserOrders, '/orders')
    admin.add_resource(UpdateStatus, '/update/order/<int:id>')

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
