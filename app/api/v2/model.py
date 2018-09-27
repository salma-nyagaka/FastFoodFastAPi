import psycopg2
from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                current_app.config.get('DATABASE_URL')
            )

            self.cur = self.connection.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def init_app(self, app):
        self.connection = psycopg2.connect(
                current_app.config.get('DATABASE_URL')
            )

    def save(self):
        self.cur.close()
        self.connection.commit()


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
        self.cur.execute(
            '''
            CREATE TABLE IF NOT EXIST users(
                id serial PRIMARY KEY,
                username VARCHAR (200) NOT NULL,
                email VARCHAR (200) NOT NULL,
                password VARCHAR (200) NOT NULL,
                confirm_password VARCHAR (200) NOT NULL
            )'''
        )
        self.save()

    def add(self):
        ''' add user to the users table'''
        self.cur.execute(
            '''
            INSERT INTO users(username, email,
            password, confirm_password, is_admin)
            VALUES(%s, %s, %s, %s, %s)
            '''
            (self.username, self.email, self.password,
             self.confirm_password, self.is_admin)
        )
        self.save()

    def get_by_username(self, username):
        ''' Get user by username '''
        self.cur.execute(
            "SELECT * FROM users WHERE username=%s", (username,)
        )

        user = self.cur.fetchone()

        self.save()

        if user:
            return user
        return None

    def get_by_email(self, email):
        ''' Get user by email '''
        self.cur.execute(
            "SELECT * FROM users WHERE email=%s", (email,)
        )

        user = self.cur.fetchone()

        self.save()

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

    def __init__(self, name=None, price=None,
                 description=None, date=None):
        super().__init__()
        self.name = name
        self.price = price
        self.description = description
        self.date = datetime.now().replace(second=0, microsecond=0)

    def create_table(self):
        ''' create orders table '''
        self.cur.execute(
            '''
            CREATE TABLE IF NOT EXIST foodmenu(
                id serial PRIMARY KEY,
                name VARCHAR (200) NOT NULL,
                price NUMERIC NOT NULL,
                description VARCHAR(200) NOT NULL,
                date TIMESTAMP
            )'''
        )
        self.save()

    def add(self):
        ''' add user to the users table'''
        self.cur.execute(
            '''
            INSERT INTO foodmenu(name, price, description, date)
            VALUES(%s, %s, %s, %s)
            '''
            (self.name, self.price, self.description, self.date)
        )
        self.save()
        
    def get_by_id(self, item_id):
        ''' Get user by username '''
        self.cur.execute(
            "SELECT * FROM foodmenu WHERE id=%s", (item_id,)
        )

        item = self.cur.fetchone()

        self.save()

        if item:
            return item
        return None
        
    def get_all(self):
        """ get all available food items """
        self.cur.execute("SELECT * FROM foodmenu")
        foodmenu = self.cur.fetchall()

        self.save()

        if foodmenu:
            return foodmenu
        return None

    def delete(self, menu_id):
        ''' delete a menu '''
        self.cur.execute("DELETE FROM foodmenu WHERE id=%s", (menu_id,))

        self.save()
    
    def serialize(self):
        return dict(
            name=self.name,
            price=self.price,
            description=self.description,
            date=self.date
        )


class FoodOrder(DatabaseConnection):

    def __init__(self, name=None,
                 destination=None, status=None,
                 ordered_by=None, date=None):
        super().__init__()
        self.name = name
        self.destination = destination
        self.status = status
        self.ordered_by = ordered_by
        self.date = datetime.now().replace(second=0, microsecond=0)

    def create_table(self):
        ''' create orders table '''
        self.cur.execute(
            '''
            CREATE TABLE IF NOT EXIST foodorders(
                id serial PRIMARY KEY,
                name VARCHAR (200) NOT NULL,
                destination VARCHAR(200) NOT NULL,
                status VARCHAR (200) NOT NULL,
                ordered_by VARCHAR(200) NOT NULL,
                date TIMESTAMP
            )'''
        )
        self.save()

    def add(self):
        ''' add orders to the foodorders table'''
        self.cur.execute('''
            INSERT INTO foodorders(name, destination, status, ordered_by, date)
            VALUES(%s, %s, %s, %s, %s, %s)
            '''
            (self.name, self.destination, self.status,
             self.ordered_by, self.date)
        )
        self.save()

    def get_all(self):
        """ get all available food items """
        self.cur.execute("SELECT * FROM foodorders")
        foodorder = self.cur.fetchall()

        self.save()

        if foodorder:
            return foodorder
        return None


    def get_by_id(self, item_id):
        ''' Get food item by ID '''
        self.cur.execute(
            "SELECT * FROM foodmenu WHERE id=%s", (item_id,)
        )

        item = self.cur.fetchone()

        self.save()

        if item:
            return item
        return None
    
    def get_id(self, order_id):
        ''' Get order by ID '''
        self.cur.execute(
            "SELECT * FROM foodorder WHERE id=%s", (order_id,)
        )

        order = self.cur.fetchone()

        self.save()

        if order:
            return order
        return None
        
    def serialize(self):
        return dict(
            name=self.name,
            destination=self.destination,
            status=self.status,
            ordered_by=self.ordered_by,
            date=self.date
        )
