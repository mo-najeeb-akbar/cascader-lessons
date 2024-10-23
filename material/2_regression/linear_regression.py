import numpy as np
import matplotlib.pyplot as plt
from functools import partial


def make_noisy_data(fn, num_samples, x_min, x_max):
    x = np.linspace(x_min, x_max, num_samples)
    y = fn(x)
    mag = np.mean(y) / 5.
    noise = np.random.normal(0, mag, num_samples)
    y = y + noise

    return x, y


"""
Useful code snippets:
    - get the mean of an array:: avg = np.mean(my_arr)

    - for loop for 10 times::
    for k in range(10):
        do_something

"""


def line(x, a, b):
    return a * x + b


def line_grad_sqerr(x, y_true, a, b):
    # (ax + b - y)^2
    # d/da = ???
    # d/db = ???
    pass


if __name__ == "__main__":
    a_true = 10
    b_true = -20

    x, y_true = make_noisy_data(partial(line, a=a_true, b=b_true), 100, 0, 10)
    plt.scatter(x, y_true)
    plt.show()
