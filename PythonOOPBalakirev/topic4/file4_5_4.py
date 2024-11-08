from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    @staticmethod
    def get_info():
        return "Базовый класс Model"


class ModelForm(Model):
    def __init__(self, login: str, password: str):
        self._login = login
        self._password = password
        self._id = hash(self)

    def get_pk(self):
        return str(self._id)


if __name__ == "__main__":
    form = ModelForm("Логин", "Пароль")
    print(form.get_pk())
