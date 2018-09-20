from flask import Flask
from flask_restful import  Api


import config
from app.api.v1.views import SpecificOrder, AllOrders, PlaceNewOrder


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config)


    api = Api(app)
    api.add_resource(SpecificOrder, '/api/v1/orders/<int:id>')
    api.add_resource( AllOrders, '/api/v1/orders')
    api.add_resource( PlaceNewOrder, '/api/v1/orders')




    return app
