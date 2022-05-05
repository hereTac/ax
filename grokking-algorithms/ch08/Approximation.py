def approximation():
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
    stations = {"one": {"id", "nv", "ut"}, "two": {"wa", "id", "mt"}, "three": {"or", "nv", "ca"}, "four": {"nv", "ut"},
                "five": {"ca", "az"}}
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
            states_needed -= states_covered
            final_stations.add(best_station)
    print(final_stations)


if __name__ == '__main__':
    approximation()
