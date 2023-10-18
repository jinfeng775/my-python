# 导入Flask类
from flask import Blueprint

simple = Blueprint('simple', __name__, template_folder='templates')


# @app.route('/model_compare')
@simple.route('/model_compare', methods=['GET'])
def hello_world():
    return 'Hello, model_compare!'