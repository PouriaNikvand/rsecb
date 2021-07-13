from rsecb.src.config.base_config import BaseConfig


class RuntimeConfig(BaseConfig):
    SERVICE_PORT = 3000
    MONGODB_PORT = 27017
    MONGODB_DB_NAME = 'test'


if __name__ == "__main__":
    RuntimeConfig.configure()
