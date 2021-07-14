from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from src.config.runtime_config import RuntimeConfig
from src.adaptor.predict_handler import Predict
from src.adaptor.stats_handler import Stats


def make_app():
    urls = [("/predict", Predict),
            ("/stats", Stats)
            ]
    return Application(urls, debug=True)


if __name__ == '__main__':
    RuntimeConfig.configure()
    app = make_app()
    app.listen(RuntimeConfig.SERVICE_PORT)
    print('rsecb webserver is started')
    IOLoop.instance().start()
