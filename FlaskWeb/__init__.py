from flask import Flask, url_for


def creat_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'adaddwqdasdasd'

    from .view import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    return app
