from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from app.api.v2.auth import Login, SignUp


import config
from app.api.v1.views import *

jwt=JWTManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config)

    jwt.init_app(app)

    api = Api(app)

    from .api.v2.auth import auth_blueprint 
    auth = Api(auth_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix="/api/v2/auth")


    auth.add_resource(SignUp, '/signup')
    auth.add_resource(Login, '/login')
    
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
