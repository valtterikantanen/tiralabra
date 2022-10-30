import os
import sys
import time

from random import randint
from statistics import mean, median

def test_map_with_10000_routes(num_of_rounds, filename):
    dijkstra_times = []
    ida_star_times = []
    adjacency_lists, map_rows = make_adjacency_lists(f"src/maps/perf_test_maps/{filename}")

    for _ in range(num_of_rounds):
        test_cases = {}
        map_width = 10
        i = 0
        while i < 10_000:
            start_x, start_y = randint(0, map_width-1), randint(0, map_width-1)
            goal_x, goal_y = randint(0, map_width-1), randint(0, map_width-1)
            if map_rows[start_y][start_x] == "@" or map_rows[goal_y][goal_x] == "@":
                continue
            start_node = start_y * map_width + start_x
            goal_node = goal_y * map_width + goal_x
            test_cases[start_node] = goal_node
            i += 1

        ida_star_times.append(find_route(test_cases, adjacency_lists, ida_star))
        dijkstra_times.append(find_route(test_cases, adjacency_lists, dijkstra))
    
    return dijkstra_times, ida_star_times

def test_map_with_1_route(num_of_rounds, filename):
    dijkstra_times = []
    ida_star_times = []
    hardest_route_for_ida_star = ""
    adjacency_lists, map_rows = make_adjacency_lists(f"src/maps/perf_test_maps/{filename}")

    i = 0
    while i < num_of_rounds:
        map_width = 20
        start_x, start_y = randint(0, map_width-1), randint(0, map_width-1)
        goal_x, goal_y = randint(0, map_width-1), randint(0, map_width-1)
        if map_rows[start_y][start_x] == "@" or map_rows[goal_y][goal_x] == "@":
            continue
        start_node = start_y * map_width + start_x
        goal_node = goal_y * map_width + goal_x

        ida_star_used_time = find_route({start_node: goal_node}, adjacency_lists, ida_star)
        if len(ida_star_times) == 0 or ida_star_used_time > max(ida_star_times):
            hardest_route_for_ida_star = f"({start_x}, {start_y}) -> ({goal_x}, {goal_y})"
        ida_star_times.append(ida_star_used_time)
        dijkstra_times.append(find_route({start_node: goal_node}, adjacency_lists, dijkstra))
        i += 1
    
    return dijkstra_times, ida_star_times, hardest_route_for_ida_star

def find_route(test_cases, graph, algorithm):
    start_time = time.time()
    for test_case in test_cases.items():
        start, goal = test_case
        algorithm(graph, start, goal)
    used_time = time.time() - start_time
    return used_time

if __name__ == "__main__":
    # Tämä rivi vaaditaan, jotta allaolevat importit toimivat
    sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

    from algorithms.dijkstra import dijkstra
    from algorithms.ida_star import ida_star
    from util.graph import make_adjacency_lists

    dijkstra_times, ida_star_times = test_map_with_10000_routes(50, "map1.map")
    print("Ensimmäinen testi\nKartta: map1.map (koko 10×10)")
    print("Tutkittiin 50 kpl 10 000 reitin sarjoja")
    print("Algoritmi         Nopein         Hitain      Keskiarvo       Mediaani")
    print(f"Dijkstra  {min(dijkstra_times):12.7f} s {max(dijkstra_times):12.7f} s {mean(dijkstra_times):12.7f} s {median(dijkstra_times):12.7f} s")
    print(f"IDA*      {min(ida_star_times):12.7f} s {max(ida_star_times):12.7f} s {mean(ida_star_times):12.7f} s {median(ida_star_times):12.7f} s")
    print()

    dijkstra_times, ida_star_times = test_map_with_10000_routes(50, "map2.map")
    print("Toinen testi\nKartta: map2.map (koko 10×10)")
    print("Tutkittiin 50 kpl 10 000 reitin sarjoja")
    print("Algoritmi         Nopein         Hitain      Keskiarvo       Mediaani")
    print(f"Dijkstra  {min(dijkstra_times):12.7f} s {max(dijkstra_times):12.7f} s {mean(dijkstra_times):12.7f} s {median(dijkstra_times):12.7f} s")
    print(f"IDA*      {min(ida_star_times):12.7f} s {max(ida_star_times):12.7f} s {mean(ida_star_times):12.7f} s {median(ida_star_times):12.7f} s")
    print()

    dijkstra_times, ida_star_times, hardest_route = test_map_with_1_route(20000, "map3.map")
    print("Kolmas testi\nKartta: map3.map (koko 20×20)")
    print("Tutkittiin 20 000 kpl reittejä")
    print("Algoritmi         Nopein         Hitain      Keskiarvo       Mediaani")
    print(f"Dijkstra  {min(dijkstra_times):12.7f} s {max(dijkstra_times):12.7f} s {mean(dijkstra_times):12.7f} s {median(dijkstra_times):12.7f} s")
    print(f"IDA*      {min(ida_star_times):12.7f} s {max(ida_star_times):12.7f} s {mean(ida_star_times):12.7f} s {median(ida_star_times):12.7f} s")
    print(f"IDA* käytti eniten aikaa reittiin {hardest_route}")
    print()

    dijkstra_times, ida_star_times, hardest_route = test_map_with_1_route(20000, "map4.map")
    print("Neljäs testi\nKartta: map4.map (koko 20×20)")
    print("Tutkittiin 20 000 kpl reittejä")
    print("Algoritmi         Nopein         Hitain      Keskiarvo       Mediaani")
    print(f"Dijkstra  {min(dijkstra_times):12.7f} s {max(dijkstra_times):12.7f} s {mean(dijkstra_times):12.7f} s {median(dijkstra_times):12.7f} s")
    print(f"IDA*      {min(ida_star_times):12.7f} s {max(ida_star_times):12.7f} s {mean(ida_star_times):12.7f} s {median(ida_star_times):12.7f} s")
    print(f"IDA* käytti eniten aikaa reittiin {hardest_route}")
