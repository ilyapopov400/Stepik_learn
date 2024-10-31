CURRENT_OS = 'windows'  # 'windows', 'linux'


class FileDialogFactory:
    def __new__(cls, title: str, path: str, exts: tuple):
        if CURRENT_OS == 'windows':
            return cls.create_windows_filedialog(title, path, exts)
        return cls.create_linux_filedialog(title, path, exts)

    @staticmethod
    def create_windows_filedialog(title, path, exts):
        """
        - для создания объектов класса WindowsFileDialog
        """
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        """
        - для создания объектов класса LinuxFileDialog
        """
        return LinuxFileDialog(title, path, exts)


class WindowsFileDialog:
    def __init__(self, title: str, path: str, exts: tuple):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title: str, path: str, exts: tuple):
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


if __name__ == "__main__":
    title, path, exts = 'Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png')
    dlg = FileDialogFactory(title, path, exts)
    print(dlg)
