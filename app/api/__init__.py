from flask import Blueprint

api = Blueprint('api', __name__)
print("Создали Blueprint api")

from . import views
