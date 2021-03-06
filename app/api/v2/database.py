'''import modules'''
import psycopg2
from flask import current_app

class DatabaseConnection:
    '''connection to the database'''
    def __init__(self):
        try:
            self.connection = psycopg2.connect(current_app.config['DATABASE_URL'])
            self.cursor = self.connection.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print("\n\n\Error!!! : {}\n\n\n".format(error))

    def save(self):
        ''' method to call the connection'''
        self.connection.commit()
 