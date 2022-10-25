from tkinter import ttk, constants, Canvas, messagebox

from services.ui_logic import UILogic


class UI:

    def __init__(self, root, ui_logic: UILogic):
        self._root = root
        self._ui_logic = ui_logic
        self._root.configure(bg="#F0F0F0")

        self._grid = Canvas(master=self._root, height=self._ui_logic.grid_width,
                            width=self._ui_logic.grid_width)

        self._draw_map()

    def start(self):
        time_label = ttk.Label(master=self._root, background="#F0F0F0", text="Aikaa kului")
        time_elapsed = ttk.Label(master=self._root, background="#F0F0F0",
                                 textvariable=self._ui_logic.used_time)

        distance_label = ttk.Label(master=self._root, background="#F0F0F0", text="Reitin pituus")
        distance = ttk.Label(master=self._root, background="#F0F0F0",
                             textvariable=self._ui_logic.shortest_path_length)

        start_node_label = ttk.Label(master=self._root, background="#F0F0F0", text="Lähtöruutu")
        start_node_entry = ttk.Entry(
            master=self._root, textvariable=self._ui_logic.start_node_input)

        goal_node_label = ttk.Label(master=self._root, background="#F0F0F0", text="Maaliruutu")
        goal_node_entry = ttk.Entry(master=self._root, textvariable=self._ui_logic.end_node_input)

        selected_map_label = ttk.Label(
            master=self._root, background="#F0F0F0", text="Kartta")
        selected_map_dropdown = ttk.OptionMenu(self._root, self._ui_logic.selected_map,
                                               self._ui_logic.available_maps[0],
                                               *self._ui_logic.available_maps,
                                               command=self._handle_reset_map)

        own_style = ttk.Style()
        own_style.configure("Own.TRadiobutton", background="#F0F0F0")

        algorithm_label = ttk.Label(
            master=self._root, background="#F0F0F0", text="Algoritmi")
        ida_star_button = ttk.Radiobutton(master=self._root, text="IDA*", style="Own.TRadiobutton",
                                          variable=self._ui_logic.chosen_algorithm, takefocus=0, value="IDA*")
        dijkstra_button = ttk.Radiobutton(master=self._root, text="Dijkstra", style="Own.TRadiobutton",
                                          variable=self._ui_logic.chosen_algorithm, takefocus=0, value="Dijkstra")

        find_route_btn = ttk.Button(
            master=self._root, text="Löydä lyhin reitti", command=self._handle_validate_input)

        reset_btn = ttk.Button(master=self._root, text="Tyhjennä", command=self._handle_reset_map)

        self._grid.grid(row=0, column=0, rowspan=6)
        time_label.grid(row=0, column=1, padx=5, pady=5, sticky=constants.W)
        time_elapsed.grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky=constants.W)

        distance_label.grid(row=1, column=1, padx=5, pady=5, sticky=constants.W)
        distance.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky=constants.W)

        start_node_label.grid(row=2, column=1, padx=5, pady=5, sticky=constants.W)
        start_node_entry.grid(row=2, column=2, columnspan=2, padx=5, pady=5, sticky=constants.W)

        goal_node_label.grid(row=3, column=1, padx=5, pady=5, sticky=constants.W)
        goal_node_entry.grid(row=3, column=2, columnspan=2, padx=5, pady=5, sticky=constants.W)

        algorithm_label.grid(row=4, column=1, padx=5, pady=5, sticky=constants.W)
        ida_star_button.grid(row=4, column=2, padx=15, sticky=constants.W)
        dijkstra_button.grid(row=4, column=3, padx=15, sticky=constants.E)

        selected_map_label.grid(row=5, column=1, padx=5, pady=5, sticky=constants.W)
        selected_map_dropdown.grid(row=5, column=2, columnspan=2,
                                   sticky=constants.EW, padx=5, pady=5)

        find_route_btn.grid(row=6, column=0, columnspan=4, sticky=constants.EW, padx=5, pady=5)

        reset_btn.grid(row=7, column=0, columnspan=4, sticky=constants.EW, padx=5, pady=5)

        # Hiiren vasemmalla painikkeella valitaan lähtöruutu ja oikealla maaliruutu
        self._grid.bind("<Button-1>", self._handle_click)
        self._grid.bind("<Button-3>", self._handle_click)

    def _draw_map(self, map_file=None):
        map_rows, square_size = self._ui_logic.create_map(map_file)

        for y, row in enumerate(map_rows):
            for x, column in enumerate(row):
                color = "black" if column == "@" else "white"
                self._draw_rectangle(square_size, x, y, color)

    def _handle_reset_map(self, map_file=None):
        self._ui_logic.reset_map()
        self._draw_map(map_file)

    def _update_map(self):
        self._draw_map()
        square_size = self._ui_logic.grid_width / self._ui_logic.map_width

        for y in range(self._ui_logic.map_width):
            for x in range(self._ui_logic.map_width):
                node_number = self._ui_logic.get_node_number(f"{x},{y}")
                color = self._ui_logic.get_node_color(node_number)
                if not color:
                    continue
                self._draw_rectangle(square_size, x, y, color)

    def _draw_rectangle(self, size, x, y, color):
        self._grid.create_rectangle(size*x, size*y, size*(x+1), size*(y+1), width=0, fill=color)

    def _handle_click(self, event):
        if self._ui_logic.handle_click(event) is False:
            messagebox.showerror(title="Virhe", message="Valitsit ruudun, jossa on este!")
            return
        self._update_map()

    def _handle_validate_input(self):
        error_msg = self._ui_logic.validate_input()
        if error_msg:
            messagebox.showerror(title="Virhe", message=error_msg)
        else:
            self._ui_logic.find_route()
            self._update_map()
