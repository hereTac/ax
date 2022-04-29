def dijkstra(graph_list, costs_list, parents_list):
    processed = []
    node = find_lowest_cost(costs_list, processed)
    while node is not None:
        neighbor = graph_list[node]
        for nodes in neighbor:
            cost = costs_list[node] + graph_list[node][nodes]
            if cost < costs_list[nodes]:
                costs_list[nodes] = cost
                parents_list[nodes] = node
        processed.append(node)
        node = find_lowest_cost(costs_list, processed)
    return costs_list, parents_list


def find_lowest_cost(cost_list, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in cost_list:
        if cost_list[node] < lowest_cost and node not in processed:
            lowest_cost = cost_list[node]
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == '__main__':
    graph = {"s": {}, "a": {}, "b": {}, "c": {}, "d": {}, "e": {}}
    graph["s"]["a"] = 5
    graph["s"]["b"] = 2
    graph["b"]["a"] = 8
    graph["b"]["c"] = 7
    graph["a"]["c"] = 2
    graph["a"]["d"] = 4
    graph["d"]["c"] = 6
    graph["d"]["e"] = 3
    graph["c"]["e"] = 1
    costs = {"a": 5, "b": 2, "c": float("inf"), "d": float("inf"), "e": float("inf")}
    parents = {"a": "s", "b": "s", "c": None, "d": None, "e": None}
    print(dijkstra(graph, costs, parents))
    import Dijkstra

    print(Dijkstra.dijkstra(graph, costs, parents))
