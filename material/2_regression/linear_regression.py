import numpy as np
import matplotlib.pyplot as plt


def make_noisy_data(fn, num_samples, x_min, x_max):
    x = np.linspace(x_min, x_max, num_samples)
    y = np.log(fn(x))
    noise = np.random.normal(0, .1, num_samples)
    y = np.exp(y + noise)

    return x, y


"""
Useful code snippets:
    - get the mean of an array:: avg = np.mean(my_arr)

    - for loop for 10 times::
    for k in range(10):
        do_something

"""


def line(x, a, b):
    pass


def line_grad_sqerr(x, y_true, a, b):
    # (ax + b - y)^2
    # d/da = ???
    # d/db = ???
    pass


if __name__ == "__main__":
    pass
