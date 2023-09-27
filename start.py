from flask import Flask, request
from static.app import response as util
from nb_log import LogManager
logger = LogManager('lalala',).get_logger_and_add_handlers(log_path="./log",log_filename="my_log.log")


from static.app import mongoClient
mongo = mongoClient.MongoDB()
import random
id = mongo.insert_one('test','123',{
        'id': random.randint(1,99999),
        'name': random.randint(1,99999),
})
print(id)
mongo.close()











app = Flask(__name__)
# logger.debug(f'debug是绿色，说明是调试的，代码ok ')
# logger.info('info是天蓝色，日志正常 ')
# logger.warning('黄色yello，有警告了 ')
# logger.error('粉红色说明代码有错误 ')
# logger.critical('血红色，说明发生了严重错误 ')


@app.route('/')
def hello_world():
    return 'hello world,你好世界'


@app.route('/login', methods=['POST'])
def register():
    logger.debug(request.stream.read())

    return util.response(message='213')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # app.run(port=5000, debug=True)
