from pymongo import MongoClient
from concurrent.futures import ThreadPoolExecutor
import socket
import time
import os
from nb_log import LogManager

logger = LogManager('mangGoDB',).get_logger_and_add_handlers(log_path="./log",log_filename="my_MangGoDB_log.log")

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')
MONGO_USER = os.environ.get('MONGO_USER')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')


class MongoDB:
    def __init__(self):
        self.mongo_url = f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}'
        self.pool = ThreadPoolExecutor(max_workers=10)
        self.client = MongoClient(self.mongo_url, connectTimeoutMS=5000)

    def get_client(self):
        return self.pool.submit(MongoClient, self.mongo_url,
                                connectTimeoutMS=5000)

    def get_database(self, name):
        client = self.get_client()
        db = client[name]
        return db

    def insert_one(self, db_name, collection_name, doc):
        try:
            db = self.get_database(db_name)
            collection = db[collection_name]
            collection.insert_one(doc)
        except Exception as e:
            logger.error(f'Failed to insert document into {db_name}.{collection_name}: {e}')

    def close(self):
        self.client.close()
        self.pool.shutdown()
