from abc import ABC
from tornado.web import RequestHandler

from src.manager.api_manager import ApiManager


class AdaptorApiController(RequestHandler, ABC):
    manager = ApiManager()

