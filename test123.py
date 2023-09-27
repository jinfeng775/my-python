from static.app import mongoClient
mongo = mongoClient.MongoDB()
import random
id = mongo.insert_one('test','123',{
        'id': random.randint(1,99999),
        'name': random.randint(1,99999),
})
print(id)
mongo.close()
