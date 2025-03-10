import time
import datetime
import os
import hello_world.settings


class Logs:
    def __init__(self):
        self.path_logs = "logs.log"

    def __call__(self):
        path1 = hello_world.settings.BASE_DIR
        path = os.path.join(path1, self.path_logs)

        with open(file=path, mode="a", encoding="utf-8") as f:
            text = str(datetime.datetime.now().strftime('%Y-%m-%d: %H:%M:%S')) + "\n"
            f.write(text)


if __name__ == "__main__":
    Logs()()
