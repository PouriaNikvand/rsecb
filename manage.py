from tornado.web import Application
from tornado.ioloop import IOLoop
from src.config.runtime_config import RuntimeConfig
from src.adaptor.predict_handler import Predict
from src.adaptor.stats_handler import Stats
from src.manager.api_manager import ApiManager

""" Author: Pouria Nikvand """


def make_app():
    """
    Returns tornado application using valid urls request paths
    """
    urls = [("/predict", Predict),
            ("/stats", Stats)
            ]
    return Application(urls)


if __name__ == '__main__':
    RuntimeConfig().configure()
    ApiManager()
    app = make_app()
    try:
        app.listen(RuntimeConfig.SERVICE_PORT)
    except ConnectionError as e:
        print("Port is not available at the moment, the error is:")
        print(e)
    print('>>>>>>>>>>>\n>> rsecb webserver is started <<\n>>>>>>>>>>>')
    IOLoop.instance().start()
