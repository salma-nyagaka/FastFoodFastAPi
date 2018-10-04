'''import modules'''
from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash
from app.api.v2.database import DatabaseConnection
import psycopg2


class User(DatabaseConnection):
    '''create an instance of the class'''
    def __init__(self, username=None, email=None,
                 password=None, is_admin=False):
        super().__init__()
        self.username = username
        self.email = email
        if password:
            self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def create_table(self):
        '''create users table'''
        self.connection = psycopg2.connect(current_app.config['DATABASE_URL'])

        self.cursor = self.connection.cursor()
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users(
                id serial PRIMARY KEY,
                username VARCHAR (200) NOT NULL,
                email VARCHAR (200) NOT NULL,
                password VARCHAR (200) NOT NULL,
                is_admin BOOL NOT NULL
            )'''
            )
        self.connection.commit()

    def drop_tables(self):
        '''Drop tables'''
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            ''' DROP TABLE IF EXISTS users'''
        )
        self.save()

    def add(self):
        ''' add user to the users table'''
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            '''
            INSERT INTO users(username, email,
            password, is_admin)
            VALUES(%s, %s, %s, %s)
            ''',
            (self.username, self.email, self.password,
             self.is_admin)
        )
        self.save()

    def get_by_username(self, username):
        ''' Get user by username '''
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "SELECT * FROM users WHERE username=%s", (username,)
        )

        user = self.cursor.fetchone()

        self.save()


        if user:
            return self.objectify_user(user)
        return None

    def get_by_email(self, email):
        ''' Get user by email '''
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "SELECT * FROM users WHERE email=%s", (email,)
        )

        user = self.cursor.fetchone()

        self.save()


        if user:
            return self.objectify_user(user)
        return None

    def serialize(self):
        '''converts an object to a dictionary'''
        return dict(
            username=self.username,
            email=self.email,
            password=self.password,
            is_admin=self.is_admin
        )

    def objectify_user(self, data):
        ''' Map a user to an object '''
        self._id = data[0]
        self.username = data[1]
        self.email = data[2]
        self.password = data[3]
        self.is_admin = data[4]

        return self


class FoodMenu(DatabaseConnection):
    ''' instance of the FoodMenu class'''
    def __init__(self, name=None, price=None, description=None):
        super().__init__()
        self.name = name
        self.price = price
        self.description = description
        self.date_created = datetime.now().replace(second=0, microsecond=0)
    
    def create_table(self):
        ''' create orders table '''
        self.cursor = self.connection.cursor()
        self.cursor.execute(            
            '''
            CREATE TABLE IF NOT EXISTS foodmenu(
                id serial PRIMARY KEY,
                name VARCHAR (200) NOT NULL,
                price INTEGER NOT NULL,
                description VARCHAR(200) NOT NULL,
                date_created TIMESTAMP
            )'''
            )
        self.save()


    def drop_tables(self):
        ''' Drop tables'''
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            ''' DROP TABLE IF EXISTS foodmenu'''
        )
        self.save()

    def add(self):
        ''' add orders to the food orders table'''
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            INSERT INTO foodmenu(name, price, description, date_created)
            VALUES(%s, %s, %s, %s)
            ''', (self.name, self.price, self.description, self.date_created))
        
        self.save()


    def get_by_id(self, id):
        ''' Get user by food id '''
        self.cursor = self.connection.cursor()
        self.cursor.execute(   
            "SELECT * FROM foodmenu WHERE id=%s", (id,)
        )

        item = self.cursor.fetchone()

        self.save()


        if item:
            return self.obectify_fooditem(item)
        return None

    def get_by_name(self, name):
        ''' Get user by food id '''
        self.cursor = self.connection.cursor()
        self.cursor.execute(   
            "SELECT * FROM foodmenu WHERE name=%s", (name,)
        )

        item = self.cursor.fetchone()

        self.save()


        if item:
            return self.obectify_fooditem(item)
        return None

    def get_all(self):
        """ get all available food in the menu"""
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM foodmenu")

        FoodMenu = self.cursor.fetchall()
        print(FoodMenu)

        self.save()


        if FoodMenu:
            return [self.obectify_fooditem(foodmenu) for foodmenu in FoodMenu]
        return None


    def delete(self, menu_id):
        ''' delete a menu '''
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM foodmenu WHERE id=%s", (menu_id,))

        self.save()

    def serialize(self):
        ''' return a dictionary from the object'''
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description,
            date=str(self.date_created)
        )

    def obectify_fooditem(self, data):
        ''' Map a fooditem to an object '''
        item = FoodMenu(name=data[1], description=data[3], price=data[2])
        item.id = data[0]
        item.date_created = data[4]
        self = item
        return self


class FoodOrder(DatabaseConnection):

    def __init__(self, requester=None, name=None, destination=None):
        super().__init__()
        self.requester = requester
        self.name = name
        self.destination = destination
        self.status = 'pending'
        self.date_created = datetime.now().replace(second=0, microsecond=0)

    def create_table(self):
        ''' create orders table '''
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS foodorders(
                id serial PRIMARY KEY,
                requester VARCHAR (200) NOT NULL,
                name VARCHAR (200) NOT NULL,
                destination VARCHAR(200) NOT NULL,
                status VARCHAR (200) NOT NULL,
                date TIMESTAMP
            )'''
            )
        self.save()

    def get_by_destination(self, destination):
        ''' Get user by food id '''
        self.cursor = self.connection.cursor()
        self.cursor.execute(   
            "SELECT * FROM foodorders WHERE destination=%s", (destination,))

        FoodOrder = self.cursor.fetchone()

        self.save()

        if FoodOrder:
            return self.objectify_foodorder(FoodOrder)
        return None



    def drop_tables(self):
        ''' Drop tables'''
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            ''' DROP TABLE IF EXISTS foodorders'''
        )
        self.save()
    
    def add(self):
        ''' add orders to the foodorders table'''
        self.cursor.execute('''
            INSERT INTO foodorders(requester, name, destination, status, date)
            VALUES(%s, %s, %s, %s, %s)
            ''', (self.requester, self.name, self.destination,
                  self.status, self.date_created))
        self.save()

    def get_all(self):
        """ get all available food items """
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM foodorders")

        Foodorders = self.cursor.fetchall()

        self.save()

        if Foodorders:
            return [self.objectify_foodorder(foodorder)
                    for foodorder in Foodorders]
        return None
    
    def get_all_orders_by_username(self, username):
        """ get all orders available by username """
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM foodorders WHERE requester=%s", (username, ))

        food_orders = self.cursor.fetchall()

        self.save()

        if food_orders:
            return [self.objectify_foodorder(foodorder)
                    for foodorder in food_orders]
        return None

    def get_by_id(self, order_id):
        ''' Get order by ID '''
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "SELECT * FROM foodorders WHERE id=%s", (order_id,)
        )

        order = self.cursor.fetchone()

        self.save()
        if order:
            return self.objectify_foodorder(order)
        return None

    def update_order(self, order_id):
        """update order status"""
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        UPDATE foodorders SET status=%s WHERE id=%s
                    """, ('status', order_id))
        self.save()

    def serialize(self):
        ''' returns a dictioanry from the object'''
        return dict(
            id=self.id,
            name=self.name,
            destination=self.destination,
            status=self.status,
            date=str(self.date_created),
            requester=self.requester
        )

    def objectify_foodorder(self, data):
        ''' Map a foodorder to an object '''
        order = FoodOrder(
            requester=data[1], name=data[2], destination=data[3])
        order.id = data[0]
        order.status = data[4]
        order.date_created = data[5]
        self = order

        return self
