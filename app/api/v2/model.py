import psycopg2
from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash
from app.api.v2.database import DatabaseConnection


class User(DatabaseConnection):
    def __init__(self, username=None, email=None,
                 password=None, confirm_password=None, is_admin=False):
        super().__init__()
        self.username = username
        self.email = email
        if password:
            self.password = generate_password_hash(password)
        self.confirm_password = confirm_password
        self.is_admin = is_admin

    def create_table(self):
        ''' create users table '''
        cursor = self.connection.cursor()
        cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS users(
                    id serial PRIMARY KEY,
                    username VARCHAR (200) NOT NULL,
                    email VARCHAR (200) NOT NULL,
                    password VARCHAR (200) NOT NULL,
                    confirm_password VARCHAR (200) NOT NULL,
                    is_admin BOOL NOT NULL
                )'''
            )
        self.connection.commit()
        self.connection.close()
        self.cursor.close()

    def drop_tables(self):
        ''' Drop tables'''
        cursor = self.connection.cursor()
        cursor.execute(
            ''' DROP TABLE IF EXISTS users'''
        )
        self.connection.commit()
        self.connection.close()
        self.cursor.close()

    def add(self):
        ''' add user to the users table'''
        cursor = self.connection.cursor()
        cursor.execute(
            '''
            INSERT INTO users(username, email,
            password, confirm_password, is_admin)
            VALUES(%s, %s, %s, %s, %s)
            ''',
            (self.username, self.email, self.password,
             self.confirm_password, self.is_admin)
        )
        self.connection.commit()
        cursor.close()

    def get_by_username(self, username):
        ''' Get user by username '''
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE username=%s", (username,)
        )

        user = cursor.fetchone()

        self.connection.commit()
        cursor.close()

        if user:
            return self.objectify_user(user)
        return None

    def get_by_email(self, email):
        ''' Get user by email '''
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM users WHERE email=%s", (email,)
        )

        user = cursor.fetchone()

        self.connection.commit()
        cursor.close()

        if user:
            return self.objectify_user(user)
        return None

    def serialize(self):
        return dict(
            username=self.username,
            email=self.email,
            password=self.password,
            confirm_password=self.confirm_password,
            is_admin=self.is_admin
        )

    def objectify_user(self, data):
        ''' Map a user to an object '''
        self.id = data[0]
        self.username = data[1]
        self.email = data[2]
        self.password = data[3]
        self.is_admin = data[4]

        return self


class FoodMenu(DatabaseConnection):
    def __init__(self, name=None, price=None, description=None):
        super().__init__()
        self.name = name
        self.price = price
        self.description = description
        self.date_created = datetime.now().replace(second=0, microsecond=0)
    
    def create_table(self):
        ''' create orders table '''
        cursor = self.connection.cursor()
        cursor.execute(            
            '''
            CREATE TABLE IF NOT EXISTS foodmenu(
                id serial PRIMARY KEY,
                name VARCHAR (200) NOT NULL,
                price INTEGER NOT NULL,
                description VARCHAR(200) NOT NULL,
                date_created TIMESTAMP
            )'''
        )
        self.connection.commit()
        self.connection.close()
        self.cursor.close()

    def drop_tables(self):
        ''' Drop tables'''
        cursor = self.connection.cursor()
        cursor.execute(
            ''' DROP TABLE IF EXISTS foodmenu'''
        )
        self.connection.commit()
        self.connection.close()
        self.cursor.close()

    def add(self):
        ''' add user to the users table'''
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO foodmenu(name, price, description, date)
            VALUES(%s, %s, %s, %s)
            ''', (self.name, self.price, self.description, self.date_created)
        )
        cursor.close()
        self.connection.commit()

    def get_by_id(self, item_id):
        ''' Get user by username '''
        cursor = self.connection.cursor()
        cursor.execute(   
            "SELECT * FROM foodmenu WHERE id=%s", (item_id,)
        )

        item = cursor.fetchone()

        cursor.close()
        self.connection.commit()

        if item:
            return self.obectify_fooditem(item)
        return None
        
    def get_all(self):
        """ get all available food in the menu"""
        cur = self.connection.cursor()
        cur.execute("SELECT * FROM foodmenu")

        FoodMenu = cur.fetchall()
        print(FoodMenu)

        self.connection.commit()
        cur.close()

        if FoodMenu:
            return [self.obectify_fooditem(foodmenu) for foodmenu in FoodMenu]
        return None

    def delete(self, menu_id):
        ''' delete a menu '''
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM foodmenu WHERE id=%s", (menu_id,))

        cursor.close()
        self.connection.commit()
    
    def serialize(self):
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description,
            date=str(self.date_created)
        )

    def obectify_fooditem(self, data):
        ''' Map a user to an object '''
        item = FoodMenu(name=data[1], description=data[2], price=data[3])
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
        cursor = self.connection.cursor()
        cursor.execute(
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
        self.connection.commit()
        self.connection.close()
        self.cursor.close()

    def drop_tables(self):
        ''' Drop tables'''
        cursor = self.connection.cursor()
        cursor.execute(
            ''' DROP TABLE IF EXISTS foodorders'''
        )
        self.connection.commit()
        self.connection.close()
        self.cursor.close()
    
    def add(self):
        ''' add orders to the foodorders table'''
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO foodorders(requester, name, destination, status, date)
            VALUES(%s, %s, %s, %s, %s)
            ''', (self.requester, self.name, self.destination,
                  self.status, self.date_created)
        )
        cursor.close()
        self.connection.commit()

    def get_all(self):
        """ get all available food items """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM foodorders")

        Foodorders = cursor.fetchall()

        cursor.close()
        self.connection.commit()

        if Foodorders:
            return [self.objectify_foodorder(foodorder)
                    for foodorder in Foodorders]
        return None

    def get_by_id(self, order_id):
        ''' Get order by ID '''
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM foodorders WHERE id=%s", (order_id,)
        )

        order = cursor.fetchone()

        cursor.close()
        self.connection.commit()

        if order:
            return self.objectify_foodorder(order)
        return None

    def accept_order(self, order_id):
        """ Accept an order """
        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE foodorders SET status=%s WHERE id=%s
                    """, ('accepted', order_id))
        cursor.close()
        self.connection.commit()

    def decline_order(self, order_id):
        """ Decline an order """
        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE foodorders SET status=%s WHERE id=%s
                    """, ('declined', order_id))
        cursor.close()
        self.connection.commit()

    def complete_accepted_order(self, order_id):
        """ Complete an accepted order """
        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE foodorders SET status=%s WHERE id=%s
                    """, ('completed', order_id))
        cursor.close()
        self.connection.commit()

    def comete_accepted_order(self, order_id):
        """ Complete an accepted order """
        cursor = self.connection.cursor()
        cursor.execute("""
        UPDATE foodorders SET status=%s WHERE id=%s
                    """, ('completed', order_id))
        cursor.close()
        self.connection.commit()

    def serialize(self):
        return dict(
            id=self.id,
            name=self.name,
            destination=self.destination,
            status=self.status,
            date=str(self.date_created)
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
