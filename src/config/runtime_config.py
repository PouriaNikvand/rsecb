import os

from src.config.base_config import BaseConfig

""" Author: Pouria Nikvand """


class RuntimeConfig(BaseConfig):
    """
    RuntimeConfig configuration for project. This class contains main runtime config parameters for the project
    MONGODB_USER : login parameter for mongodb
    MONGODB_KEY : login parameter for mongodb
    MONGODB_PORT : login parameter for mongodb - the port that mongodb is listening its container
    MONGODB_ADDRESS : the address that mongodb running on
    MONGODB_DB_NAME : target mongodb database name
    CTR_COLLECTION_NAME : target mongodb database collection name
    SERVICE_PORT : main port for calling the api service
    CACHE_SLEEP_TIME : max time per second for updating the cache of mongodb collection
    SERVER_SELECTOPM_TIMEOUT : 1 controls how long the driver will try to connect to a server. The default value is 30s
    DEFAULT_NOT_FOUND_CTR_VALUE : Default value for not found ctr in mongodb set for -1
    """

    MONGODB_USER = 'root'
    MONGODB_KEY = 'example'
    MONGODB_PORT = '27017'
    MONGODB_ADDRESS = os.getenv('MONGODB_ADDRESS', 'localhost')
    MONGODB_DB_NAME = 'test'
    CTR_COLLECTION_NAME = 'taptap'
    SERVICE_PORT = 5005
    CACHE_SLEEP_TIME = 1
    SERVER_SELECTOPM_TIMEOUT = 1
    DEFAULT_NOT_FOUND_CTR_VALUE = -1


if __name__ == "__main__":
    RuntimeConfig.configure()
