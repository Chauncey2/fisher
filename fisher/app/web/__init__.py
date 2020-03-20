"""
蓝图
"""
from flask import Blueprint

web = Blueprint('web', __name__)

# 将视图函数在蓝图中进行注册
from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
