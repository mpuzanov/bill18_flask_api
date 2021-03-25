from flask import Blueprint

main = Blueprint('main', __name__)
print("Создали Blueprint main")

from . import views
