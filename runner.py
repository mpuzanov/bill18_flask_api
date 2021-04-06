import os
from dotenv import load_dotenv
from bill18 import log
from bill18 import create_app

# from flask_script import Manager

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = create_app(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')  # create_app('flask.cfg')


# print(app.config)
# manager = Manager(bill18)


@app.before_first_request
def setup_logging():
    if not app.debug:
        app.logger.addHandler(log.get_mail_handler())
        app.logger.addHandler(log.get_rotating_file_handler())
    else:
        app.logger.addHandler(log.get_file_handler())


if __name__ == '__main__':
    app.run(debug=True, port=5001)
