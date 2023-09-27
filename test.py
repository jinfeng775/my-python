import os

import pymongo
MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT =int(os.environ.get('MONGO_PORT'))
MONGO_USER = os.environ.get('MONGO_USER')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')

mongo_url = f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}'
client = pymongo.MongoClient(mongo_url)
# db 表示数据库名称，username 用户名 password 密码
db = client['test']
collection = db['123']
student = {
    'id': 12321,
    'name': '123',
}
res = collection.insert_one(student)
print(res, res.inserted_id)

