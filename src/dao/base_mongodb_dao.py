from pymongo import MongoClient


class BaseMongodbDao:

    def __init__(self, host: str, port: str, database_name: str, user: str, key: str, collection_name: str):
        self.host = host
        self.port = port
        self.client = MongoClient('mongodb://' + user + ':' + key + '@' + host + ':' + port + '/' + database_name,
                                  authSource="admin")
        self.db = self.client[database_name]

    @staticmethod
    def find(cn, query_body, return_params):
        res = cn.find(query_body, return_params)
        return [each for each in res]

    def insert(self, collection_name, body):
        pass

    def delete(self, collection_name, body):
        pass
