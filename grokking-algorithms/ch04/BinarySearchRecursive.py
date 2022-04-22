def binary_search_recursive(arr, item, low, high):
    # mid = (low + high) // 2
    mid = int((low + high) / 2)
    guess = arr[mid]
    if item == guess:
        return mid
    if item > guess:
        return binary_search_recursive(arr, item, mid + 1, high)
    if item < guess:
        return binary_search_recursive(arr, item, low, mid - 1)


if __name__ == '__main__':
    array = [2, 3, 4, 5, 6, 7, 9, 10, 23, 43, 54]
    print(binary_search_recursive(array, 3, 0, len(array)-1))
