from math import floor

# Minimikeon toteuttava luokka

# Taulukon indeksointi alkaa 1:stä
# Pienin alkio aina juuressa eli indeksissä 1
# Jos solmu on kohdassa k, niin vasen lapsi on kohdassa 2k, oikea lapsi kohdassa 2k+1 ja vanhempi kohdassa floor(k/2)
# Pienimmän alkion löytäminen ajassa O(1), alkion lisääminen tai pienimmän alkion poistaminen ajassa O(log n)

class Heap:
    def __init__(self):
        self.__heap = [None]

    # Lisää alkion kekoon
    def insert(self, item):
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

    # Poistaa pienimmän alkion keosta
    def extract(self):
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

        return smallest_item

    def size(self):
        return len(self.__heap) - 1

    def is_empty(self):
        return self.size() == 0

    def __str__(self):
        return f"{self.__heap[1:]}"
