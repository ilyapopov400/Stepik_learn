import dearpygui.dearpygui as dpg

from cpu_view import StatisticsCPU

dpg.create_context()
dpg.create_viewport(title='Тестовое задание для DeleteAm', width=600, height=300)


def button_callback():
    with dpg.window(label="CPU"):
        data_cpu = StatisticsCPU()
        dpg.add_text("CPU: {}".format(data_cpu.cpu))
        dpg.add_text("RUM: {}".format(data_cpu.ram))
        print("Hello World!!!")
        print("CPU: {}, RAM: {}".format(data_cpu.cpu, data_cpu.ram))
        print("----------------")


if __name__ == "__main__":
    with dpg.window(label="Window of CPU"):
        dpg.add_text("System boot information")
        dpg.add_button(label="Start", callback=button_callback)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
