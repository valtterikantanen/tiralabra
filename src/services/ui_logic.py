import os
import time

from tkinter import StringVar

from algorithms.dijkstra import dijkstra
from algorithms.ida_star import ida_star
from util.graph import make_adjacency_lists


class UILogic:
    """Käyttöliittymälogiikasta vastaava luokka."""

    def __init__(self, grid_width=600):
        """Luokan konstruktori.

        Args:
            grid_width: Käyttöliittymään haluttu kartan leveys (pikseleinä). Oletuksena 600.
        """

        self.grid_width = grid_width

        self.start_node_input = StringVar()
        self.end_node_input = StringVar()
        self.used_time = StringVar()
        self.shortest_path_length = StringVar()
        self.chosen_algorithm = StringVar()
        self.available_maps = self._get_available_maps()
        self.selected_map = StringVar(value=self.available_maps[0])

        self.map_width = None
        self._map_height = None
        self._map_rows = None
        self._graph = None
        self._start_node = None
        self._end_node = None
        self._route = None
        self._visited_nodes = None

    def _get_available_maps(self):
        """Hakee hakemistossa src/maps sijaitsevat kartat.

        Returns:
            Lista karttatiedostojen nimistä.
        """

        available_maps = []
        for file in os.listdir("src/maps"):
            if file.endswith(".map"):
                available_maps.append(file)
        return available_maps

    def create_map(self, map_file=None):
        """Luo annetusta kartasta olion, jonka perusteella voidaan laatia visuaalinen vastine.

        Args:
            map_file: Käytettävän kartan nimi, oletuksena None (jolloin haetaan valittu kartta).

        Returns:
            Tuple, jossa on kartta matriisimuodossa sekä yhden ruudun koko pikseleinä.
        """

        map_file = self.selected_map.get() if map_file is None else map_file
        self._graph, self._map_rows = make_adjacency_lists(f"src/maps/{map_file}")
        self._map_height = len(self._map_rows)
        self.map_width = len(self._map_rows[0])
        square_size = self.grid_width / self.map_width

        return self._map_rows, square_size

    def reset_map(self):
        """Palauttaa kartan alkutilanteeseen ja nollaa muuttujat."""

        self.create_map()

        self.start_node_input.set("")
        self.end_node_input.set("")
        self.used_time.set("")
        self.shortest_path_length.set("")
        self._route = None
        self._visited_nodes = None
        self._start_node = None
        self._end_node = None

    def handle_click(self, event):
        """Vastaa kartan klikkauksen käsittelystä

        Args:
            event: TkInterin Event-olio, joka sisältää tiedot klikkauksesta.

        Returns:
            False, jos aloitus- tai lähtösolmua ei voitu valita, muuten True.
        """

        width = self.grid_width / self.map_width
        height = self.grid_width / self._map_height

        x = int(event.x // width)
        y = int(event.y // height)

        coord_as_str = f"{x}, {y}"
        node_number = self.get_node_number(coord_as_str)

        if self._is_obstacle(node_number):
            return False

        if self._route is not None:
            self.reset_map()

        # Aloitusruutu asetetaan hiiren vasemmalla näppäimellä, jolloin numero on 1, oikealla 3
        if event.num == 1:
            self.start_node_input.set(coord_as_str)
            self._start_node = node_number
        elif event.num == 3:
            self.end_node_input.set(coord_as_str)
            self._end_node = node_number

        return True

    def find_route(self):
        """Hakee lyhimmän reitin kahden annetun solmun välillä."""

        start_time = time.time()
        if self.chosen_algorithm.get() == "IDA*":
            self._route, distance = ida_star(self._graph, self._start_node, self._end_node)
            self._visited_nodes = [False for _ in range(len(self._graph))]
        elif self.chosen_algorithm.get() == "Dijkstra":
            self._route, self._visited_nodes, distance = dijkstra(
                self._graph, self._start_node, self._end_node)
        else:
            return
        used_time = time.time() - start_time
        self._set_used_time_and_distance(used_time, distance)

    def _set_used_time_and_distance(self, used_time, distance):
        """Asettaa käyttöliittymän muuttujiin lyhimmän etäisyyden kahden
        pisteen välillä ja reitin etsintään käytetyn ajan.

        Args:
            used_time: Reitin etsintään käytetty aika
            distance: Lyhimmän löydetyn reitin pituus
        """

        used_time = f"{round(used_time, 5)}"
        distance = f"{round(distance, 5)}"
        distance = "∞" if distance == "inf" else distance
        self.shortest_path_length.set(f"{distance.replace('.', ',')}")
        self.used_time.set(f"{used_time.replace('.', ',')} s")

    def validate_input(self):
        """Tarkistaa, että tarvittavat syötteet ovat oikein.

        Returns:
            Jos virheitä ei ollut, palauttaa tyhjän merkkijonon, muuten virheviestin.
        """

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
        """Tarkistaa, että solmun numero on sallitulla välillä.

        Args:
            node: Kokonaisluku, joka edustaa solmun tunnusta.

        Returns:
            True, jos solmun numero on mahdollinen, muuten False.
        """

        return 0 <= node < len(self._graph)

    def _is_obstacle(self, node):
        """Tarkistaa, onko parametrina annetussa solmussa este.

        Args:
            node: Kokonaisluku, joka edustaa solmun tunnusta.

        Returns:
            True, jos solmussa on este, muuten False.
        """

        x, y = self._get_coordinates(node)
        return self._map_rows[y][x] == "@"

    def _get_coordinates(self, node):
        """Muuttaa solmun tunnuksen koordinaateiksi.

        Args:
            node: Solmun tunnusta edustava kokonaisluku.

        Returns:
            Tuple, jossa on solmun x- ja y-koordinaatit.
        """

        x = node % self.map_width
        y = node // self.map_width
        return x, y

    def get_node_number(self, node):
        """Muuttaa koordinaatit solmun tunnukseksi.

        Args:
            node: Merkkijono muotoa "x, y"

        Returns:
            Jos syöte oli vaadittua muotoa, palauttaa solmun tunnuksen, muuten False.
        """

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
        """Palauttaa solmun värin kartan piirtämistä varten.

        Args:
            node: Solmun tunnus.

        Returns:
            Merkkijono, joka on tyhjä (jolloin solmu ei kuulu polkuun tai vierailtuihin solmuihin)
            tai green, red tai yellow solmun roolin mukaan.
        """

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
