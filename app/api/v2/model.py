import psycopg2
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
            CREATE TABLE users IF NOT EXIST(
                id serial PRIMARY KEY,
                username VARCHAR (200) NOT NULL,
                email VARCHAR (200) NOT NULL,
                password VARCHAR (200) NOT NULL,
                confirm_password VARCHAR (200) NOT NULL
            ) 
            '''
        )
        self.save()

    def add(self):
        ''' add user to the users table'''
        self.cur.execute(
            '''
            INSERT INTO users(username, email, password, confirm_password, is_admin)
            VALUES(%s, %s, %s, %s, %s)
            '''
            (self.username, self.email, self.password, self.confirm_password, self.is_admin)
        )    
        self.save()

    def get_by_username(self, username):
        ''' Get user by username '''
        self.cur.execute(
            "SELECT * FROM users WHERE username=%s",(username,)
        )

        user = self.cur.fetchone()

        self.save()

        if user:
            return user
        return None

    def get_by_email(self, email):
        ''' Get user by email '''
        self.cur.execute(
            "SELECT * FROM users WHERE email=%s",(email,)
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


class FoodOrder:

    def __init__(self, name=None, price=None,
                 description=None, status="Pending"):
        self.id = len(orders)+1
        self.name = name
        self.price = price
        self.description = description
        self.status = status

    def serialize(self):
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description,
            status=self.status
        )

    def get_id(self, order_id):
        for order in orders:
            if order.id == order_id:
                return order
