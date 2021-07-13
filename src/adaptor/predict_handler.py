import json
from abc import ABC

import prometheus_client

from src.adaptor.adaptor_api_controller import AdaptorApiController


class Predict(AdaptorApiController, ABC):
    def __init__(self):
        super().__init__()

    def post(self):
        data = json.loads(self.request.body)
        res = self.manager.process_data(data)
        return res

    def get(self):
        pass

