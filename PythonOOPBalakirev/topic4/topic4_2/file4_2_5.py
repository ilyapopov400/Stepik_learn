class VideoItem:
    def __init__(self, title: str, descr: str, path: str):
        """

        :param title:  заголовок видео (строка)
        :param descr:  описание видео (строка)
        :param path:  путь к видеофайлу
        """
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        if rating not in range(0, 6):
            raise ValueError('неверное присваиваемое значение')
        self.__rating = rating


if __name__ == "__main__":
    v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
    print(v.rating.rating)  # 0
    v.rating.rating = 5
    print(v.rating.rating)  # 5
    title = v.title
    descr = v.descr
    try:
        v.rating.rating = 6  # ValueError
    except ValueError:
        assert True, "исключение ValueError"
