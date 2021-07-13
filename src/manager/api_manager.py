from prometheus_client import Summary


class ApiManager:
    TL1 = Summary('params', 'Time spent some processing request')

    def process_data(self, data):
        pass
