class ValidatorString:
    def __init__(self, min_length: int, max_length: int, chars: str):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if not isinstance(string, str):
            raise ValueError('недопустимая строка')
        if not bool(self.chars):
            return
        if not (len(string) in range(self.min_length, self.max_length + 1)):
            raise ValueError('недопустимая строка')
        if not bool(
                set(string) & set(self.chars)
        ):
            raise ValueError('недопустимая строка')


class LoginForm:  # TODO
    def __init__(self, login_validator: ValidatorString, password_validator: ValidatorString):
        self.login_validator = login_validator
        self.password_validator = password_validator

    @staticmethod
    def __validate_request(date: dict):
        if not isinstance(date, dict):
            raise TypeError('not type dict')
        if "login" not in date or "password" not in date:
            raise TypeError('в запросе отсутствует логин или пароль')

    def form(self, request: dict):
        self.__validate_request(date=request)

        login = request.get("login")
        password = request.get("password")

        self.login_validator.is_valid(login)
        self.password_validator.is_valid(password)

        self._login = login
        self._password = password


if __name__ == "__main__":
    login_v = ValidatorString(4, 50, "")
    password_v = ValidatorString(10, 50, "!$#@%&?")
    lg = LoginForm(login_v, password_v)
    login, password = input().split()
    try:
        lg.form({'login': login, 'password': password})
    except (TypeError, ValueError) as e:
        print(e)
    else:
        print(lg._login)
