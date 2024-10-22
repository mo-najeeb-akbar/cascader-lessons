import numpy as np

if __name__ == "__main__":
    a = np.array([1, 2, 3, 4])
    a = a + 1
    print(f'Result of adding to a: {a}')
    print(f'Shape of a: {a.shape}')
    # compare this with -- not possible using the simple syntax
    # b = [1, 2, 3, 4]
    # b = b + 1

    mat_0 = np.eye(3)
    print(f'Result of np.eye:\n {mat_0}')
    print(f'Shape of mat_0: {a.shape}')
