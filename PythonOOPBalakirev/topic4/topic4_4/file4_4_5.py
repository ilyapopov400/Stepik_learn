vector_log = []


def class_log(log_lst):
    def wrapper(cls):
        for k, v in cls.__dict__.items():
            if callable(v):
                setattr(cls, k, log_method_decorator(v))
        return cls

    def log_method_decorator(func):
        def wrapper(*args, **kwargs):
            log_lst.append(func.__name__)
            return func(*args, **kwargs)

        return wrapper

    return wrapper


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


if __name__ == "__main__":
    v = Vector(1, 2, 3)
    v[0] = 10

    print(vector_log)
