def check_voter(name):
    if voted.get(name):
        print("kick him out!")
    else:
        voted[name] = True
        print("let them vote!")


if __name__ == '__main__':
    voted = {}
    check_voter("tom")
    check_voter("mike")
    check_voter("mike")
