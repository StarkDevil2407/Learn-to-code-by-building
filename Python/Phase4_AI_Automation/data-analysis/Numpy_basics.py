import numpy as np

def numpy_demo():
    # Creating arrays
    arr = np.array([1, 2, 3, 4, 5])
    print("Original Array:", arr)

    # Array operations
    print("Array + 2:", arr + 2)
    print("Array squared:", arr ** 2)

    # 2D array and sum
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print("\n2D Array:\n", matrix)
    print("Sum of all elements:", np.sum(matrix))
    print("Column-wise sum:", np.sum(matrix, axis=0))

if __name__ == "__main__":
    numpy_demo()
