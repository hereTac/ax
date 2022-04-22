def find_max_element_in_list(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    else:
        if len(arr) == 2:
            return arr[0] if arr[0] > arr[1] else arr[1]
        return arr[0] if arr[0] > find_max_element_in_list(arr[1:]) else find_max_element_in_list(arr[1:])


if __name__ == '__main__':
    print(find_max_element_in_list([2, 4, 6, 8]))
