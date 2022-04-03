import numpy as np
import matplotlib.pyplot as plt


def main():

    delta_x = 0.15
    initial_value = 2.5
    x_max = 10

    # compute approximated function
    arr_x = np.arange(0, x_max + delta_x, step=delta_x)
    arr_y = np.zeros(arr_x.shape)

    arr_y[0] = initial_value

    for i in range(1, len(arr_x)):
        arr_y[i] = arr_y[i - 1] + f4(arr_x[i - 1], arr_y[i - 1]) * delta_x

    # compute approximated function with Heun's method
    heun_x = np.arange(0, x_max + delta_x, step=delta_x)
    heun_y = np.zeros(arr_x.shape)

    heun_y[0] = initial_value

    for i in range(1, len(heun_x)):
        heun_y[i] = heun_step(f4, heun_x[i - 1], heun_y[i - 1], delta_x)

    # compute very precise approximation
    ref_x = np.arange(0, x_max, step=0.001)
    ref_y = np.empty(ref_x.shape)

    ref_y[0] = initial_value

    for i in range(1, len(ref_x)):
        ref_y[i] = ref_y[i - 1] + f4(ref_x[i - 1], ref_y[i - 1]) * 0.001

    # plot results
    plt.plot(ref_x, ref_y, "k")
    plt.plot(arr_x, arr_y, "g")
    plt.plot(heun_x, heun_y, "r")
    plt.show()


def heun_step(f, x, y, delta_x):
    k1 = f(x, y)
    k2 = f(x + delta_x, y + k1 * delta_x)
    y_pred = y + 0.5 * delta_x * (k1 + k2)
    return y_pred


# simple function with only x dependency
def f1(x):
    f = -x / 10
    return f


# complex function with only x dependency
def f2(x):
    x = (x - 5) * 2
    f = -1 - ((x**4 * (1 - np.exp(-x) + np.exp(x))) / (
        (np.exp(-x) + np.exp(x) + x)**2)) + ((4 * x**3) /
                                             (np.exp(-x) + np.exp(x) + x))
    return f


# simple function with y dependecy (Newton's Law of cooling)
def f3(y):
    k = 0.003  # heat transfer coefficient
    Tr = 20  # temperature of environment
    f = -k * (y - Tr)
    return f


def f4(x, y):
    f = x**2 - y**2
    return f


if __name__ == "__main__":
    main()
