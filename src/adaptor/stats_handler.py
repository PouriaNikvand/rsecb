import json
from abc import ABC

import prometheus_client
import tornado.web

from src.adaptor.adaptor_api_controller import AdaptorApiController


class Stats(AdaptorApiController, ABC):
    def get(self):
        res = [prometheus_client.generate_latest(self.manager.TL1), ]
        # res = json.dump(res)
        self._response(res)

    def _response(self, res):
        self.write(res[0])
        self.finish()