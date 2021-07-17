from abc import ABC
from typing import Union
from tornado.web import RequestHandler
from src.manager.api_manager import ApiManager

""" Author: Pouria Nikvand """


class AdaptorApiController(RequestHandler, ABC):
    """
    This method is for overwriting the base methods from Request Handler
    And main methods and objects share with all instances for service paths
    """
    manager = ApiManager()

    def _response(self, res: Union[list, bytes, str]):
        self.set_header("Content-Type", "text/plain")
        if isinstance(res, list):
            for each in res:
                self.write(each)
        else:
            self.write(res)
        self.finish()
