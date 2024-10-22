import numpy as np
import matplotlib.pyplot as plt


def generate_random_throws(board_size, num_throws):
    x = np.random.uniform(-board_size/2., board_size/2., num_throws)
    y = np.random.uniform(-board_size/2., board_size/2., num_throws)

    return x, y


def fraction_in_circle(board_size, x, y):
    inside = np.sqrt(x**2 + y**2) <= board_size/2.
    return np.sum(inside) / inside.shape[0] * 4.0


def draw_circle_and_square(radius, x, y):
    fig, ax = plt.subplots()

    square = plt.Rectangle((-radius, -radius), 2 * radius, 2 * radius, fill=False, edgecolor='black')
    ax.add_patch(square)

    circle = plt.Circle((0, 0), radius, fill=False, edgecolor='blue')
    ax.add_patch(circle)

    inside = np.sqrt(x ** 2 + y ** 2) <= radius
    inds = np.where(inside)
    ax.scatter(x[inds], y[inds], marker='+', color='green')
    inds = np.where(np.bitwise_not(inside))
    ax.scatter(x[inds], y[inds], marker='+', color='red')

    ax.set_aspect('equal')
    ax.axis('off')

    ax.set_xlim(-radius * 1.1, radius * 1.1)
    ax.set_ylim(-radius * 1.1, radius * 1.1)

    plt.show()


x, y = generate_random_throws(1, 10**8)
print(fraction_in_circle(1, x, y))
# draw_circle_and_square(1/2., x, y)