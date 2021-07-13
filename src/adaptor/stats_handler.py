from abc import ABC

import prometheus_client

from src.adaptor.adaptor_api_controller import AdaptorApiController


class Stats(AdaptorApiController, ABC):
    def __init__(self):
        super().__init__()

    def post(self):
        pass

    def get(self):
        res = [prometheus_client.generate_latest(self.manager.TL1), ]
        return res
