import numpy as np
import math
import time

for i in range(0, 361, 30):
    radian = math.radians(i)
    print("sin {} = {}".format(i, np.sin(radian)))
    time.sleep(0.5)

if __name__ == "__main__":
    pass
