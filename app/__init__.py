from flask import Flask
from flask_restful import  Api

#local imports
import config
from app.api.v1.views import SpecificOrder, AllOrders, Accept, Complete, Decline, PlaceNewOrder,DeclineOrder, GetAcceptedOrders, CompletedOrders, DeclinedOrders

#wraps creation of a new Flask object
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config)

    api = Api(app)
    api.add_resource(SpecificOrder, '/api/v1/orders/<int:id>')
    api.add_resource( AllOrders, '/api/v1/orders')
    api.add_resource( PlaceNewOrder, '/api/v1/orders')
    api.add_resource( Accept, '/api/v1/accept/orders/<int:id>')
    api.add_resource( Decline, '/api/v1/decline/orders/<int:id>')
    api.add_resource( Complete, '/api/v1/complete/orders/<int:id>')


    api.add_resource( GetAcceptedOrders, '/api/v1/accepted/orders')
    api.add_resource( CompletedOrders, '/api/v1/completed/orders')
    api.add_resource( DeclinedOrders, '/api/v1/declined/orders')
    
    api.add_resource( DeclineOrder, '/api/v1/decline/orders/<int:id>')

    return app
