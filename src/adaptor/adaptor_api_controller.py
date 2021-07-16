from abc import ABC
from typing import Union

from tornado.web import RequestHandler

from src.manager.api_manager import ApiManager


class AdaptorApiController(RequestHandler, ABC):
    manager = ApiManager()

    def _response(self, res: Union[list, bytes, str]):
        self.set_header("Content-Type", "text/plain")
        if isinstance(res, list):
            for each in res:
                self.write(each)
        else:
            self.write(res)
        self.finish()
