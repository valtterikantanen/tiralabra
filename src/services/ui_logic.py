import os
import time

from tkinter import StringVar

from algorithms.dijkstra import dijkstra
from algorithms.ida_star import ida_star
from util.graph import make_adjacency_lists


class UILogic:
    def __init__(self, grid_width=600):
        self.grid_width = grid_width

        self.start_node_input = StringVar()
        self.end_node_input = StringVar()
        self.used_time = StringVar()
        self.shortest_path_length = StringVar()
        self.chosen_algorithm = StringVar()
        self.available_maps = self._get_available_maps()
        self.selected_map = StringVar(value=self.available_maps[0])

        self._graph = None
        self._map_rows = None
        self._map_height = None
        self.map_width = None
        self._start_node = None
        self._end_node = None

        self._route = None
        self._visited_nodes = None

    def _get_available_maps(self):
        available_maps = []
        for file in os.listdir("src/maps"):
            if file.endswith(".map"):
                available_maps.append(file)
        return available_maps

    def create_map(self, map_file=None):
        map_file = self.selected_map.get() if map_file is None else map_file
        self._graph, self._map_rows = make_adjacency_lists(f"src/maps/{map_file}")
        self._map_height = len(self._map_rows)
        self.map_width = len(self._map_rows[0])
        square_size = self.grid_width / self.map_width

        return self._map_rows, square_size

    def reset_map(self):
        self.create_map()

        self.start_node_input.set("")
        self.end_node_input.set("")
        self.used_time.set("")
        self.shortest_path_length.set("")
        self._route = None
        self._visited_nodes = None

    def handle_click(self, event):
        width = self.grid_width / self.map_width
        height = self.grid_width / self._map_height

        x_coord = int(event.x // width)
        y_coord = int(event.y // height)

        coord_as_str = f"{x_coord}, {y_coord}"

        # Aloitusruutu asetetaan hiiren vasemmalla näppäimellä, jolloin numero on 1, oikealla 3
        if event.num == 1:
            self.start_node_input.set(coord_as_str)
            self._start_node = self.get_node_number(coord_as_str)
        elif event.num == 3:
            self.end_node_input.set(coord_as_str)
            self._end_node = self.get_node_number(coord_as_str)

    def find_route(self):
        if self.chosen_algorithm.get() == "IDA*":
            start_time = time.time()
            self._route, distance = ida_star(self._graph, self._start_node, self._end_node)
            self._visited_nodes = [False for _ in range(len(self._graph))]
            elapsed_time = f"{round(time.time() - start_time, 5)}"
        elif self.chosen_algorithm.get() == "Dijkstra":
            start_time = time.time()
            self._route, self._visited_nodes, distance = dijkstra(
                self._graph, self._start_node, self._end_node)
            elapsed_time = f"{round(time.time() - start_time, 5)}"
        distance = f"{round(distance, 5)}"
        distance = "∞" if distance == "inf" else distance
        self.shortest_path_length.set(f"{distance.replace('.', ',')}")
        self.used_time.set(f"{elapsed_time.replace('.', ',')} s")

    def validate_input(self):
        error_msg = ""
        algorithm = self.chosen_algorithm.get()
        self._start_node = self.get_node_number(self.start_node_input.get())
        self._end_node = self.get_node_number(self.end_node_input.get())

        if not algorithm:
            error_msg = "Valitse algoritmi!"

        elif self._start_node is False or self._end_node is False:
            error_msg = "Syötä koordinaatit muodossa 0, 0!"

        elif (not self._validate_node_number(self._start_node) or
              not self._validate_node_number(self._end_node)):
            max_x = self.map_width - 1
            max_y = self._map_height - 1
            error_msg = f"Koordinaattien on oltava välillä 0–{max_x}, 0–{max_y}"

        elif self._is_obstacle(self._start_node) or self._is_obstacle(self._end_node):
            error_msg = "Valitsit alku- tai loppupisteeksi ruudun, jossa on este!"

        return error_msg

    def _validate_node_number(self, node):
        return 0 <= node < len(self._graph)

    def _is_obstacle(self, node):
        x_coord, y_coord = self._get_coordinates(node)
        return self._map_rows[y_coord][x_coord] == "@"

    def _get_coordinates(self, node):
        x_coord = node % self.map_width
        y_coord = node // self.map_width
        return x_coord, y_coord

    def get_node_number(self, node):
        try:
            node = node.split(",")
            if len(node) != 2:
                return False
            # Ruudun tunnus saadaan kertomalla sen y-koordinaatti rivin
            # pituudella ja lisäämällä siihen x-koordinaatti
            node = int(node[1]) * self.map_width + int(node[0])
            return node
        except ValueError:
            return False

    def get_node_color(self, node):
        color = ""
        if self._route is None:
            if node in (self._start_node, self._end_node):
                color = "green"
        else:
            if node in (self._route[0], self._route[len(self._route) - 1]):
                color = "green"
            elif node in self._route:
                color = "red"
            elif self._visited_nodes[node]:
                color = "yellow"
        return color
