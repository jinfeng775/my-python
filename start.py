
from flask import Flask
# 导入token框架
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import datetime
from static.user.user import simple
from static.app.uploadImage import UploadImage
from static.app import response as util


# 配置
app = Flask(__name__)
app.register_blueprint(UploadImage)
app.register_blueprint(simple)
jwt = JWTManager(app)
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return util.response(code=500, message='令牌过期')

app.config['JWT_SECRET_KEY'] = 'my_secret_key'
# 设置 token的默认过期时间
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(minutes=1)



@app.route('/')
def hello_world():
    return 'hello world,你好世界'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
