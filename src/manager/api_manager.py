from prometheus_client import Summary, Histogram
from src.dao.ctr_mongodb_dao import CTRMongodbDao


class ApiManager:
    TL1 = Summary('params', 'Time spent some processing request')
    TL2 = Histogram('params2', 'Time spent some processing request')

    def __init__(self):
        self.ctr_mongodb_dao = CTRMongodbDao()

    @TL1.time()
    @TL2.time()
    def find_estimated_ctr(self, add_id_list: dict) -> dict:
        result = dict()
        for each_id in add_id_list['adId']:
            each_ecvr = self.ctr_mongodb_dao.get_ctr_ad_id(each_id)
            if len(each_ecvr) == 1:
                result[each_id] = each_ecvr[0]
        return result
