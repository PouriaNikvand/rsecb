import threading
import time

from src.manager.api_manager import ApiManager


class CacheManager(ApiManager):
    def __init__(self):
        super().__init__()

    def start(self):
        my_thread = threading.Thread(target=self.do)
        my_thread.start()
        # my_thread.join(5)

    def do(self):
        # lock = threading.Lock()
        while True:
            resolved_db_col = self.ctr_mongodb_dao.get_ctr_collection()
            self._do_update_cache(resolved_db_col)
            time.sleep(5)

    def _do_update_cache(self, resolved_db_col):
        for each in resolved_db_col:
            ad_id_cvr = self.cached_db.get(each["adId"], None)
            if ad_id_cvr is None or ad_id_cvr != each["estimatedCVR"]:
                self.cached_db[each["adId"]] = each["estimatedCVR"]
