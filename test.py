
ip = '49.232.253.214'
# db.auth("Plated0058","G3hJ6btp7aqaVz")
useranme = 'Plated0058'
password = "G3hJ6btp7aqaVz"
import pymongo


client = pymongo.MongoClient(host=ip, port=27017, username=useranme, password=password)
# db 表示数据库名称，username 用户名 password 密码
db = client['test']
collection = db['123']
student = {
    'id': 2,
    'name': '123',
}
res = collection.insert_one(student)
print(res, res.inserted_id)