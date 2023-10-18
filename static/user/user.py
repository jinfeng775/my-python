# 导入单向加密
from werkzeug.security import check_password_hash, generate_password_hash
# 导入工具类
from static.app import response as util
# 导入日志框架
from nb_log import LogManager
logger = LogManager('lalala',).get_logger_and_add_handlers(log_path="./log",log_filename="my_log.log")
# 导入token框架
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
# 创建数据库打开数据库
from static.app import mongoClient

from flask import Blueprint, request

simple = Blueprint('simple', __name__, template_folder='templates')

# logger.debug(f'debug是绿色，说明是调试的，代码ok ')
# logger.info('info是天蓝色，日志正常 ')
# logger.warning('黄色yello，有警告了 ')
# logger.error('粉红色说明代码有错误 ')
# logger.critical('血红色，说明发生了严重错误 ')

# @app.route('/model_compare')
@simple.route('/model_compare', methods=['GET'])
def hello_world():
    return 'Hello, model_compare!'

@simple.route('/vue-admin-template/user/login', methods=['POST'])
def login():
    # logger.debug(request.stream.read())
    username = request.json['username']
    password = request.json['password']
    mongo = mongoClient.MongoDB()
    data = mongo.select_one_collection('user', 'accountPassword', {
        'username': username
    })
    mongoPassword = data['password']
    mongo.close()
    if not check_password_hash(mongoPassword, password):
        return util.response(message='账号或密码错误',code=500)

    access_token = create_access_token(identity=username)
    return util.response(data={'token':access_token})

@simple.route('/vue-admin-template/user/info', methods=['GET'])
@jwt_required()
def info():
    data = {
        'roles': ['admin'],
        'introduction': 'I am a super administrator',
        'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
        'name': 'Super Admin'
    }
    return util.response(code=20000, data=data)

@simple.route('/vue-admin-template/user/logout', methods=['POST'])
def logout():
    return util.response(code=20000, data='success')

