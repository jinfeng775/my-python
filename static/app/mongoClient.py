import pymongo
from concurrent.futures import ThreadPoolExecutor
import socket
import time
import os
from nb_log import LogManager
import sys
logger = LogManager('mangGoDB',).get_logger_and_add_handlers(log_path="./log/my_MangGoDB_log",log_filename="my_MangGoDB_log.log")

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT =int(os.environ.get('MONGO_PORT'))
MONGO_USER = os.environ.get('MONGO_USER')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')

class MongoDB:
    def __init__(self):

        self.mongo_url = f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}'
        self.pool = ThreadPoolExecutor(max_workers=10)
        self.client = pymongo.MongoClient(self.mongo_url, connectTimeoutMS=5000)

    def get_client(self):
        return self.pool.submit(pymongo.MongoClient,self.mongo_url,connectTimeoutMS=5000)

    def get_database(self, name):
        client = self.get_client().result()
        db = client[name]
        return db

    def insert_one(self, db_name, collection_name, doc):
        try:
            db = self.get_database(db_name)
            collection = db[collection_name]
            id = collection.insert_one(doc)
            return id.inserted_id
        except Exception as e:
            logger.error(f'向数据库插入单个报错了~表名---> {db_name} 集合名字---> {collection_name}: 错误内容--->{e}')
    def insert_many(self, db_name, collection_name, doc):
        try:
            db = self.get_database(db_name)
            collection = db[collection_name]
            id = collection.insert_many(doc)
            return id.inserted_ids
        except Exception as e:
            logger.error(f'向数据库插入多个报错了~表名---> {db_name} 集合名字---> {collection_name}: 错误内容--->{e}')

    def select_one_collection(self,db_name,collection_name,doc=None):#获取一条数据
        '''search_col：只能是dict类型,key大于等于一个即可，也可为空
        可使用修饰符查询：{"name": {"$gt": "H"}}#读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据
        使用正则表达式查询：{"$regex": "^R"}#读取 name 字段中第一个字母为 "R" 的数据'''
        db = self.get_database(db_name)
        collection = db[collection_name]
        try:
            result = collection.find_one(doc)  # 这里只会返回一个对象，数据需要自己取
            return result
        except TypeError as e:
            logger.error(f'查询单个的内容必须是dict类型---> {db_name} 集合名字---> {collection_name}: 错误内容--->{e}')
            return None
    def select_all_collection(self,db_name,collection_name,search_col=None,limit_num=sys.maxsize,sort_col='None_sort',sort='asc'):
        '''search_col：只能是dict类型,key大于等于一个即可，也可为空
        可使用修饰符查询：{"name": {"$gt": "H"}}#读取 name 字段中第一个字母 ASCII 值大于 "H" 的数据
        使用正则表达式查询：{"$regex": "^R"}#读取 name 字段中第一个字母为 "R" 的数据
        limit_num:返回指定条数记录，该方法只接受一个数字参数(sys.maxsize:返回一个最大的整数值)'''
        db = self.get_database(db_name)
        collection = db[collection_name]
        try:
            if sort_col==False or sort_col=='None_sort':
                results=collection.find(search_col).limit(limit_num)#这里只会返回一个对象，数据需要自己取
            else:
                sort_flag = 1
                if sort == 'desc':
                    sort_flag = -1
                results = collection.find(search_col).sort(sort_col,sort_flag).limit(limit_num)  # 这里只会返回一个对象，数据需要自己取
            result_all=[i for i in results]#将获取到的数据添加至list
            return result_all
        except TypeError as e:
            logger.error(f'查询多个的内容必须是dict类型---> {db_name} 集合名字---> {collection_name}: 错误内容--->{e}')
            return None

    def update_one_collecton(self,db_name,collection_name, search_col, update_col):
        '''该方法第一个参数为查询的条件，第二个参数为要修改的字段。
            如果查找到的匹配数据多余一条，则只会修改第一条。
            修改后字段的定义格式： { "$set": { "alexa": "12345" } }'''
        db = self.get_database(db_name)
        collection = db[collection_name]
        try:
            relust = collection.update_one(search_col, {
                "$set": update_col
            })
            return relust
        except TypeError as e:
            logger.error(f'查询单个条件与需要修改的字段只能是dict类型---> {db_name} 集合名字---> {collection_name}: 错误内容--->{e}')
            return None

    def update_batch_collecton(self, db_name,collection_name, search_col, update_col):
        '''批量更新数据'''
        db = self.get_database(db_name)
        collection = db[collection_name]
        try:
            relust = collection.update_many(search_col, update_col)
            return relust
        except TypeError as e:
            logger.error(f'查询多个条件与需要修改的字段只能是dict类型---> {db_name} 集合名字---> {collection_name}: 错误内容--->{e}')
            return None
    def close(self):
        self.client.close()
        self.pool.shutdown()
