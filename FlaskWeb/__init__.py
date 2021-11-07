from flask import Flask
from flask_sqlalchemy import sqlalchemy
from os import path

db = sqlalchemy
DB_NAME = "database.db"


def creat_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'adaddwqdasdasd'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .view import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .models import User, Note

    return app
def create_database(app):
    if not path('website/'+DB_NAME):
        db.create_all(app=app)
        print('Create Database!')

