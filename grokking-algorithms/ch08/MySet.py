def set_t():
    fruits = set(["avocado", "tomato", "banana"])
    vegetables = set(["beets", "carrots", "tomato"])
    print(fruits | vegetables)
    print(fruits & vegetables)
    print(fruits-vegetables)
    print(vegetables-fruits)


if __name__ == '__main__':
    set_t()
