import unittest

from src.dao.ctr_mongodb_dao import CTRMongodbDao

""" Author: Pouria Nikvand """


class TestCTRMongodbDao(unittest.TestCase):
    ctr_mongo_dao = CTRMongodbDao()

    def test_get_ctr_ad_id(self):
        self.assertEqual(self.ctr_mongo_dao.get_ctr_ad_id(1)[0], {"estimatedCVR": 0.841029708})
        self.assertIsInstance(self.ctr_mongo_dao.get_ctr_ad_id(1), list)
        self.assertIsInstance(self.ctr_mongo_dao.get_ctr_ad_id(-1), list)

    def test_get_ctr_collection(self):
        self.assertEqual(len(self.ctr_mongo_dao.get_ctr_collection()), 59)
        self.assertIsInstance(self.ctr_mongo_dao.get_ctr_collection(), list)
