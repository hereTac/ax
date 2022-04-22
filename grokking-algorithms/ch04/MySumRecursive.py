def my_sum_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + my_sum_recursive(arr[1:len(arr)])


if __name__ == '__main__':
    print(my_sum_recursive([2, 4, 6]))
