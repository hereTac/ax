from collections import deque
import Graph


def bfs():
    search_queue = deque()
    searched = []
    listed = Graph.my_graph()
    for x in listed.get("you"):
        search_queue.append(x)
    while search_queue:
        name = search_queue.popleft()
        if name not in searched:
            searched.append(name)
            if is_seller(name):
                return name
            for x in listed.get(name):
                search_queue.append(x)
        else:
            print(name + " was Searched.")
    return "No Seller"


def is_seller(name):
    if name.endswith("m"):
        return True
    return False


if __name__ == '__main__':
    print("the seller is " + bfs() + ".")
