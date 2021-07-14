from src.dao.base_mongodb_dao import BaseMongodbDao
from src.config.runtime_config import RuntimeConfig


class CTRMongodbDao(BaseMongodbDao):
    def __init__(self):
        super().__init__(
            host=RuntimeConfig.MONGODB_ADDRESS,
            port=RuntimeConfig.MONGODB_PORT,
            database_name=RuntimeConfig.MONGODB_DB_NAME,
            user=RuntimeConfig.MONGODB_USER,
            key=RuntimeConfig.MONGODB_KEY,
            collection_name=RuntimeConfig.MONGODB_COLLECTION_NAME
        )

    def get_ctr_ad_id(self, ad_id: int):
        return self.find(self.db[RuntimeConfig.CTR_COLLECTION_NAME],
                         {"adId": ad_id},
                         {'_id': 0, 'estimatedCVR': 1})
