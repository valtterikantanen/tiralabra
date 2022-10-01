import time

from tkinter import Tk, ttk, constants, StringVar, Canvas
from dijkstra import dijkstra
from graph import make_adjacency_lists
from ida_star import ida_star

class UI:

    def __init__(self, root):
        self._root = root
        self._root.configure(bg="#F0F0F0")
        self._MAP_WIDTH = 400
        self._map = Canvas(master=self._root, height=self._MAP_WIDTH, width=self._MAP_WIDTH)
        
        self._chosen_algorithm = StringVar()
        self._start_node = StringVar()
        self._end_node = StringVar()
        self._used_time = StringVar()
        self._shortest_path_length = StringVar()

        self._graph = None
        self._row_length = None
        
        self._create_map()
    
    def start(self):
        time_label = ttk.Label(master=self._root, background="#F0F0F0", text="Aikaa kului")
        time_elapsed = ttk.Label(master=self._root, background="#F0F0F0", textvariable=self._used_time)

        distance_label = ttk.Label(master=self._root, background="#F0F0F0", text="Reitin pituus")
        distance = ttk.Label(
            master=self._root, background="#F0F0F0", textvariable=self._shortest_path_length)

        start_node_label = ttk.Label(master=self._root, background="#F0F0F0", text="Lähtöruutu")
        start_node_entry = ttk.Entry(master=self._root, textvariable=self._start_node)

        goal_node_label = ttk.Label(master=self._root, background="#F0F0F0", text="Maaliruutu")
        goal_node_entry = ttk.Entry(master=self._root, textvariable=self._end_node)

        own_style = ttk.Style()
        own_style.configure("Own.TRadiobutton", background="#F0F0F0")

        algorithm_label = ttk.Label(
            master=self._root, background="#F0F0F0", text="Valitse algoritmi")
        ida_star_button = ttk.Radiobutton(
            master=self._root, text="IDA*", style="Own.TRadiobutton",
            variable=self._chosen_algorithm, takefocus=0, value="IDA*"
        )
        dijkstra_button = ttk.Radiobutton(
            master=self._root, text="Dijkstra", style="Own.TRadiobutton",
            variable=self._chosen_algorithm, takefocus=0, value="Dijkstra"
        )

        find_route_btn = ttk.Button(
            master=self._root, text="Löydä lyhin reitti", command=self._handle_find_route)

        reset_btn = ttk.Button(master=self._root, text="Tyhjennä", command=self._handle_reset)

        self._map.grid(row=0, column=0, rowspan=4)
        time_label.grid(row=0, column=1)
        time_elapsed.grid(row=0, column=2)

        distance_label.grid(row=1, column=1)
        distance.grid(row=1, column=2)

        start_node_label.grid(row=2, column=1)
        start_node_entry.grid(row=2, column=2)

        goal_node_label.grid(row=3, column=1)
        goal_node_entry.grid(row=3, column=2)

        algorithm_label.grid(row=4, column=0, padx=5, pady=5)
        ida_star_button.grid(row=4, column=1, padx=5, pady=5)
        dijkstra_button.grid(row=4, column=2, padx=5, pady=5)

        find_route_btn.grid(
            row=5, column=0, columnspan=3, sticky=(constants.E, constants.W), padx=5, pady=5)

        reset_btn.grid(
            row=6, column=0, columnspan=3, sticky=(constants.E, constants.W), padx=5, pady=5)

    def _create_map(self):
        self._graph, map_rows = make_adjacency_lists("src/maps/Map_20.map")
        self._row_length = len(map_rows)
        square_size = self._MAP_WIDTH / self._row_length

        for y, row in enumerate(map_rows):
            for x, column in enumerate(row):
                color = "black" if column == "@" else "white"
                self._map.create_rectangle(
                    (square_size*x, square_size*y, square_size*(x+1), square_size*(y+1)),
                    width=0, fill=color
                )

    def _update_map(self, route, visited_nodes):
        self._create_map()
        square_size = self._MAP_WIDTH / self._row_length

        for y in range(self._row_length):
            for x in range(self._row_length):
                node_number = self._row_length * y + x
                if route[0] == node_number or route[len(route)-1] == node_number:
                    color = "green"
                elif node_number in route:
                    color = "red"
                elif visited_nodes[node_number]:
                    color = "yellow"
                else:
                    continue
                self._map.create_rectangle(
                    (square_size*x, square_size*y, square_size*(x+1), square_size*(y+1)),
                    width=0, fill=color
                )

    def _handle_find_route(self):
        algorithm = self._chosen_algorithm.get()
        start_node = self._start_node.get().split(",")
        end_node = self._end_node.get().split(",")
        # Ruudun tunnus saadaan kertomalla sen y-koordinaatti rivin pituudella
        # ja lisäämällä siihen x-koordinaatti
        start_node = int(start_node[1]) * self._row_length + int(start_node[0])
        end_node = int(end_node[1]) * self._row_length + int(end_node[0])

        if algorithm == "IDA*":
            start_time = time.time()
            route, visited, distance = ida_star(self._graph, start_node, end_node)
            elapsed_time = f"{round(time.time() - start_time, 5)}"
        elif algorithm == "Dijkstra":
            start_time = time.time()
            route, visited, distance = dijkstra(self._graph, start_node, end_node)
            elapsed_time = f"{round(time.time() - start_time, 5)}"
        distance = f"{round(distance, 5)}"
        self._shortest_path_length.set(f"{distance.replace('.', ',')}")
        self._used_time.set(f"{elapsed_time.replace('.', ',')} s")
        self._update_map(route, visited)

    def _handle_reset(self):
        self._create_map()

        self._start_node.set("")
        self._end_node.set("")
        self._used_time.set("")
        self._shortest_path_length.set("")
