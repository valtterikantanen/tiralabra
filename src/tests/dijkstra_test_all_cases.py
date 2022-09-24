from dijkstra import dijkstra
from graph import make_adjacency_lists

def collect_known_distances(filename):
    with open(filename) as file:
        distances = {}

        for row, line in enumerate(file):
            if row == 0:
                continue
            line = line.split()
            start = int(line[5]) * int(line[2]) + int(line[4])
            end = int(line[7]) * int(line[2]) + int(line[6])
            distances[(start, end)] = float(line[8])
    return distances

def write_test_results(graph, correct_distances, filename):
    with open(filename, "w") as file:
        file.write("start_node;end_node;calculated_distance;known_distance;difference\n")
        for key, value in correct_distances.items():
            start = key[0]
            end = key[1]
            distance = dijkstra(graph, start, end)[1]
            difference = abs(distance - value)
            file.write(f"{start};{end};{distance};{value};{difference}\n")

if __name__ == "__main__":
    adjacency_lists = make_adjacency_lists("src/maps/Berlin_0_256.map")[0]
    known_distances = collect_known_distances("src/maps/Berlin_0_256.map.scen")
    write_test_results(adjacency_lists, known_distances, "result.csv")
