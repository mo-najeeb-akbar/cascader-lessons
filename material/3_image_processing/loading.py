import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from kernels import apply_kernel_and_show

if __name__ == "__main__":
    pth = 'images/halloween_sausage.webp'

    if os.path.exists(pth):
        my_img = cv2.imread(sys.argv[1])[..., ::-1]
        plt.imshow(my_img)
        plt.show()

        # Add code here to apply gradients and visualize
    else:
        print(f"The path '{pth}' does not exist.")
