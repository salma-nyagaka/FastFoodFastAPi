import psycopg2
from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash
from database import DatabaseConnection

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
        try:
            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS users(
                    id serial PRIMARY KEY,
                    username VARCHAR (200) NOT NULL,
                    email VARCHAR (200) NOT NULL,
                    password VARCHAR (200) NOT NULL,
                    confirm_password VARCHAR (200) NOT NULL
                )'''
            )
        except:
            print("Error!")

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
            return user
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
            return user
        return None

    def serialize(self):
        return dict(
            username=self.username,
            email=self.email,
            password=self.password,
            confirm_password=self.confirm_password,
            is_admin=self.is_admin
        )


class FoodMenu(DatabaseConnection):

    def __init__(self, name=None, price=None, description=None, date=None):
        self.name = name
        self.price = price
        self.description = description
        self.date = datetime.now().replace(second=0, microsecond=0)
        super().__init__()


    def create_table(self):
        ''' create orders table '''
        cursor = self.connection.cursor()
        try:
            cursor.execute(            '''
            CREATE TABLE IF NOT EXISTS foodmenu(
                id serial PRIMARY KEY,
                name VARCHAR (200) NOT NULL,
                price NUMERIC NOT NULL,
                description VARCHAR(200) NOT NULL,
                date TIMESTAMP
            )'''
        )
      
        except:
            print("Error!")

        self.connection.commit()
        self.connection.close()
        self.cursor.close()

    def add(self):
        ''' add user to the users table'''
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO foodmenu(name, price, description, date)
            VALUES(%s, %s, %s, %s)
            ''',
            (self.name, self.price, self.description, self.date)
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
            return item
        return None
        
    def get_all(self):
        """ get all available food items """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM foodmenu")
        foodmenu = cursor.fetchall()

        cursor.close()
        self.connection.commit()

        if foodmenu:
            return foodmenu
        return None

    def delete(self, menu_id):
        ''' delete a menu '''
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM foodmenu WHERE id=%s", (menu_id,))

        cursor.close()
        self.connection.commit()
    
    def serialize(self):
        return dict(
            name=self.name,
            price=self.price,
            description=self.description,
            date=self.date
        )


class FoodOrder(DatabaseConnection):

    def __init__(self, name=None, destination=None, status=None,
                 date=None):
        self.name = name
        self.destination = destination
        self.status = status
        self.date = datetime.now().replace(second=0, microsecond=0)
        super().__init__()


    def create_table(self):
        ''' create orders table '''
        cursor = self.connection.cursor()
        try:
            cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS foodorders(
                id serial PRIMARY KEY,
                name VARCHAR (200) NOT NULL,
                destination VARCHAR(200) NOT NULL,
                status VARCHAR (200) NOT NULL,
                date TIMESTAMP
            )'''
        )
      
        except:
            print("Error!")

        self.connection.commit()
        self.connection.close()
        self.cursor.close()
    
    def add(self):
        ''' add orders to the foodorders table'''
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO foodorders(name, destination, status,date)
            VALUES(%s, %s, %s, %s, %s, %s)
            ''',
            (self.name, self.destination, self.status,
             self.date)
        )
        cursor.close()
        self.connection.commit()

    def get_all(self):
        """ get all available food items """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM foodorders")
        foodorder = cursor.fetchall()

        cursor.close()
        self.connection.commit()

        if foodorder:
            return foodorder
        return None


    def get_by_id(self, item_id):
        ''' Get food item by ID '''
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM foodmenu WHERE id=%s", (item_id,)
        )

        item = cursor.fetchone()

        cursor.close()
        self.connection.commit()

        if item:
            return item
        return None
    
    def get_id(self, order_id):
        ''' Get order by ID '''
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM foodorder WHERE id=%s", (order_id,)
        )

        order = cursor.fetchone()

        cursor.close()
        self.connection.commit()

        if order:
            return order
        return None
        
    def serialize(self):
        return dict(
            name=self.name,
            destination=self.destination,
            status=self.status,
            date=self.date
        )

foodorder = FoodOrder()
foodorder.create_table()

foodmenu = FoodMenu()
foodmenu.create_table()

user= User()
user.create_table()