import unittest

from algorithms.dijkstra import dijkstra
from tests.dijkstra_test import collect_known_distances
from util.graph import make_adjacency_lists


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.adjacency_lists = make_adjacency_lists("src/maps/Berlin_0_256.map")[0]
        self.known_distances = collect_known_distances("src/maps/Berlin_0_256.map.scen")

    def test_dijkstra_finds_the_shortest_path(self):
        for test_case in self.known_distances.items():
            start_and_end, test_distance = test_case
            start, end = start_and_end
            distance = dijkstra(self.adjacency_lists, start, end)[2]
            # Tarkistetaan, että arvot vastaavat toisiaan kuuden desimaalin tarkkuudella
            self.assertAlmostEqual(distance, test_distance, 6)
