class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:
    def __init__(self, path: str, router_cls: Router):
        self.__path = path
        self.__router_cls = router_cls

    def __call__(self, func):
        self.__router_cls.add_callback(path=self.__path, func=func)
        return func


if __name__ == "__main__":
    @Callback('/', Router)
    def index():
        return '<h1>Главная</h1>'


    route = Router.get('/')
    if route:
        ret = route()
        print(ret)
