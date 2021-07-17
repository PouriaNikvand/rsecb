from src.dao.base_mongodb_dao import BaseMongodbDao
from src.config.runtime_config import RuntimeConfig

""" Author: Pouria Nikvand """


class CTRMongodbDao(BaseMongodbDao):
    """
    CTR methods using mongodb connection for accessing the collection and read as the project wants

    methods :
    get_ctr_ad_id gets an ad_id and returns the estimatedCVR in the database and from the CTR collection
    get_ctr_collection : this method returns the whole ctr collection from the database
    """

    def __init__(self):
        super().__init__(
            host=RuntimeConfig.MONGODB_ADDRESS,
            port=RuntimeConfig.MONGODB_PORT,
            database_name=RuntimeConfig.MONGODB_DB_NAME,
            user=RuntimeConfig.MONGODB_USER,
            key=RuntimeConfig.MONGODB_KEY,
            collection_name=RuntimeConfig.CTR_COLLECTION_NAME,
            serverSelectionTimeoutMS=RuntimeConfig.SERVER_SELECTOPM_TIMEOUT
        )

    def get_ctr_ad_id(self, ad_id: int):
        return self.find({"adId": ad_id},
                         {'_id': 0, 'estimatedCVR': 1})

    def get_ctr_collection(self):
        return self.find({},
                         {'_id': 0, "adId": 1, 'estimatedCVR': 1})
