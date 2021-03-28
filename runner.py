import os
from dotenv import load_dotenv
# from flask_script import Manager
import logging
import sys

from bill18 import create_app

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = create_app(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')  # create_app('flask.cfg')
# print(app.config)

# manager = Manager(bill18)


@app.before_first_request
def setup_logging():

    if not app.debug:
        # In production mode, add log handler to sys.stdout.
        app.logger.addHandler(logging.StreamHandler(stream=sys.stdout))
        app.logger.setLevel(logging.INFO)
    else:
        app.logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
