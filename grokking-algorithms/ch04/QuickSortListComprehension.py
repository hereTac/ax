def quick_sort_list_comprehension(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        greater = [y for y in arr[1:] if y > pivot]
        return quick_sort_list_comprehension(less) + [pivot] + quick_sort_list_comprehension(greater)


if __name__ == '__main__':
    array = [12, 23, 234, 32, 54, 563, 43163, 3451, 343]
    print(quick_sort_list_comprehension(array))
