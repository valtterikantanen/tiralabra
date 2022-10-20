from math import floor


class Heap:
    """Minimikeon toteuttava luokka.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden keon.
        """

        self.__heap = [None]

    def insert(self, item):
        """Lisää annetun alkion kekoon ajassa O(log n).

        Args:
            item: Kekoon lisättävä alkio. Jos alkio on tuple, järjestäminen tapahtuu tuplen
            ensimmäisen alkion perusteella.
        """

        self.__heap.append(item)
        position = self.size()

        while position > 1:
            parent_position = floor(position / 2)
            parent = self.__heap[parent_position]
            if parent > self.__heap[position]:
                self.__heap[parent_position] = self.__heap[position]
                self.__heap[position] = parent
                position = parent_position
            else:
                break

    def extract(self):
        """Poistaa pienimmän alkion keosta ajassa O(log n).

        Returns:
            Keon pienin alkio.
        """

        # Jos keossa oli enintään yksi solmu ennen poistoa, ei ole siirrettäviä lapsisolmuja
        if self.is_empty():
            return None
        if self.size() == 1:
            return self.__heap.pop()

        # Pienin alkio indeksissä 1
        smallest_item = self.__heap[1]
        # Poistetaan keon viimeinen solmu ja siirretään se juureen eli indeksiin 1
        last_item = self.__heap.pop()
        self.__heap[1] = last_item

        self._restore_heap_condition()

        return smallest_item

    def _restore_heap_condition(self):
        """Palauttaa kekoehdon voimaan alkion poiston jälkeen.
        """

        # Lasketaan juureen nostettua alkiota alaspäin, kunnes kekoehto on jälleen voimassa
        position = 1
        left_child_position = 2 * position
        while left_child_position <= self.size():
            right_child_position = left_child_position + 1
            # Oletetaan aluksi, että pienempi lapsi on vasemmalla
            # Jos oikea lapsi on olemassa, ja se on pienempi kuin vasen solmu, valitaan se
            smaller_child_position = left_child_position
            if right_child_position <= self.size():
                if self.__heap[right_child_position] < self.__heap[left_child_position]:
                    smaller_child_position = right_child_position
            parent = self.__heap[position]
            smaller_child = self.__heap[smaller_child_position]
            # Jos vanhempi ei ole suurempi kuin pienempi lapsi, vanhempaa ei tarvitse enää laskea
            if parent <= smaller_child:
                break
            self.__heap[position] = self.__heap[smaller_child_position]
            self.__heap[smaller_child_position] = parent
            position = smaller_child_position
            left_child_position = 2 * smaller_child_position

    def size(self):
        """Palauttaa keon koon.

        Returns:
            Keon koko kokonaislukuna.
        """

        return len(self.__heap) - 1

    def is_empty(self):
        """Palauttaa tiedon siitä, onko keko tyhjä.

        Returns:
            True, jos keko on tyhjä ja False, jos ei ole.
        """

        return self.size() == 0

    def __str__(self):
        """Palauttaa keon kuvauksen merkkijonona.

        Returns:
            Keko merkkijonona, jonka sisältönä on lista keon alkioista.
        """

        return f"{self.__heap[1:]}"
