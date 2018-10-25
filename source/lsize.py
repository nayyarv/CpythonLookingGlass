from matplotlib import pyplot as plt
from matplotlib import style
style.use("ggplot")
import numpy as np

def list_size(n):
    return n + (n >>3) + (3 if n < 9 else 6)

def np_list_size(n):
    adds = 3*(n < 9) + 6 * (n >= 9)
    return n + (n  >> 3) + adds

if __name__ == '__main__':
    N = 10000
    x = np.arange(0, N, 10)
    y = np_list_size(x)

    print(x)
    print(y)
    print(y-x)
    plt.plot(x, y)
    plt.plot(x,x)
    plt.plot(x, y-x)
    plt.show()
