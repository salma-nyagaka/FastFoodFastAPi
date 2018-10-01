from app.api.v2.model import User, FoodMenu, FoodOrder, User

def drop():
    User().drop_tables()
    FoodOrder().drop_tables()
    FoodMenu().drop_tables()


def create():

    foodorder = FoodOrder()
    foodorder.create_table()

    foodmenu = FoodMenu()
    foodmenu.create_table()

    user= User()
    user.create_table()

def create_admin():
    admin = User(username='Admin', email='admin@gmail.com',
                 password='Admin123',  confirm_password='Admin123', is_admin=True)
    admin.add()

if __name__ == '__main__':
    drop()
    create()
    create_admin()