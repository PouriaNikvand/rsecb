import json
from abc import ABC

from src.adaptor.adaptor_api_controller import AdaptorApiController


class Predict(AdaptorApiController, ABC):
    def post(self):
        ad_id_list = json.loads(self.request.body)
        res = self.manager.find_estimated_ctr(ad_id_list)
        return self._response(json.dumps(res))
