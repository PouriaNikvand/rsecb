import json
from abc import ABC

import prometheus_client
from tornado.web import RequestHandler

from rsecb.src.manager.api_manager import ApiManager


class AdaptorApiController(RequestHandler, ABC):
    def __init__(self):
        super().__init__()
        self.manager = ApiManager()

    def post(self):
        data = json.loads(self.request.body)
        res = self.manager.process_data(data)
        return res

    def get(self):
        res = [prometheus_client.generate_latest(self.manager.TL1), ]
        return res
