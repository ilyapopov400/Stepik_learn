from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def go(self):
        """Метод для перемещения транспортного средства"""

    @property
    @abstractmethod
    def speed(self):
        """Абстрактный объект-свойство"""


class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        """
        - абстрактное свойство (property), название страны (строка)
        """

    @property
    @abstractmethod
    def population(self):
        """
        - абстрактное свойство (property), численность населения (целое положительное число)
        """

    @property
    @abstractmethod
    def square(self):
        """
        - абстрактное свойство (property), площадь страны (положительное число)
        """

    @abstractmethod
    def get_info(self):
        """
        - абстрактный метод для получения сводной информации о стране
        """


class Country(CountryInterface):
    def __init__(self, name: str, population: int, square: float):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population: int):
        self._population = population

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, square: float):
        self._square = square

    def get_info(self):
        return "{}: {}, {}".format(self._name, self._square, self._population)


if __name__ == "__main__":
    country = Country("Россия", 140000000, 324005489.55)
    name = country.name
    pop = country.population
    country.population = 150000000
    country.square = 354005483.0
    print(country.get_info())  # Россия: 354005483.0, 150000000
