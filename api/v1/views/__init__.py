!/usr/bin/python3
'''
Create Flask app blueprint
'''
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from ap1.v1.views.index import *
from api.v1.views.states import *
