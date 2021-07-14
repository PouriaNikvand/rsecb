from src.config.base_config import BaseConfig


class RuntimeConfig(BaseConfig):
    SERVICE_PORT = 3000
    MONGODB_PORT = 27017
    MONGODB_ADDRESS = 'mongodb'
    MONGODB_DB_NAME = 'test'
    MONGODB_COLLECTION_NAME = 'taptap'
    CTR_COLLECTION_NAME = 'taptap'


if __name__ == "__main__":
    RuntimeConfig.configure()
