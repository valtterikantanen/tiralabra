from math import inf
from random import choice

import unittest

from algorithms.ida_star import ida_star
from algorithms.dijkstra import dijkstra
from util.graph import make_adjacency_lists


class TestIdaStar(unittest.TestCase):
    def setUp(self):
        self.adjacency_lists, self.graph = make_adjacency_lists("src/maps/Map_20.map")
        self.empty_squares = []
        self.occupied_squares = []
        # Kartan tyhjät ruudut, joihin ei ole kaikista muista tyhjistä ruuduista reittiä
        self.unreachable_squares = [263, 283, 303]
        for y in range(len(self.graph)):
            for x in range(len(self.graph[0])):
                node = y * len(self.graph) + x
                if self.graph[y][x] == ".":
                    if node in self.unreachable_squares:
                        continue
                    self.empty_squares.append(node)
                else:
                    self.occupied_squares.append(node)

    def test_ida_star_finds_the_shortest_path_when_path_exists(self):
        # Luodaan noin 25 satunnaista testitapausta 20×20-kokoiseen ruudukkoon
        for _ in range(25):
            start = choice(self.empty_squares)
            end = choice(self.empty_squares)
            ida_star_distance = ida_star(self.adjacency_lists, start, end)[1]
            # Verrataan saatua tulosta Dijkstran algoritmin antamaan tulokseen
            dijkstra_distance = dijkstra(self.adjacency_lists, start, end)[2]
            # Tarkistetaan, että saadut tulokset vastaavat toisiaan kymmenen desimaalin tarkkuudella
            self.assertAlmostEqual(ida_star_distance, dijkstra_distance, 10)

    def test_ida_star_returns_inf_when_start_node_is_occupied(self):
        for _ in range(5):
            start = choice(self.occupied_squares)
            end = choice(self.empty_squares)
            distance = ida_star(self.adjacency_lists, start, end)[1]
            self.assertEqual(distance, inf)

    def test_ida_star_returns_inf_when_end_node_is_occupied(self):
        for _ in range(5):
            start = choice(self.empty_squares)
            end = choice(self.occupied_squares)
            distance = ida_star(self.adjacency_lists, start, end)[1]
            self.assertEqual(distance, inf)

    def test_ida_star_returns_inf_when_start_node_is_unreachable(self):
        end_nodes = [221, 223, 225, 245, 265]
        for end_node in end_nodes:
            distance = ida_star(self.adjacency_lists, 263, end_node)[1]
        self.assertEqual(distance, inf)

    def test_ida_star_returns_inf_when_end_node_is_unreachable(self):
        self.adjacency_lists, self.graph = make_adjacency_lists("src/maps/Map_5.map")
        distance = ida_star(self.adjacency_lists, 10, 12)[1]
        self.assertEqual(distance, inf)