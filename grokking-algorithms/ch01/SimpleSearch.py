def simple_search(my_list, target):
    for guess_index in range(len(my_list)):
        if target == my_list[guess_index]:
            return guess_index
    return None


if __name__ == '__main__':
    my_list = (2, 4, 6, 7, 8, 9, 22, 134, 545)
    print(simple_search(my_list, 134))
