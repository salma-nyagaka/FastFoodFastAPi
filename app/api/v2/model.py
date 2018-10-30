'''creation of database tables'''
from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash
from app.api.v2.database import DatabaseConnection


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
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users(
                id serial PRIMARY KEY,
                username VARCHAR (200) NOT NULL,
                email VARCHAR (200) NOT NULL,
                password VARCHAR (200) NOT NULL,
                is_admin BOOL NOT NULL)'''
            )
        self.save()

    def drop_tables(self):
        '''Drop tables'''
        self.cursor.execute(
            ''' DROP TABLE IF EXISTS users'''
        )
        self.save()

    def add(self):
        ''' add user to the users table'''
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
        self.cursor.execute(
            "SELECT * FROM users WHERE username=%s", (username,)
        )

        user = self.cursor.fetchone()

        self.save()


        if user:
            return self.objectify_user(user)
        return None


    def get_all_users(self):
        """ get all users"""
        self.cursor.execute("SELECT * FROM users")

        users = self.cursor.fetchall()
        self.save()

        if users:
            return [self.objectify_user(user) for user in users]
        return None


    def get_by_email(self, email):
        ''' Get user by email '''
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
            is_admin=self.is_admin,
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
    def __init__(self, name=None, price=None, description=None, image=None):
        super().__init__()
        self.name = name
        self.price = price
        self.description = description
        self.date_created = datetime.now().replace(second=0, microsecond=0)
        self.image = image
    
    def create_table(self):
        ''' create orders table '''
        self.cursor.execute(            
            '''
            CREATE TABLE IF NOT EXISTS foodmenu(
                id serial PRIMARY KEY,
                name VARCHAR (200) NOT NULL,
                price INTEGER NOT NULL,
                description VARCHAR(200) NOT NULL,
                date_created TIMESTAMP,
                image VARCHAR (200) NOT NULL)'''
            )
        self.save()


    def drop_tables(self):
        ''' Drop tables'''
        self.cursor.execute(
            ''' DROP TABLE IF EXISTS foodmenu'''
        )
        self.save()

    def add(self):
        ''' add orders to the food orders table'''
        self.cursor.execute('''
            INSERT INTO foodmenu(name, price, description,  date_created, image)
            VALUES(%s, %s, %s, %s, %s)
            ''', (self.name, self.price, self.description,  self.date_created, self.image))
        self.save()

    
    def update(self, id):
        """ update an existing food item """

        self.cursor.execute(
            """ UPDATE foodmenu SET name=%s, price=%s,  description=%s,  image=%s WHERE id=%s """, (
                self.name, self.price, self.description, self.image , id))
        self.save()


    def get_by_id(self, id):
        ''' Get user by food id '''
        self.cursor.execute(   
            "SELECT * FROM foodmenu WHERE id=%s", (id, )
        )
        item = self.cursor.fetchone()

        self.save()

        if item:
            return self.obectify_fooditem(item)
        return None

    def get_by_name(self, name):
        ''' Get user by food id '''
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
        self.cursor.execute("SELECT * FROM foodmenu ORDER BY id")

        FoodMenu = self.cursor.fetchall()
        self.save()

        if FoodMenu:
            return [self.obectify_fooditem(foodmenu) for foodmenu in FoodMenu]
        return None

    def get_all_menu(self):
        """ get all available food in the menu"""
        self.cursor.execute("SELECT * FROM foodmenu ORDER BY id")

        FoodMenu = self.cursor.fetchall()
        self.save()

        if FoodMenu:
            return [self.obectify_fooditem(foodmenu) for foodmenu in FoodMenu]
        return None


    def delete(self, menu_id):
        ''' delete a menu '''
        self.cursor.execute("DELETE FROM foodmenu WHERE id=%s", (menu_id,))

        self.save()

    def serialize(self):
        ''' return a dictionary from the object'''
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description,
            date=str(self.date_created),
            image=self.image
        )

    def obectify_fooditem(self, data):
        ''' Map a fooditem to an object '''
        item = FoodMenu(name=data[1], description=data[3], price=data[2])
        item.id = data[0]
        item.date_created = str(data[4])
        item.image = data[5]
        self = item
        return self


class FoodOrder(DatabaseConnection):
    '''creates tables for the food orders database'''
    def __init__(self, id = None, username=None,  food_name=None, description = None, price=None,
                 status="New", date = None, quantity = None, phonenumber=None):
        super().__init__()
        self.username = username
        self.food_name = food_name
        self.description = description
        self.price = price
        self.status = status
        self.date = datetime.now().replace(second=0, microsecond=0)
        self.quantity = quantity
        self.phonenumber = phonenumber
   

    def drop_tables(self):
        ''' Drop tables'''
        self.cursor.execute(
            ''' DROP TABLE IF EXISTS foodorders'''
        )
        self.save()

    def create_table(self):
        ''' create orders table '''
        self.cursor.execute(            
            '''
            CREATE TABLE IF NOT EXISTS foodorders(
               id serial PRIMARY KEY,
                username VARCHAR NOT NULL,
                food_name VARCHAR NOT NULL,
                description VARCHAR NOT NULL,
                price INT NOT NULL,
                status VARCHAR NOT NULL,
                date TIMESTAMP,
                quantity INT NOT NULL,
                phonenumber INT NOT NULL)
            '''
            )
        self.save()

    def add(self):
        ''' Add food order to database'''
        self.cursor.execute(
            ''' INSERT INTO foodorders(username, food_name, description, price, status, date, quantity, phonenumber)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
            ''',
            (self.username, self.food_name, self.description, self.price, self.status, self.date, self.quantity, self.phonenumber))

        self.save()


    def get_by_id(self, order_id):
        '''fetch an order by id'''
        self.cursor.execute(''' SELECT * FROM foodorders WHERE id=%s''',
                            (order_id, ))

        food_order = self.cursor.fetchone()

        self.save()

        if food_order:
            return self.objectify_orders(food_order)
        return None

    def get_all_orders_by_username(self, username):
        '''fetch orders by username'''
        self.cursor.execute(''' SELECT * FROM foodorders WHERE username=%s''', (username,))

        food_orders = self.cursor.fetchall()

        self.save()


        if food_orders:
            return [self.objectify_orders(foodorder) for foodorder in food_orders]
        return None

    def accept_order(self, order_id):
        """ accept an order """

        self.cursor.execute(
            """ UPDATE foodorder SET status=%s WHERE id= %s """, (
                'New', order_id
            )
        )
        self.save()

    def delete(self, order_id):
        ''' delete an order '''
        self.cursor.execute("DELETE FROM foodorders WHERE id=%s", (order_id,))

        self.save()


    def get_all(self):
        """ get all available food items """
        self.cursor.execute("SELECT * FROM foodorders ORDER BY id")

        food_orders = self.cursor.fetchall()

        self.save()

        if food_orders:

            return [self.objectify_orders(foodorder) for foodorder in food_orders]
        return None

    def get_all_orders_by_status(self, status):
        """ get all available food items """
        self.cursor.execute("SELECT * FROM foodorders WHERE status=%s", (status,))

        food_orders = self.cursor.fetchall()

        self.save()

        if food_orders:
            return [self.objectify_orders(foodorder)
                    for foodorder in food_orders]
        return None
    
    def update_order(self, status, order_id):
        """update order status"""
        self.cursor.execute("""
        UPDATE foodorders SET status=%s WHERE id=%s
                    """, (status, order_id))
        
        self.save()
   


    def serialize(self):
        ''' return object as a dictionary '''
        return dict (
            id = self.id,
            username = self.username,
            food_name = self.food_name,
            description = self.description,
            price = self.price,
            status = self.status,
            date = self.date,
            quantity = self.quantity,
            phonenumber = self.phonenumber
        )
    
    def objectify_orders(self, data):
        ''' map tuple to an object '''
        order = FoodOrder(  username=data[1],
                            food_name=data[2],
                            description=data[3],
                            price=data[4],
                            status=data[5])
        order.id = data[0],
        order.date = str(data[6]),
        order.quantity = data[7],
        order.phonenumber = data[8]
        self = order
        return self