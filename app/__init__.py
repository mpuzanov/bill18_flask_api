import os
from flask import Flask
from .utils import MyJSONEncoder


def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)
    # app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
    app.json_encoder = MyJSONEncoder

    from app import db
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    print("Создали create_app")
    return app
