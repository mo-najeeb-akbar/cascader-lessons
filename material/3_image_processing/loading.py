import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from kernels import apply_kernel_and_show

if __name__ == "__main__":
    pth = 'images/halloween_sausage.webp'

    if os.path.exists(pth):
        my_img = cv2.imread(pth)[..., ::-1]
        plt.imshow(my_img)
        plt.show()

        # Add code here to apply gradients and visualize
        sobel_x_kernel = np.array([
            [1, 0, -1],
            [2, 0, -2],
            [1, 0, -1]
        ])
        apply_kernel_and_show(sobel_x_kernel, my_img, 'Smooth Gradient in X')
    else:
        print(f"The path '{pth}' does not exist.")
