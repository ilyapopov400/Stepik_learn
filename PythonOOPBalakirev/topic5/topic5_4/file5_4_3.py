import re
from datetime import datetime


class DateError(Exception):
    """
    - класс-исключения, унаследованный от класса Exception
    """


class DateString:
    def __init__(self, date_string: str):
        """

        :param date_string: - строка с датой в формате "DD.MM.YYYY"
        здесь DD - день (целое число от 1 до 31);
        MM - месяц (целое число от 1 до 12);
        YYYY - год (целое число от 1 до 3000)
        """
        self.__validate_date(date=date_string)
        self.date_string = self.__creater_date_string(date_string)

    @staticmethod
    def __validate_date(date: str):
        if not isinstance(date, str):
            raise DateError

        pattern = r'\d{1,2}\.\d{1,2}\.\d{1,4}'
        result = re.findall(pattern=pattern, string=date)
        if not result:
            raise DateError
        day, month, year = int(result[0].split(".")[0]), int(result[0].split(".")[1]), int(result[0].split(".")[2])

        if 1 > year < 3000:
            raise DateError

        try:
            datetime.strptime(date, "%d.%m.%Y").date()
        except ValueError:
            raise DateError

    @staticmethod
    def __creater_date_string(date_string: str) -> str:
        date_object = datetime.strptime(date_string, "%d.%m.%Y").date()
        result = date_object.strftime("%d.%m.%Y")

        return result

    def __str__(self):
        return self.date_string


if __name__ == "__main__":
    try:
        # date_string = input()
        date_string = "1.2.1812"
        date = DateString(date_string=date_string)

        print(date)  # date - объект класса DateString
    except DateError:
        print("Неверный формат даты")
