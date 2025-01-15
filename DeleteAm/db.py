import sqlite3


class DataLogs:
    def __init__(self):
        self.con = sqlite3.connect('log.db')

        # открываем базу
        with self.con:
            # получаем количество таблиц с нужным нам именем
            data = self.con.execute("select count(*) from sqlite_master where type='table' and name='logs'")
            for row in data:
                # если таких таблиц нет
                if row[0] == 0:
                    # создаём таблицу для товаров
                    with self.con:
                        self.con.execute("""
                            CREATE TABLE logs (
                                data_time TEXT,
                                cpu REAL,
                                ram REAL
                            );
                        """)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(exc_type)
            self.__del__()
        return False

    def __call__(self, data_time: str, cpu: float, ram: float):
        """
        - записываем данные в таблицу
        :param data_time:
        :param cpu:
        :param ram:
        :return:
        """
        self.con = sqlite3.connect('log.db')

        # открываем базу
        with self.con:
            # получаем количество таблиц с нужным нам именем
            data = self.con.execute("select count(*) from sqlite_master where type='table' and name='logs'")
            for row in data:
                # если таких таблиц нет
                if row[0] == 0:
                    # создаём таблицу для товаров
                    with self.con:
                        self.con.execute("""
                                    CREATE TABLE logs (
                                        data_time TEXT,
                                        cpu REAL,
                                        ram REAL
                                    );
                                """)
        # подготавливаем множественный запрос
        sql = 'INSERT INTO logs (data_time, cpu, ram) values(?, ?, ?)'
        # указываем данные для запроса
        data = [
            (data_time, cpu, ram),

        ]

        # добавляем с помощью множественного запроса все данные сразу
        with self.con:
            self.con.executemany(sql, data)

    def __repr__(self):
        result = list()
        with self.con:
            data = self.con.execute("SELECT * FROM logs")
            for row in data:
                result.append(str(row))
        result = "\n".join(result)
        return result

    def __del__(self):
        self.con.close()


if __name__ == "__main__":
    db = DataLogs()
    # db("Hello", 1, 2)
    print(db)
