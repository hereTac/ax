def sort_by_sorted(arr1, arr2):
    c = []
    x, y = 0, 0
    # len 6 4
    while x < len(arr1) and y < len(arr2):
        if arr1[x] < arr2[y]:
            c.append(arr1[x])
            x += 1
        else:
            c.append(arr2[y])
            y += 1
    while y < len(arr2):
        c.append(arr2[y])
        y += 1
    while x < len(arr1):
        c.append(arr1[x])
        x += 1
    return c


if __name__ == '__main__':
    array1 = [2, 3, 12, 32, 121, 2323]
    array2 = [23, 46, 856, 5683, 5777, 5887]
    print(sort_by_sorted(array1, array2))
