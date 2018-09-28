# import psycopg2
# import os
# # from queries import queries


# # url = os.getenv('DATABASE_URL')

# # conn = psycopg2.connect(url)
# # curr = conn .cursor()

# # def init_db():
# #     for query in queries:
# #             curr.execute(query)
# #     conn.commit()

# # print(conn)

# class db:
#     def __init__(self):
#         self.db_name = "fast_food_db"
#         self.db_host = "localhost"
#         self.db_username = "fast_food_user"
#         self.db_password = "salma"
#         self.conn = psycopg2.connect(
#             database=self.db_name,
#             host=self.db_host,
#             user=self.db_username,
#             password=self.db_password)
#         self.cur = self.conn.cursor()
#         print(self.conn)

#     def create_table(self, schema):
#         self.cur.execute(schema)
#         # self.save()

# class User(db):
#     """ User Model """

#     def __init__(
#             self, username=None, name=None, email=None, password=None, is_admin=False):
#         super().__init__()
#         self.username = username
#         self.name = name
#         self.email = email
#         self.is_admin = is_admin
#         self.password_hash = "" if not password else generate_password_hash(
#             password)

#     def create(self):
#         self.create_table(
#             """
#             CREATE TABLE users(
#                 id serial PRIMARY KEY,
#                 username VARCHAR NOT NULL UNIQUE,
#                 name VARCHAR NOT NULL,
#                 email VARCHAR NOT NULL UNIQUE,
#                 password_hash TEXT NOT NULL,
#                 is_admin BOOLEAN NOT NULL
#             );
#             """
#         )

# t = db()
# t
# user = User()
# user.create()


import psycopg2

try:
    conn = psycopg2.connect(database = "fast_food_db", user = "fast_food_user", password = "salma", host = "localhost")
except:
    print("I am unable to connect to the database") 

cur = conn.cursor()
try:
    cur.execute(
        """
            CREATE TABLE users(
                id serial PRIMARY KEY,
                username VARCHAR NOT NULL UNIQUE,
                name VARCHAR NOT NULL,
                email VARCHAR NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                is_admin BOOLEAN NOT NULL
            );
            """
    )
except:
    print("I can't drop our test database!")

conn.commit() # <--- makes sure the change is shown in the database
conn.close()
cur.close()
