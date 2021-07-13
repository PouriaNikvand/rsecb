import json
from abc import ABC

import prometheus_client
from tornado.web import RequestHandler

from rsecb.src.manager.api_manager import ApiManager


class AdaptorApiController(RequestHandler, ABC):
    def __init__(self):
        super().__init__()
        self.manager = ApiManager()

