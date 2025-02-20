class CleanDate:
    """
    - при вызове экземпляра класса возвращает True если проверка прошла и наоборот
    """

    def __init__(self, username: str, first_name: str, last_name: str, email: str, password1: str, password2: str):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password1 = password1
        self.password2 = password2

    def verification(self):
        if not all(
                map(lambda x: bool(x) is True,
                    (self.username, self.first_name, self.last_name, self.email, self.password1, self.password2))
        ):
            return True

        return not self.password1 == self.password2

    def __call__(self):
        return not self.verification()


if __name__ == "__main__":
    a = CleanDate(username="q", first_name="q", last_name="e", email="r", password1="t", password2="t")
    print(a())
