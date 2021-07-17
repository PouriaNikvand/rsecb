from typing import Union

from pymongo import MongoClient
import pymongo.errors as errors

""" Author: Pouria Nikvand """


class BaseMongodbDao:
    """
    Base method for initialization of mongodb connection and also main method for db accessing objects
    host : logging mongodb info - host address
    port : logging mongodb info - mongodb running port
    database_name : logging mongodb info - database name for creating the connection

    methods :
    find : find a document using a query returns it as the return_params defined
    insert : (not defined yet) for inserting into db if needed
    delete : (not defined yet) for deleting from db if needed
    """

    def __init__(self, host: str, port: str, database_name: str, user: str, key: str, collection_name: str,
                 serverSelectionTimeoutMS: int):
        self.host = host
        self.port = port
        try:
            self.client = MongoClient('mongodb://' + user + ':' + key + '@' + host + ':' + port + '/' + database_name,
                                      authSource="admin",
                                      serverSelectionTimeoutMS=serverSelectionTimeoutMS)
            self.client.server_info()
        except errors.ServerSelectionTimeoutError as e:
            print("Connection Failure to server", e)

        self.db = self.client[database_name]
        try:
            if database_name not in self.client.list_database_names():
                raise errors.OperationFailure(errors.PyMongoError)
        except errors.OperationFailure as e:
            print("Database Operation Failed or Connection Failure to server", e)

        self.cn = self.db[collection_name]
        try:
            if collection_name not in self.db.list_collection_names():
                raise errors.OperationFailure(errors.PyMongoError)
        except errors.OperationFailure as e:
            print("Collection Operation Failed or Connection Failure to server", e)

    def find(self, query_body: dict, return_params: Union[dict, None]):
        if isinstance(return_params, dict):
            docs = self.cn.find(query_body, return_params)
        else:
            docs = self.cn.find(query_body)
        try:
            res = [each for each in docs]
        except (errors.OperationFailure, errors.ConnectionFailure) as e:
            print('Collection Operation Failed or Connection Failure to server ', e)
            return None
        return res

    def insert(self, cn, body: dict):
        pass

    def delete(self, cn, body: dict):
        pass
