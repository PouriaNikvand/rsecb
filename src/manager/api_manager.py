from prometheus_client import Summary, Histogram
from src.dao.ctr_mongodb_dao import CTRMongodbDao
from src.arch.singletone import Singleton


class ApiManager(metaclass=Singleton):
    TL1 = Summary('Summery', 'Summery spent some processing request')
    TL2 = Histogram('Histogram', 'Histogram spent some processing request')

    def __init__(self):
        super().__init__()
        self.ctr_mongodb_dao = CTRMongodbDao()
        self.cached_db = {}

    @TL1.time()
    @TL2.time()
    def find_estimated_ctr(self, add_id_list: dict) -> dict:
        result = dict()
        for each_id in add_id_list['adId']:
            cached_ad_id_cvr = self.get_cached_cvr(each_id)
            if cached_ad_id_cvr is not None:
                result[each_id] = cached_ad_id_cvr
                continue
            else:
                each_cvr = self.ctr_mongodb_dao.get_ctr_ad_id(each_id)
                if len(each_cvr) == 1:
                    result[each_id] = each_cvr[0]
                    self.cached_db[each_id] = each_cvr[0]
                else:
                    pass
        return result

    def get_cached_cvr(self, ad_id):
        if ad_id in self.cached_db:
            # we have cached the cvr for the symbol set cvr in a local variable
            return self.cached_db[ad_id]
        return None
