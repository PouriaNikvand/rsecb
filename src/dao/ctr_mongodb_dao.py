from src.dao.base_mongodb_dao import BaseMongodbDao
from src.config.runtime_config import RuntimeConfig


class CTRMongodbDao(BaseMongodbDao):
    def __init__(self):
        super().__init__(
            RuntimeConfig.MONGODB_ADDRESS,
            RuntimeConfig.MONGODB_PORT,
            RuntimeConfig.MONGODB_DB_NAME,
            RuntimeConfig.MONGODB_COLLECTION_NAME
        )

    def get_ctr_ad_id(self, ad_id: int):
        return self.find(self.db[RuntimeConfig.CTR_COLLECTION_NAME],
                         {"adId": str(ad_id)},
                         {'estimatedCVR': 1})
