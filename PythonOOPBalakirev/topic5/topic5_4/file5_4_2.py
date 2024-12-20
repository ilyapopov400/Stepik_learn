class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if kwargs:
            key = list(kwargs.keys())[0]
            value = kwargs.get(key)
            self.__setattr__(key, value)

    def __repr__(self):
        if self.__dict__:
            key = list(self.__dict__.keys())[0]
            value = self.__getattribute__(key)
            return "Значение первичного ключа {} = {} недопустимо".format(key, value)
        return "Первичный ключ должен быть целым неотрицательным числом"

    def __str__(self):
        if self.__dict__:
            key = list(self.__dict__.keys())[0]
            value = self.__getattribute__(key)
            return "Значение первичного ключа {} = {} недопустимо".format(key, value)
        return "Первичный ключ должен быть целым неотрицательным числом"


if __name__ == "__main__":
    error = PrimaryKeyError(id="-10.5")

    try:
        print("Hello World!!!")
        # здесь команда для генерации исключения
        raise error
    except PrimaryKeyError as ex:
        print(ex)
