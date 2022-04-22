def count_list_elements(arr):
    # if arr == []:
    if not arr:
        return 0
    return 1+count_list_elements(arr[1:])


if __name__ == '__main__':
    print(count_list_elements([1, 2, 3, 4, 5]))
