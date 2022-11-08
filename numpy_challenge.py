import numpy as np

if __name__ == "__main__":  # creatint 3 different numpy arrays
    arr_1 = np.eye(3, dtype=int)
    arr_2 = np.arange(9).reshape((3, 3))
    arr_3 = np.fromstring('7 3', dtype=int, sep=' ')  # fav number of Sheldon Cooper


def matrix_multiplication(a, b):  # a and b are matrices
    return np.matmul(a, b)


def multiplication_check(a):  # a is an array of matrices
    for i in range(1, len(a)):
        if np.shape(a[i])[0] != np.shape(a[i - 1])[1] or np.shape(a[i])[1] != np.shape(a[i - 1])[0]:
            return False
    return True


def multiply_matrices(a):  # a is an array of matrices
    matt = a[0]
    for i in range(1, len(a)):
        if np.shape(a[i])[0] != np.shape(a[i - 1])[1] or np.shape(a[i])[1] != np.shape(a[i - 1])[0]:
            return None
        matt = np.matmul(a[i], matt)
    return matt


def compute_2d_distance(a, b):  # two arrays and two 'points'
    return np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def compute_multidimensional_distance(a, b):  # two 1d arrays
    return np.array(a) - np.array(b)


def compute_pair_distances(a):  # 2d array
    return np.sqrt(np.sum(np.square(a[:, np.newaxis, :] - a[np.newaxis, :, :]), axis=-1))
