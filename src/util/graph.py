from math import sqrt


def make_adjacency_lists(filename):
    """Muodostaa annetun tiedoston perusteella verkon vieruslistamuodossa.

    Args:
        filename: Polku tiedostoon

    Returns:
        Tuple, jossa on verkko vieruslistamuodossa sekä parametrina annettu kartta matriisimuodossa.
    """

    map_rows = _create_map_from_file(filename)

    height = len(map_rows)
    width = len(map_rows[0])

    # Esitetään verkko vieruslistoina ja alustetaan jokainen lista tyhjäksi
    graph = [[] for _ in range(height * width)]

    empty = "."

    # Rivin numero = y-koordinaatti
    for i, row in enumerate(map_rows):
        # Sarakkeen numero = x-koordinaatti
        for j, column in enumerate(row):
            if column != empty:
                continue
            # Käydään läpi kaikki mahdolliset naapurisolmut
            for option in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                y = i + option[0]
                x = j + option[1]
                # Tarkistetaan, menevätkö koordinaatit reunojen yli
                if not 0 <= x < width or not 0 <= y < height:
                    continue
                # Viistoon voidaan liikkua vain, jos kaksi sen viereistä ruutua ovat vapaana
                if 0 not in option and map_rows[y][j] != empty or row[x] != empty:
                    continue
                if map_rows[y][x] == empty:
                    # Jos liikuttiin vaaka- tai pystysuunnassa, kaaren paino on 1, muuten sqrt(2)
                    weight = 1 if 0 in option else sqrt(2)
                    # Solmun tunnus saadaan kaavalla leveys * y-koordinaatti + x-koordinaatti
                    endpoint = width * y + x
                    graph[width * i + j].append((weight, endpoint))
    return graph, map_rows


def _create_map_from_file(filename):
    """Muodostaa annetusta karttatiedostosta listan.

    Args:
        filename: Polku tiedostoon

    Returns:
        Kartta matriisimuodossa, jossa yksi kartan rivi muodostaa yhden listan matriisin sisällä.
    """

    with open(filename) as file:
        map_rows = []

        for i, line in enumerate(file):
            # Ensimmäiset neljä riviä sisältävät tietoa kartasta
            if i >= 4:
                line = line.replace("\n", "")
                row = list(line)
                map_rows.append(row)
    return map_rows
