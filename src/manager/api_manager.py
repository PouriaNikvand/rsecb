from prometheus_client import Summary

from src.dao.ctr_mongodb_dao import CTRMongodbDao


class ApiManager:
    TL1 = Summary('params', 'Time spent some processing request')

    def __init__(self):
        self.ctr_mongodb_dao = CTRMongodbDao()

    @TL1.time()
    def find_ctr(self, add_id_list: list):
        for each_id in add_id_list:
            print(self.ctr_mongodb_dao.get_ctr_ad_id(each_id))
