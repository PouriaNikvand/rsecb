import json

import prometheus_client

from src.adaptor.adaptor_api_controller import AdaptorApiController


class Predict(AdaptorApiController):
    def __init__(self):
        super().__init__()

    def post(self):
        data = json.loads(self.request.body)
        res = self.manager.process_data(data)
        return res

    def get(self):
        res = [prometheus_client.generate_latest(self.manager.TL1), ]
        return res


class Stats(AdaptorApiController):
    def __init__(self):
        super().__init__()

    def post(self):
        data = json.loads(self.request.body)
        res = self.manager.process_data(data)
        return res

    def get(self):
        res = [prometheus_client.generate_latest(self.manager.TL1), ]
        return res
