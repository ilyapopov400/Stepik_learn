class ConnectionError(Exception):
    pass


class DatabaseConnection:
    def __enter__(self):
        print("Run database")
        return self

    def connect(self, login, password):
        self._fl_connection_open = True
        raise ConnectionError

    def close(self):
        self._fl_connection_open = False

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Close database")
        self.close()


if __name__ == "__main__":
    c = DatabaseConnection()
    try:
        c.connect('aaa', 'bbb')
    except ConnectionError:
        assert c._fl_connection_open
    else:
        assert False, "не сгенерировалось исключение ConnectionError"
    try:
        with DatabaseConnection() as conn:
            conn.connect('aaa', 'bbb')
    except ConnectionError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ConnectionError"
    assert conn._fl_connection_open == False, "атрибут _fl_connection_open принимает значение True, а должно быть False"
