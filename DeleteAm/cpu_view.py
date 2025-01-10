import psutil


class StatisticsCPU:
    def __init__(self):
        """
        - self.__cpu: Загрузка CPU
        - self.__ram: Использование RAM
        """
        self.__cpu = psutil.cpu_percent()
        self.__ram = psutil.virtual_memory().percent

    @property
    def cpu(self):
        return psutil.cpu_percent()

    @property
    def ram(self):
        return psutil.virtual_memory().percent


if __name__ == "__main__":
    print(f"Загрузка CPU: {psutil.cpu_percent()}%")
    print(f"Использование RAM: {psutil.virtual_memory().percent}%")
    python_process = psutil.Process()
    print(f"RAM, используемая Python-процессом: {python_process.memory_info()[0] / 2. ** 30:.2f} GB")

    a = StatisticsCPU()
    for _ in range(10):
        print(f"Загрузка CPU: {a.cpu}%")
        print(f"Использование RAM: {a.ram}%")
