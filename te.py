#__author__ = 'jyzhang'

from pymongo import MongoClient


host = '127.0.0.1'
port = 27017


db = MongoClient(host, port)
coon = db['data']['db']
for i in range(10):
    coon.insert(
        {
            "_id": "bssssr",
            "baz": {
                "asd": "sss"
            },
            "z":10 - i
        }
    )

for i in range(4):
    print i
