import os
import click
from app import create_app


config = os.getenv('APP_SETTINGS' or 'default')
app = create_app(config)


if __name__ == "__main__":
    app.run(debug=True)
