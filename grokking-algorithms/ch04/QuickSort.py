def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for x in arr[1:]:
            if x < pivot:
                less.append(x)
        for y in arr[1:]:
            if y > pivot:
                greater.append(y)
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    array = [6, 3, 1, 9, 10]
    print(quick_sort(array))
