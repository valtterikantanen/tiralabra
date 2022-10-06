from random import choice

import unittest

from dijkstra import dijkstra
from graph import make_adjacency_lists


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.adjacency_lists = make_adjacency_lists("src/maps/Berlin_0_256.map")[0]
        self.known_distances = collect_known_distances("src/maps/Berlin_0_256.map.scen")

    def test_dijkstra_finds_the_shortest_path(self):
        # Valitaan 930:stä testitapauksesta mielivaltaiset 15 tapausta
        for _ in range(15):
            start_and_end, test_distance = choice(list(self.known_distances.items()))
            start = start_and_end[0]
            end = start_and_end[1]
            distance = dijkstra(self.adjacency_lists, start, end)[2]
            # Tarkistetaan, että arvot vastaavat toisiaan kuuden desimaalin tarkkuudella
            self.assertAlmostEqual(distance, test_distance, 6)


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
