import threading
import time

from src.arch.singletone import Singleton
from src.config.runtime_config import RuntimeConfig
from src.dao.ctr_mongodb_dao import CTRMongodbDao

""" Author: Pouria Nikvand """


class CacheManager(metaclass=Singleton):
    """
    this class is for managing in memory caching method
    it creates a thread that updates the cached_db (a dictionary that contains the CTR data) each specific time
    the method gets the data from the mongodb CTR collection and update the values in the cached_db

    methods :
    start : creates the thread for updating
    do : the main act that the thread is going to do
    _do_update_cache : updates the cache_db for updating the cache
    """

    def __init__(self):
        super().__init__()
        self.cached_db = {}
        self._is_stop = False
        self.ctr_mongodb_dao = CTRMongodbDao()
        self.start()

    def start(self):
        my_thread = threading.Thread(target=self.do)
        my_thread.start()

    def stop(self):
        self._is_stop = True

    def do(self):
        while True:
            if self._is_stop:
                break
            resolved_db_col = self.ctr_mongodb_dao.get_ctr_collection()
            if resolved_db_col is not None:
                self._do_update_cache(resolved_db_col)
            else:
                print("EXCEPTION : THERE IS NO CONNECTION TO DB")
            time.sleep(RuntimeConfig.CACHE_SLEEP_TIME)

    def _do_update_cache(self, resolved_db_col):
        for each in resolved_db_col:
            ad_id_cvr = self.cached_db.get(each["adId"], None)
            if ad_id_cvr is None or ad_id_cvr["estimatedCVR"] != each["estimatedCVR"]:
                self.cached_db[each["adId"]] = {"estimatedCVR": each["estimatedCVR"]}
