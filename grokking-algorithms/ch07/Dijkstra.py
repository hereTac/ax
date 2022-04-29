def dijkstra(graph_list, cost_list, parents_list):
    processed = []
    node = find_lowest_cost_node(cost_list, processed)
    while node is not None:
        cost = cost_list[node]
        neighbors = graph_list[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if cost_list[n] > new_cost:
                cost_list[n] = new_cost
                parents_list[n] = node
        processed.append(node)
        node = find_lowest_cost_node(cost_list, processed)
    return cost_list, parents_list


def find_lowest_cost_node(cost_list, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in cost_list:
        cost = cost_list[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == '__main__':
    graph = {"s": {}, "a": {}, "b": {}, "e": {}}
    graph["s"]["a"] = 6
    graph["s"]["b"] = 2
    graph["a"]["e"] = 1
    graph["b"]["a"] = 3
    graph["b"]["e"] = 5
    costs = {"a": 6, "b": 2, "e": float("inf")}
    parents = {"a": "s", "b": "s", "e": None}
    print(dijkstra(graph, costs, parents))
