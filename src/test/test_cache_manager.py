import unittest

from src.manager.cache_manager import CacheManager

""" Author: Pouria Nikvand """


class TestCacheManager(unittest.TestCase):
    cache_manager = CacheManager()

    def test__do_update_cache(self):
        self.cache_manager.stop()
        self.cache_manager._do_update_cache([{"adId": 1, "estimatedCVR": 0.5}, {"adId": 2, "estimatedCVR": 0.8}])
        self.assertEqual(self.cache_manager.cached_db[1], {"estimatedCVR": 0.5})
