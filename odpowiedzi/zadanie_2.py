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

    # plot results
    plt.plot(arr_x, arr_y, "g")
    plt.show()


# basic function dependent only on x
def f1(x):
    f = -x / 10
    return f


if __name__ == "__main__":
    main()
