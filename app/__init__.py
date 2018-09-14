from flask import Flask
from flask_restful import  Api
import config
from app.orders import SpecificOrder

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config)

    api = Api(app)

    api.add_resource(AcceptOrder, '/api/v1/orders/<int:id>')

    return app
