from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from rsecb.src.config.runtime_config import RuntimeConfig
from rsecb.src.adaptor.predict_handler import Predict
from rsecb.src.adaptor.predict_handler import Stats


def make_app():
    urls = [("/predict", Predict),
            ("/stats", Stats)
            ]
    return Application(urls)


if __name__ == '__main__':
    RuntimeConfig.configure()
    app = make_app()
    app.listen(RuntimeConfig.SERVICE_PORT)
    IOLoop.instance().start()
