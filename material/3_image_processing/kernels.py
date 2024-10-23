import cv2
import numpy as np
import matplotlib.pyplot as plt


def create_checkerboard(size=24, num_tiles=2):
    checkerboard = np.zeros((num_tiles, num_tiles))
    checkerboard[1::2, ::2] = 1
    checkerboard[::2, 1::2] = 1

    checkerboard = np.kron(checkerboard, np.ones((size, size))) * 255.0

    return checkerboard.astype(np.float32)


def apply_kernel_and_show(kernel, image, name):
    filtered_img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
    fig, axs = plt.subplots(1, 2)
    cmap = None
    if image.ndim == 2:
        cmap = 'gray'
    axs[0].imshow(image, cmap=cmap)
    axs[1].imshow(filtered_img, cmap=cmap)
    axs[0].set_title('original')
    axs[1].set_title('kernel_applied')
    axs[0].axis('off')
    axs[1].axis('off')
    fig.suptitle(name)
    plt.show()


if __name__ == "__main__":

    box_kernel = np.ones((3, 3)) / 9.0
    edge_kernel = np.array([
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ])

    grad_x_kernel = np.array([
        [0, 0, 0],
        [-1, 2, -1],
        [0, 0, 0]
    ])

    sobel_x_kernel = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])

    grad_y_kernel = np.array([
        [1, -1]
    ])

    # What should these look like?
    black_image = np.zeros((24, 24), dtype=np.uint8)
    apply_kernel_and_show(edge_kernel, black_image, 'edge on black image')

    # What should these look like?
    checker_board = create_checkerboard()

    apply_kernel_and_show(grad_x_kernel, checker_board, 'edge x on checkerboard')
    apply_kernel_and_show(sobel_x_kernel, checker_board, 'sobel x on checkerboard')
    apply_kernel_and_show(edge_kernel, checker_board, 'edge on checkerboard')
    apply_kernel_and_show(box_kernel, checker_board, 'blur on checkerboard')
