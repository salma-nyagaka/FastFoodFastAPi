'''imort modules'''
import psycopg2
from flask import current_app


class DatabaseConnection:
    '''creates a connection to the database'''
    def __init__(self):
        try:
            self.connection = psycopg2.connect(current_app.config['DATABASE_URL'])
            self.cursor = self.connection.cursor()



        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def save(self):
        ''' closes the cursor  and makes commits to the database'''
        self.cursor.close()
        self.connection.commit()
