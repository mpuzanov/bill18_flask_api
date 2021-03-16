from flask import Flask
import os
import config

# создание экземпляра приложения
app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
app.config['JSON_AS_ASCII'] = False

from . import views
