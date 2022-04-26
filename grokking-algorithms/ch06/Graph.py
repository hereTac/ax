def my_graph():
    graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"],
             "claire": ["thom", "jonny"], "anuj": [], "peggy": [], "thom": [], "jonny": []}
    return graph


if __name__ == '__main__':
    print(my_graph())
