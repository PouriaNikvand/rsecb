import time

from tornado.web import Application
from tornado.ioloop import IOLoop
from src.config.runtime_config import RuntimeConfig
from src.adaptor.predict_handler import Predict
from src.adaptor.stats_handler import Stats
from src.manager.api_manager import ApiManager
from src.manager.cache_manager import CacheManager


def make_app():
    urls = [("/predict", Predict),
            ("/stats", Stats)
            ]
    return Application(urls, debug=False)


if __name__ == '__main__':
    RuntimeConfig.configure()
    cm = CacheManager()
    cm.start()
    app = make_app()
    app.listen(RuntimeConfig.SERVICE_PORT)
    print('rsecb webserver is started')
    IOLoop.instance().start()

