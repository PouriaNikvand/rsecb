import json
from abc import ABC
import prometheus_client
from tornado.escape import utf8

from src.adaptor.adaptor_api_controller import AdaptorApiController


class Stats(AdaptorApiController, ABC):
    def get(self):
        res = [
            prometheus_client.generate_latest(self.manager.TL1),
            prometheus_client.generate_latest(self.manager.TL2),
        ]
        self._response(res)
