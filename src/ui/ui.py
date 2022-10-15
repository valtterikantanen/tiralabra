import os
import time

from tkinter import ttk, constants, StringVar, Canvas, messagebox
from dijkstra import dijkstra
from graph import make_adjacency_lists
from ida_star import ida_star


class UI:

    def __init__(self, root):
        self._root = root
        self._root.configure(bg="#F0F0F0")
        self._GRID_WIDTH = 400
        self._grid = Canvas(master=self._root, height=self._GRID_WIDTH, width=self._GRID_WIDTH)

        self._chosen_algorithm = StringVar()
        self._start_node = StringVar()
        self._end_node = StringVar()
        self._used_time = StringVar()
        self._shortest_path_length = StringVar()

        self._graph = None
        self._map_rows = None
        self._map_width = None
        self._map_height = None
        self._available_maps = []

        self._get_available_maps()
        self._selected_map = StringVar(value=self._available_maps[0])
        self._create_map()

    def start(self):
        time_label = ttk.Label(master=self._root, background="#F0F0F0", text="Aikaa kului")
        time_elapsed = ttk.Label(master=self._root, background="#F0F0F0",
                                 textvariable=self._used_time)

        distance_label = ttk.Label(master=self._root, background="#F0F0F0", text="Reitin pituus")
        distance = ttk.Label(master=self._root, background="#F0F0F0",
                             textvariable=self._shortest_path_length)

        start_node_label = ttk.Label(master=self._root, background="#F0F0F0", text="Lähtöruutu")
        start_node_entry = ttk.Entry(master=self._root, textvariable=self._start_node)

        goal_node_label = ttk.Label(master=self._root, background="#F0F0F0", text="Maaliruutu")
        goal_node_entry = ttk.Entry(master=self._root, textvariable=self._end_node)

        selected_map_label = ttk.Label(
            master=self._root, background="#F0F0F0", text="Valitse kartta")
        selected_map_dropdown = ttk.OptionMenu(
            self._root, self._selected_map, self._available_maps[0], *self._available_maps, command=self._create_map)

        own_style = ttk.Style()
        own_style.configure("Own.TRadiobutton", background="#F0F0F0")

        algorithm_label = ttk.Label(
            master=self._root, background="#F0F0F0", text="Valitse algoritmi")
        ida_star_button = ttk.Radiobutton(master=self._root, text="IDA*", style="Own.TRadiobutton",
                                          variable=self._chosen_algorithm, takefocus=0, value="IDA*")
        dijkstra_button = ttk.Radiobutton(master=self._root, text="Dijkstra", style="Own.TRadiobutton",
                                          variable=self._chosen_algorithm, takefocus=0, value="Dijkstra")

        find_route_btn = ttk.Button(
            master=self._root, text="Löydä lyhin reitti", command=self._handle_validate_input)

        reset_btn = ttk.Button(master=self._root, text="Tyhjennä", command=self._handle_reset)

        self._grid.grid(row=0, column=0, rowspan=6)
        time_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)
        time_elapsed.grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky=constants.W)

        distance_label.grid(row=1, column=1, padx=5, pady=5, sticky=constants.W)
        distance.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky=constants.W)

        start_node_label.grid(row=2, column=1, padx=5, pady=5, sticky=constants.W)
        start_node_entry.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky=constants.W)

        goal_node_label.grid(row=3, column=1, padx=5, pady=5, sticky=constants.W)
        goal_node_entry.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky=constants.W)

        algorithm_label.grid(row=4, column=1, padx=5, pady=5)
        ida_star_button.grid(row=4, column=2, padx=15, sticky=constants.W)
        dijkstra_button.grid(row=4, column=3, padx=15, sticky=constants.E)

        selected_map_label.grid(row=5, column=1, padx=5, pady=5, sticky=constants.W)
        selected_map_dropdown.grid(row=5, column=2, columnspan=2, sticky=constants.EW, padx=5, pady=5)

        find_route_btn.grid(row=6, column=0, columnspan=4, sticky=constants.EW, padx=5, pady=5)

        reset_btn.grid(row=7, column=0, columnspan=4, sticky=constants.EW, padx=5, pady=5)

    def _create_map(self, map=None):
        map_file = self._selected_map.get() if map is None else map
        self._graph, self._map_rows = make_adjacency_lists(f"src/maps/{map_file}")
        self._map_height = len(self._map_rows)
        self._map_width = len(self._map_rows[0])
        square_size = self._GRID_WIDTH / self._map_width

        for y, row in enumerate(self._map_rows):
            for x, column in enumerate(row):
                color = "black" if column == "@" else "white"
                self._grid.create_rectangle(
                    (square_size*x, square_size*y, square_size*(x+1), square_size*(y+1)), width=0, fill=color)

    def _update_map(self, route, visited_nodes):
        self._create_map()
        square_size = self._GRID_WIDTH / self._map_width

        for y in range(self._map_width):
            for x in range(self._map_width):
                node_number = self._map_width * y + x
                if route[0] == node_number or route[len(route)-1] == node_number:
                    color = "green"
                elif node_number in route:
                    color = "red"
                elif visited_nodes[node_number]:
                    color = "yellow"
                else:
                    continue
                self._grid.create_rectangle(
                    (square_size*x, square_size*y, square_size*(x+1), square_size*(y+1)), width=0, fill=color)

    def _get_available_maps(self):
        for file in os.listdir("src/maps"):
            if file.endswith(".map"):
                self._available_maps.append(file)

    def _handle_validate_input(self):
        algorithm = self._chosen_algorithm.get()
        if algorithm == "":
            messagebox.showerror(title="Virhe", message="Valitse algoritmi!")
            return
        start_node = self._start_node.get().split(",")
        end_node = self._end_node.get().split(",")
        if len(start_node) != 2 or len(end_node) != 2:
            messagebox.showerror(title="Virhe", message="Syötä koordinaatit muodossa 0, 0!")
            return
        # Ruudun tunnus saadaan kertomalla sen y-koordinaatti rivin pituudella
        # ja lisäämällä siihen x-koordinaatti
        try:
            start_node = int(start_node[1]) * self._map_width + int(start_node[0])
            end_node = int(end_node[1]) * self._map_width + int(end_node[0])
        except ValueError:
            messagebox.showerror(title="Virhe", message="Syötä koordinaatit muodossa 0, 0!")
            return
        if not self._validate_node_number(start_node) or not self._validate_node_number(end_node):
            max_x = self._map_width - 1
            max_y = self._map_height - 1
            msg = f"Koordinaattien on oltava välillä 0–{max_x}, 0–{max_y}"
            messagebox.showerror(title="Virhe", message=msg)
            return
        if self._is_obstacle(start_node) or self._is_obstacle(end_node):
            msg = "Valitsit alku- tai loppupisteeksi ruudun, jossa on este!"
            messagebox.showerror(title="Virhe", message=msg)
            return
        self._find_route(start_node, end_node)

    def _find_route(self, start_node, end_node):
        if self._chosen_algorithm.get() == "IDA*":
            start_time = time.time()
            route, distance = ida_star(self._graph, start_node, end_node)
            visited = [False for _ in range(len(self._graph))]
            elapsed_time = f"{round(time.time() - start_time, 5)}"
        elif self._chosen_algorithm.get() == "Dijkstra":
            start_time = time.time()
            route, visited, distance = dijkstra(self._graph, start_node, end_node)
            elapsed_time = f"{round(time.time() - start_time, 5)}"
        distance = f"{round(distance, 5)}"
        self._shortest_path_length.set(f"{distance.replace('.', ',')}")
        self._used_time.set(f"{elapsed_time.replace('.', ',')} s")
        self._update_map(route, visited)

    def _validate_node_number(self, node):
        return 0 <= node < len(self._graph)

    def _is_obstacle(self, node):
        x_coord = node % self._map_width
        y_coord = node // self._map_width
        return self._map_rows[y_coord][x_coord] == "@"

    def _handle_reset(self):
        self._create_map()

        self._start_node.set("")
        self._end_node.set("")
        self._used_time.set("")
        self._shortest_path_length.set("")
