from flask import Flask, json
from flask_mail import Mail
from datetime import date, datetime
from decimal import Decimal
import logging

mail = Mail()


def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        '%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    file_handler = logging.FileHandler('api.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)

    # if app.config["ENV"] == "prodaction":
    #     app.config.from_object('config.ProdactionConfig')
    # elif app.config["ENV"] == "testing":
    #     app.config.from_object('config.TestingConfig')
    # else:
    #     app.config.from_object('config.DevelopementConfig')

    # app.config.from_pyfile(config_filename)
    # bill18.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
    app.json_encoder = MyJSONEncoder

    mail.init_app(app)

    # logging.basicConfig(filename='record.log', level=logging.DEBUG,
    #                     format=f'%(asctime)s %(levelname)s %(name)s : %(message)s')
    app.logger = setup_logger()

    from bill18 import db
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    app.logger.debug("Создали create_app")
    return app


class MyJSONEncoder(json.JSONEncoder):
    """JSON serializer for objects not serializable by default json code"""

    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        # if isinstance(obj, Decimal):
        #     return str(obj)
        return super(MyJSONEncoder, self).default(obj)
