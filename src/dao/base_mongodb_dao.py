from pymongo import MongoClient


class BaseMongodbDao:

    def __init__(self, host: str, port: str, database_name: str, collection_name: str):
        self.host = host
        self.port = port
        self.client = MongoClient(port=self.port)
        self.db = self.client[database_name]

    @staticmethod
    def find(cn, query_body, return_params):
        return cn.find(query_body, return_params)

    def insert(self, collection_name, body):
        pass

    def delete(self, collection_name, body):
        pass
