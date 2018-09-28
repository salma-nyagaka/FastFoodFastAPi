import psycopg2

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(database = "fast_food_db", user = "fast_food_user", password = "salma", host = "localhost")

            self.cursor = self.connection.cursor()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def save(self):
        self.cursor.close()
        self.connection.commit()
