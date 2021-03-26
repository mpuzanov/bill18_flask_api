# import os
# from dotenv import load_dotenv
# from flask_script import Manager

from bill18 import create_app


# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)


app = create_app('flask.cfg')
# from .bill18 import views
# manager = Manager(bill18)


if __name__ == '__main__':
    app.run(debug=True)
