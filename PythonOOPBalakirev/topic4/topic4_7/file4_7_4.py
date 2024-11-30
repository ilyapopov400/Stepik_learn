class Note:
    def __init__(self, name: str, ton: int = 0):
        self.validate_name(date=name)
        self.validate_ton(date=ton)
        self._name = name
        self._ton = ton

    def __repr__(self):
        return "{}:{}".format(self._name, self._ton)

    @staticmethod
    def validate_name(date):
        if not isinstance(date, str) or date not in ("до", "ре", "ми", "фа", "соль", "ля", "си"):
            raise ValueError('недопустимое значение аргумента')

    @staticmethod
    def validate_ton(date):
        if not isinstance(date, int) or date not in range(-1, 2):
            raise ValueError('недопустимое значение аргумента')

    def __setattr__(self, name, value):
        if name == "_name":
            self.validate_name(date=value)
        if name == "_ton":
            self.validate_ton(date=value)
        super().__setattr__(name, value)


class Notes:
    __slots__ = ("_do", "_re", "_mi", "_fa", "_solt", "_la", "_si",)

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Notes, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._do = Note("до")
        self._re = Note("ре")
        self._mi = Note("ми")
        self._fa = Note("фа")
        self._solt = Note("соль")
        self._la = Note("ля")
        self._si = Note("си")

    def __repr__(self):
        result = "{}, {}, {}, {}, {}, {}, {}".format(self._do, self._re, self._mi, self._fa, self._solt, self._la,
                                                     self._si)
        return result

    def __getitem__(self, item):
        if not isinstance(item, int) or item not in range(7):
            raise IndexError('недопустимый индекс')
        name_attr = self.__slots__[item]
        result = getattr(self, name_attr)
        return result


if __name__ == "__main__":
    notes = Notes()
    nota = notes[2]  # ссылка на ноту ми
    print(nota)

    print(type(notes[3]), notes[3])
    notes[3]._ton = 1  # изменение тональности ноты фа
    print(notes[3])
    print(notes)
