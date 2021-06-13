from flask import Flask

def create_app():

    app = Flask(__name__)

    from .main import index
    app.register_blueprint(index.main)

    return app