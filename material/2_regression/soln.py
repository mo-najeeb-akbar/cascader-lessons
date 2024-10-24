import numpy as np
import matplotlib.pyplot as plt
from functools import partial


def square(x, a, b, c):
    return a * x**2 + b * x + c


def exp(x, a, b):
    return a * np.exp(b * x)


def make_noisy_data(fn, num_samples, x_min, x_max):
    x = np.linspace(x_min, x_max, num_samples)
    y = np.log(fn(x))
    noise = np.random.normal(0, .1, num_samples)
    y = np.exp(y + noise)

    return x, y


def square_grad_sqerr(x, y_true, a, b, c):
    # (ax^2 + bx + c - y)^2
    # d/da = 2(ax^2 + bx + c - y_true) * x^2
    # d/db = 2(ax^2 + bx + c - y_true) * x
    # d/dc = 2(ax^2 + bx + c - y_true) * 1
    error = (a*x**2 + b*x + c - y_true)**2
    intermed = 2 * (a*x**2 + b*x + c - y_true)
    d_da = intermed * x**2
    d_db = intermed * x
    d_dc = intermed
    return d_da, d_db, d_dc, error


def exp_grad_exp(x, y_true, a, b):
    # (ae^(bx) - y_true)^2
    # d/da = 2(ae^(bx) - y_true) * e^(bx)
    # d/db = 2(ae^(bx) - y_true) * axe^(bx)
    error = (a*np.exp(b*x) - y_true)**2
    intermed = 2 * (a*np.exp(b*x) - y_true)
    d_da = intermed * np.exp(b*x)
    d_db = intermed * a*x*np.exp(b*x)
    return d_da, d_db, error


if __name__ == "__main__":

    # For quadratic
    x, y_true = make_noisy_data(partial(square, a=1, b=-np.pi, c=np.e), 100, 0, 4)
    a, b, c = 0.1, 0.1, 0.1
    grad_func = square_grad_sqerr
    learning_rate = 0.01

    # training loop
    num_steps = 10
    fig, ax = plt.subplots()
    framerate = 60
    delay = 1.0 / framerate

    for step in range(num_steps):
        d_da, d_db, d_dc, err = grad_func(x, y_true, a, b, c)
        avg_d_da = np.mean(d_da)
        avg_d_db = np.mean(d_db)
        avg_d_dc = np.mean(d_dc)
        avg_err = np.mean(err)

        print(f'At step {step}: d_da: {avg_d_da} -- d_db: {avg_d_db} -- d_dc:{avg_d_dc}')
        # update rule
        a = a - learning_rate * avg_d_da
        b = b - learning_rate * avg_d_db
        c = c - learning_rate * avg_d_dc

        print(f'At step {step}: a: {a} -- b: {b} -- c:{c}')
        print(f'At step {step}: error: {np.mean(err)}')
        if step % 10 == 0:
            ax.clear()
            ax.scatter(x, y_true, c='g')
            ax.plot(x, square(x, a, b, c), c='r')
            plt.title(f'Values for: a: {a:.3f} -- b: {b:.3f} -- c: {c:.3f} -- err: {avg_err:.3f}')
            plt.draw()
            plt.pause(delay)

    # plt.ioff()  # Interactive mode off
    plt.show()

    # For exponential
    x, y_true = make_noisy_data(partial(exp, a=np.e, b=np.pi), 100, 0, 1)
    a, b = 0.1, 0.1
    grad_func = exp_grad_exp
    learning_rate = 0.001

    # training loop
    num_steps = 1000

    fig, ax = plt.subplots()
    framerate = 60
    delay = 1.0 / framerate

    for step in range(num_steps):
        d_da, d_db, err = grad_func(x, y_true, a, b)
        avg_d_da = np.mean(d_da)
        avg_d_db = np.mean(d_db)
        avg_err = np.mean(err)

        print(f'At step {step}: d_da: {avg_d_da} -- d_db: {avg_d_db}')
        # update rule
        a = a - learning_rate * avg_d_da
        b = b - learning_rate * avg_d_db

        print(f'At step {step}: a: {a} -- b: {b}')
        print(f'At step {step}: error: {np.mean(err)}')
        if True:
            ax.clear()
            ax.scatter(x, y_true, c='g')
            plt.plot(x, exp(x, a, b,), c='r')
            plt.title(f'Values for: a: {a:.3f} -- b: {b:.3f} -- err: {avg_err:.3f}')
            plt.draw()
            plt.pause(delay)

    plt.ioff()  # Interactive mode off
    plt.show()
