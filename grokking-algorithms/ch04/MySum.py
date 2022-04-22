def my_sum(arr):
    total = 0
    for v in arr:
        total = total + v
    return total


if __name__ == '__main__':
    print(my_sum([2, 4, 6]))
