    def left_rotate(arr, k):
        n = len(arr)
        k = k % n  # Handle cases where k is greater than n
        return arr[k:] + arr[:k]

    my_list = [1, 2, 3, 4, 5]
    rotated_list = left_rotate(my_list, 2)
    print(f"Left rotated list: {rotated_list}") # Output: [3, 4, 5, 1, 2]

    my_string = "Python"
    rotated_string = left_rotate(my_string, 2)
    print(f"Left rotated string: {rotated_string}") # Output: thonPy
