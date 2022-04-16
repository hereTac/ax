def binary_search(my_list, item):
    low = 0
    high = len(my_list) - 1

    while low < high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    my_list = (2, 4, 6, 7, 8, 9, 22, 134, 545)
    print(binary_search(my_list, 8))
