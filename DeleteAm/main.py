"""
- установлен PyGUI
"""
import time
import dearpygui.dearpygui as dpg

from cpu_view import StatisticsCPU
from db import DataLogs

dpg.create_context()
dpg.create_viewport(title='Тестовое задание для DeleteAm', width=600, height=300)
dpg.setup_dearpygui()


def start_writing_logs():
    """
    - функция для записи логов
    :return:
    """
    while True:
        data_cpu = StatisticsCPU()
        cpu, ram, date_time = data_cpu.cpu, data_cpu.ram, str(
            time.strftime("%x %X")
        )
        print("Начата запись логов: {}, {}, {}".format(date_time, cpu, ram))
        with DataLogs as db:  # TODO
            db = DataLogs()
            db(date_time, cpu, ram)
            time.sleep(3)


if __name__ == "__main__":
    dpg.show_viewport()

    with dpg.window(label="Window of CPU"):
        dpg.add_text("System boot information")

        data_cpu = StatisticsCPU()
        cpu, ram = data_cpu.cpu, data_cpu.ram
        dpg.add_text("CPU: {}%".format(cpu))
        dpg.add_text("RUM: {}%".format(ram))

        print("CPU: {}, RAM: {}".format(data_cpu.cpu, data_cpu.ram))
        print("----------------")

        dpg.add_button(label="Start writing logs", callback=start_writing_logs)

    dpg.start_dearpygui()
    dpg.destroy_context()
