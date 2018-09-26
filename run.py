import os

from app import create_app
from app.api.v2.database import CreateTables, DatabaseConnection

config = os.getenv('APP_SETTINGS')
app = create_app(config)


@app.cli.command()
def migrate():
    DatabaseConnection().init_app(app)
    CreateTables().create_tables()



if __name__ == "__main__":
    app.run(debug=True)
