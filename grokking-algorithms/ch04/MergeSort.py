def merge_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge_sorted_sub(left, right)


def merge_sorted_sub(arr1, arr2):
    c = []
    x, y = 0, 0
    while x < len(arr1) and y < len(arr2):
        if arr1[x] < arr2[y]:
            c.append(arr1[x])
            x += 1
        else:
            c.append(arr2[y])
            y += 1
    while x < len(arr1):
        c.append(arr1[x])
        x += 1
    while y < len(arr2):
        c.append(arr2[y])
        y += 1
    return c


if __name__ == '__main__':
    array = [221, 23, 3, 2, 121, 1, 21, 32]
    print(merge_sort(array))
