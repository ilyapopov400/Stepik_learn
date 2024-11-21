class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value: float, max_value: float):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data) -> bool:
        if not isinstance(data, float) or not (self.min_value <= data <= self.max_value):
            return False
        return True

    def __call__(self, data):
        result = self._is_valid(data=data)
        return result


if __name__ == "__main__":
    float_validator = FloatValidator(0, 10.5)

    assert hasattr(float_validator, '_is_valid') is True, "Error"

    res_1 = float_validator(1)  # False (целое число, а не вещественное)
    assert res_1 is False, "Error"

    res_2 = float_validator(1.0)  # True
    assert res_2 is True, "Error"

    res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])
    assert res_3 is False, "Error"
