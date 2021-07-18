from prometheus_client import Summary, Histogram

from src.config.runtime_config import RuntimeConfig
from src.arch.singletone import Singleton
from src.manager.cache_manager import CacheManager

""" Author: Pouria Nikvand """


class ApiManager(CacheManager, metaclass=Singleton):
    """
    This Class contains the main methods for the project
    This service returns the ctr from mongodb for each ad_id it received from user

    methods:
    find_estimated_ctr : returns the ctr for the list of input ad_id
    get_cached_ctr : check if the ad_id available on cached_db

    TL1 , TL2 are the prometheus parameters defined for monitoring the service
    """

    TL1 = Summary('Summery', 'Summery spent some processing request')
    TL2 = Histogram('Histogram', 'Histogram spent some processing request')

    def __init__(self):
        super().__init__()

    @TL1.time()
    @TL2.time()
    def find_estimated_ctr(self, add_id_dict: dict) -> dict:
        result = dict()
        for each_id in set(add_id_dict['adId']):
            cached_ad_id_ctr = self.cached_db.get(each_id, None)
            if cached_ad_id_ctr is not None:
                result[each_id] = cached_ad_id_ctr
                continue
            else:
                each_ctr = self.ctr_mongodb_dao.get_ctr_ad_id(each_id)
                # we assume that there is no duplicate for ad_id as a key
                if each_ctr:
                    result[each_id] = each_ctr[0]
                    self.cached_db[each_id] = each_ctr[0]
                else:
                    if isinstance(each_ctr, list):
                        print('ad_id ' + str(each_id) + ' not found')
                    result[each_id] = RuntimeConfig.DEFAULT_NOT_FOUND_CTR_VALUE

        return result
