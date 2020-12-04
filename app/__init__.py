from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, DeployConfig

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    app.config.from_object(DevelopmentConfig)
    #app.config.from_object(DeployConfig)
    return app

app = create_app()
db = SQLAlchemy(app)

from app import routes
