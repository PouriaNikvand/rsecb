from pymongo import MongoClient


class BaseMongodbDao:

    def __init__(self, host: str, port: str, user: str, database_name: str, collection_name: str):
        self.host = host
        self.port = port
        self.user = user

        self.client = MongoClient(port=self.port)
        self.db = self.client[database_name]
        self.default_index_name = collection_name

    def find(self, collection_name, body):
        pass

    def insert(self, collection_name, body):
        pass

    def delete(self, collection_name, body):
        pass
