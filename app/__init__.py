from flask import Flask
from flask_restful import  Api
# from flask_api import FlaskAPI
from instance.config import app_config

from app.orders import  AcceptOrder



def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    api = Api(app)

        
    
    api.add_resource(AcceptOrder, '/api/v1/orders/<int:id>')



    return app
