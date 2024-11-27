class Planet:
    def __init__(self, name: str, diametr: float, period_solar: float, period: float):
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period


mercury = Planet("mercury", 4878, 87.97, 1407.5)
venus = Planet("venus", 12104, 224.7, 5832.45)
earth = Planet("earth", 12756, 365.3, 23.93)
mars = Planet("mars", 6794, 687, 24.62)
jupiter = Planet("jupiter", 142800, 4330, 9.9)
saturn = Planet("saturn", 120660, 10753, 10.63)
uranus = Planet("uranus", 51118, 30665, 17.2)
neptune = Planet("neptune", 49528, 60150, 16.1)


class SolarSystem:
    __slots__ = ("_mercury",
                 "_venus",
                 "_earth",
                 "_mars",
                 "_jupiter",
                 "_saturn",
                 "_uranus",
                 "_neptune",)
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SolarSystem, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._mercury = mercury
        self._venus = venus
        self._earth = earth
        self._mars = mars
        self._jupiter = jupiter
        self._saturn = saturn
        self._uranus = uranus
        self._neptune = neptune


if __name__ == "__main__":
    s_system = SolarSystem()
