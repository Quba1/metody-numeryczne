import numpy as np
import matplotlib.pyplot as plt


def main():

    delta_x = 1
    initial_value = 6
    x_max = 10

    # compute approximated function
    arr_x = np.arange(0, x_max + delta_x, step=delta_x)
    arr_y = np.zeros(arr_x.shape)

    arr_y[0] = initial_value

    for i in range(1, len(arr_x)):
        arr_y[i] = arr_y[i - 1] + f1(arr_x[i - 1]) * delta_x

    # compute very precise approximation
    ref_x = np.arange(0, x_max, step=0.0001)
    ref_y = np.empty(ref_x.shape)

    ref_y[0] = initial_value

    for i in range(1, len(ref_x)):
        ref_y[i] = ref_y[i - 1] + f1(ref_x[i - 1]) * 0.0001

    # plot results
    plt.plot(arr_x, arr_y, "g")
    plt.plot(ref_x, ref_y, "k")
    plt.show()


# basic function dependent only on x
def f1(x):
    f = -x / 10
    return f


if __name__ == "__main__":
    main()
