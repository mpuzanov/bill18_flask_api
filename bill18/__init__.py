from flask import Flask, json
from flask_mail import Mail
from datetime import date, datetime
from decimal import Decimal

email = Mail()


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)

    app.json_encoder = MyJSONEncoder

    email.init_app(app)

    from bill18 import db
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

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
