import os

from src.config.base_config import BaseConfig


class RuntimeConfig(BaseConfig):
    MONGODB_USER = 'root'
    MONGODB_KEY = 'example'
    SERVICE_PORT = 5005
    MONGODB_PORT = '27017'
    MONGODB_ADDRESS = os.getenv('MONGODB_ADDRESS', 'localhost')
    MONGODB_DB_NAME = 'test'
    MONGODB_COLLECTION_NAME = 'taptap'
    CTR_COLLECTION_NAME = 'taptap'


if __name__ == "__main__":
    RuntimeConfig.configure()
