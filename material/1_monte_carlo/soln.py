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
    framerate = 60
    delay = 1.0 / framerate

    square = plt.Rectangle((-radius, -radius), 2 * radius, 2 * radius, fill=False, edgecolor='black')
    ax.add_patch(square)

    circle = plt.Circle((0, 0), radius, fill=False, edgecolor='blue')
    ax.add_patch(circle)

    pts_pos_x, pts_pos_y = [], []
    pts_neg_x, pts_neg_y = [], []
    pos_cnt = 0.0
    total = 0.0

    ax.set_aspect('equal')
    ax.axis('off')

    ax.set_xlim(-radius * 1.1, radius * 1.1)
    ax.set_ylim(-radius * 1.1, radius * 1.1)

    for xx, yy in zip(x, y):
        inside = np.sqrt(xx ** 2 + yy ** 2) <= radius
        total += 1.0
        if inside:
            ax.scatter(xx, yy, marker='+', color='green')
            pos_cnt += 1.0
        else:
            ax.scatter(xx, yy, marker='+', color='red')

        plt.title(f'Current estimate of pi: {pos_cnt/total*4.0}')
        plt.draw()
        plt.pause(delay)


    plt.ioff()  # Interactive mode off
    plt.show()


x, y = generate_random_throws(1, 10**4)
print(fraction_in_circle(1, x, y))
draw_circle_and_square(1/2., x, y)
