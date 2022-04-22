def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# gcd(a, b) = gcd(b, a mod b)
if __name__ == '__main__':
    print(gcd(1680, 640))
