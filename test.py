import pymongo

client = pymongo.MongoClient(host='49.232.253.214', port=27017)
# db 表示数据库名称，username 用户名 password 密码
client.db.authenticate("Plated0058","G3hJ6btp7aqaVz")


# 建立数据库连接
db = client.test # or db = client['test']
collection = db['123']
student = {
    'id': 1,
    'name': 'test',
}
res = collection.insert_one(student)
print(res, res.inserted_id)