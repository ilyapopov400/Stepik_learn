class FloatValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __repr__(self):
        return "{}({}-{})".format(self.__class__.__name__, self.min_value, self.max_value)

    def __validate_value(self, value):
        if not isinstance(value, float) or (self.min_value <= value <= self.max_value) is False:
            raise ValueError('значение не прошло валидацию')

    def __call__(self, value):
        self.__validate_value(value=value)


class IntegerValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __repr__(self):
        return "{}({}-{})".format(self.__class__.__name__, self.min_value, self.max_value)

    def __validate_value(self, value):
        if isinstance(value, bool) or not isinstance(value, int) or (self.min_value <= value <= self.max_value) is False:
            raise ValueError('значение не прошло валидацию')

    def __call__(self, value):
        self.__validate_value(value=value)


def is_valid(lst: list, validators: [FloatValidator, IntegerValidator]):
    result = list()
    for date in lst:
        for validate in validators:
            try:
                # print(date, validate)
                validate(date)
                result.append(date)
            except ValueError:
                continue
    return result


if __name__ == "__main__":
    fv = FloatValidator(0, 10.5)
    iv = IntegerValidator(-10, 20)
    lst_out = is_valid(lst=[1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]
    print(lst_out)
