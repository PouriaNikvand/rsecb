import unittest

from src.manager.api_manager import ApiManager

""" Author: Pouria Nikvand """


class TestApiManager(unittest.TestCase):
    api_manager = ApiManager()

    def test_find_estimated_ctr(self):
        self.assertEqual(self.api_manager.find_estimated_ctr({"adId": [1]}), {1: {"estimatedCVR": 0.841029708}})
        self.api_manager.stop()
        self.api_manager.cached_db = {1: {"estimatedCVR": 0.5}, 2: {"estimatedCVR": 0.8}}
        self.assertEqual(self.api_manager.find_estimated_ctr({"adId": [1]}), {1: {"estimatedCVR": 0.5}})
        self.assertEqual(self.api_manager.find_estimated_ctr({"adId": [-1]}), {-1: {"estimatedCVR": -1}})
