from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from rsecb.src.config.runtime_config import RuntimeConfig
from rsecb.src.adaptor.adaptor_api_controller import AdaptorApiController


def make_app():
    urls = [("/predict", AdaptorApiController),
            ("/stats", AdaptorApiController)
            ]
    return Application(urls)


if __name__ == '__main__':
    RuntimeConfig.configure()
    app = make_app()
    app.listen(RuntimeConfig.SERVICE_PORT)
    IOLoop.instance().start()
