import unittest

from src.config.runtime_config import RuntimeConfig
from src.dao.base_mongodb_dao import BaseMongodbDao

""" Author: Pouria Nikvand """


class TestBaseMongodbDao(unittest.TestCase):
    base_mongo_dao = BaseMongodbDao(
        host=RuntimeConfig.MONGODB_ADDRESS,
        port=RuntimeConfig.MONGODB_PORT,
        database_name=RuntimeConfig.MONGODB_DB_NAME,
        user=RuntimeConfig.MONGODB_USER,
        key=RuntimeConfig.MONGODB_KEY,
        collection_name=RuntimeConfig.CTR_COLLECTION_NAME,
        server_selection_timout=RuntimeConfig.SERVER_SELECTOPM_TIMEOUT
    )

    def test_base_mongo_dao(self):
        self.assertIsInstance(self.base_mongo_dao.find({}), list)
        self.assertIsInstance(self.base_mongo_dao.find({}, None), list)
