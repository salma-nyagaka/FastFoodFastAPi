class CreateTables(DatabaseConnection):
    def __init__(self):
        super().__init__()

    def create_tables(self):
        ''' create tables for data storage '''
        
        queries = [
            '''
            CREATE TABLE fooditems IF NOT EXIST(
                id serial PRIMARY KEY,
                name VARCHAR (200) NOT NULL,
                description VARCHAR (200) NOT NULL,
                price NUMERIC NOT NULL,
                date TIMESTAMP
            ) 
            ''',
            '''
            CREATE TABLE foodorders IF NOT EXIST(
                id serial PRIMARY KEY,
                name VARCHAR (200) NOT NULL,
                price NUMERIC NOT NULL,
                destination VARCHAR(200) NOT NULL,
                status VARCHAR (200) NOT NULL,
                ordered_by VARCHAR(200) NOT NULL,
                date TIMESTAMP
            ) 
            '''
        ]

        # self.connection = psycopg2.connect(
        #         current_app.config.get('DATABASE_URL')
        #     )

        cur = self.connection.cursor()

        for query in queries:
            cur.execute(query)

        cur.close()
        self.connection.commit()