class Aircraft:
    """
    самолет
    """

    def __init__(self, model: str, mass: (int, float), speed: (int, float), top: (int, float)):
        self._date_validator(model, mass, speed, top)
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    @staticmethod
    def _date_validator(model, mass, speed, top):
        if not isinstance(model, str):
            raise TypeError('неверный тип аргумента')
        for date in (mass, speed, top):
            if not isinstance(date, (int, float)) or date < 0:
                raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):
    """
    пассажирский самолет
    """

    def __init__(self, model: str, mass: int, speed: int, top: int, chairs: int):
        super().__init__(model, mass, speed, top)
        if not isinstance(chairs, int):
            raise TypeError('неверный тип аргумента')
        self._chairs = chairs


class WarPlane(Aircraft):
    """
    военный самолет
    """

    def __init__(self, model: str, mass: int, speed: int, top: int, weapons: dict):
        super().__init__(model, mass, speed, top)
        if not isinstance(weapons, dict):
            raise TypeError('неверный тип аргумента')
        self._weapons = weapons


if __name__ == "__main__":
    planes = [
        PassengerAircraft("МС-21", 1250, 8000, 12000.5, 140),
        PassengerAircraft("SuperJet", 1145, 8640, 11034, 80),
        WarPlane("Миг-35", 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
        WarPlane("Су-35", 7034, 34000, 2400, {"ракета": 4, "бомба": 7}),
    ]
