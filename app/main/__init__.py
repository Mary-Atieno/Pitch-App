# from .views import *
# from flask import Blueprint

# main = Blueprint('main', __name__)

from flask import Blueprint

main = Blueprint('main',__name__)

from . import views,error