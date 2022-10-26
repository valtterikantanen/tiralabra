from random import randint
from tkinter import Tk, Event

import unittest

from services.ui_logic import UILogic


class TestUILogic(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.ui_logic = UILogic()
        self.map_rows = self.ui_logic.create_map("Map_20.map")[0]

    def test_finds_all_available_maps(self):
        maps = self.ui_logic._get_available_maps()
        self.assertEqual(len(maps), 3)

    def test_reset_map_resets_variables(self):
        self.ui_logic.start_node_input.set("0, 0")
        self.ui_logic.end_node_input.set("9, 9")
        self.ui_logic._route = [0, 1, 12, 15, 19]
        self.ui_logic.reset_map()
        self.assertEqual(self.ui_logic.start_node_input.get(), "")
        self.assertEqual(self.ui_logic.end_node_input.get(), "")
        self.assertEqual(self.ui_logic._route, None)

    def test_create_map_creates_correct_map_with_parameter(self):
        map_row = self.map_rows[2]
        correct_row = [".", "@", "@", "@", ".", ".", ".", ".", ".", ".", ".", "@", "@", ".", ".", ".", ".", ".", ".", "."]
        self.assertEqual(map_row, correct_row)

    def test_create_map_creates_correct_map_without_parameter(self):
        map_rows = self.ui_logic.create_map()[0]
        self.assertEqual(map_rows, self.map_rows)

    def test_handle_click_when_selected_square_is_not_empty(self):
        event = Event()
        event.x = 50
        event.y = 81
        self.assertEqual(self.ui_logic.handle_click(event), False)

    def test_select_start_node_when_selected_square_is_empty(self):
        event = Event()
        event.x = 378
        event.y = 250
        event.num = 1
        self.ui_logic.handle_click(event)
        self.assertEqual(self.ui_logic.start_node_input.get(), "12, 8")
        self.assertEqual(self.ui_logic._start_node, 172)

    def test_select_end_node_when_selected_square_is_empty(self):
        event = Event()
        event.x = 163
        event.y = 531
        event.num = 3
        self.ui_logic.handle_click(event)
        self.assertEqual(self.ui_logic.end_node_input.get(), "5, 17")
        self.assertEqual(self.ui_logic._end_node, 345)

    def test_handle_click_resets_possible_route(self):
        self.ui_logic._route = [74, 93, 112, 132, 152, 171, 191, 211, 231, 251, 271, 270]
        event = Event()
        event.x = 163
        event.y = 531
        event.num = 1
        self.ui_logic.handle_click(event)
        self.assertEqual(self.ui_logic._route, None)

    def test_find_route_sets_distance_and_used_time(self):
        self.find_route()
        self.assertEqual(self.ui_logic.shortest_path_length.get(), "13,07107")
        self.assertNotEqual(self.ui_logic.used_time.get(), None)

    def test_find_route_sets_same_distance_on_both_algorithms(self):
        self.find_route()
        self.assertEqual(self.ui_logic.shortest_path_length.get(), "13,07107")
        self.ui_logic.chosen_algorithm.set("IDA*")
        self.ui_logic.find_route()
        self.assertEqual(self.ui_logic.shortest_path_length.get(), "13,07107")

    def test_find_route_returns_when_no_algorithm_is_chosen(self):
        self.ui_logic._start_node = 172
        self.ui_logic._end_node = 345
        self.assertEqual(self.ui_logic.find_route(), None)

    def test_validate_input_when_no_algorithm_is_chosen(self):
        self.assertEqual(self.ui_logic.validate_input(), "Valitse algoritmi!")

    def test_validate_input_when_no_start_node_is_chosen(self):
        self.ui_logic.end_node_input.set("6, 2")
        self.ui_logic.chosen_algorithm.set("Dijkstra")
        self.assertEqual(self.ui_logic.validate_input(), "Syötä koordinaatit muodossa 0, 0!")

    def test_validate_input_when_end_node_is_out_of_bounds(self):
        self.ui_logic.start_node_input.set("2, 19")
        self.ui_logic.end_node_input.set("21, 21")
        self.ui_logic.chosen_algorithm.set("Dijkstra")
        self.assertEqual(self.ui_logic.validate_input(), "Koordinaattien on oltava välillä 0–19, 0–19")

    def test_validate_input_when_start_node_is_not_empty(self):
        self.ui_logic.start_node_input.set("1, 2")
        self.ui_logic.end_node_input.set("2, 19")
        self.ui_logic.chosen_algorithm.set("IDA*")
        self.assertEqual(self.ui_logic.validate_input(), "Valitsit alku- tai loppupisteeksi ruudun, jossa on este!")

    def test_get_node_number_returns_false_with_unvalid_coordinates(self):
        self.assertEqual(self.ui_logic.get_node_number("a, 0"), False)

    def test_get_node_color_returns_green_if_there_is_no_route(self):
        node = 172
        self.ui_logic._start_node = node
        self.assertEqual(self.ui_logic.get_node_color(node), "green")

    def test_get_node_color_returns_green_on_start_node_and_end_node(self):
        self.find_route()
        self.assertEqual(self.ui_logic.get_node_color(172), "green")
        self.assertEqual(self.ui_logic.get_node_color(345), "green")

    def test_get_node_color_returns_red_on_other_nodes_on_the_route(self):
        self.find_route()
        self.assertEqual(self.ui_logic.get_node_color(192), "red")

    def test_get_node_color_returns_yellow_on_visited_nodes(self):
        self.find_route()
        visited_nodes = self.ui_logic._visited_nodes
        node = visited_nodes.index(True)
        self.assertEqual(self.ui_logic.get_node_color(node), "yellow")

    def find_route(self):
        self.ui_logic._start_node = 172
        self.ui_logic._end_node = 345
        self.ui_logic.chosen_algorithm.set("Dijkstra")
        self.ui_logic.find_route()
