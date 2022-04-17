def count_down(num):
    print(num)
    if num <= 0:  # base case
        return
    else:  # recursion case
        count_down(num - 1)


if __name__ == '__main__':
    count_down(3)
