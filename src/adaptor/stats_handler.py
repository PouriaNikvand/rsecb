from abc import ABC
import prometheus_client
from src.adaptor.adaptor_api_controller import AdaptorApiController

""" Author: Pouria Nikvand """


class Stats(AdaptorApiController, ABC):
    """
    This class moderate the stats path for the api
    """

    def get(self):
        res = [
            prometheus_client.generate_latest(self.manager.TL1),
            prometheus_client.generate_latest(self.manager.TL2),
        ]
        self._response(res)
