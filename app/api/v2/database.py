import psycopg2
from flask import current_app
import os 


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(current_app.config['DATABASE_URL'])
            self.cursor = self.connection.cursor()



        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def save(self):
        self.cursor.close()
        self.connection.commit()
