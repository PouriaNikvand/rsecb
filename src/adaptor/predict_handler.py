import json
from abc import ABC
from src.adaptor.adaptor_api_controller import AdaptorApiController

""" Author: Pouria Nikvand """


class Predict(AdaptorApiController, ABC):
    """
    This class moderate the predict path for the api
    """

    def post(self):
        add_id_dict = json.loads(self.request.body)
        try:
            if add_id_dict.get('adId', None) is None:
                raise Exception
            else:
                res = self.manager.find_estimated_ctr(add_id_dict)
        except Exception as e:
            print("bad request", e)
            self.set_status(400)
            res = "bad request"
        return self._response(json.dumps(res))
