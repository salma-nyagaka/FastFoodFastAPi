'''starts the applications with the configurtaion settings'''
import os
from app import create_app
import click

from app.api.v2.model import User, FoodMenu, FoodOrder

app = create_app(os.getenv("APP_SETTINGS") or 'default')


@app.cli.command()
def drop():
    '''drop all tables'''
    User().drop_tables()
    FoodOrder().drop_tables()
    FoodMenu().drop_tables()


@app.cli.command()
def create():
    '''creates tables'''
    foodorder = FoodOrder()
    foodorder.create_table()

    foodmenu = FoodMenu()
    foodmenu.create_table()

    user = User()
    user.create_table()

@app.cli.command()
def create_admin():
    '''creates an admin'''
    admin = User(username='Admin', email='admin@gmail.com',
                 password='Admin123', is_admin=True)
    admin.add()



if __name__ == "__main__":
    app.run()
