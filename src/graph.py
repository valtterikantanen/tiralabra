from math import sqrt


def make_adjacency_lists(filename):
    with open(filename) as file:
        map_rows = []

        for i, line in enumerate(file):
            # Ensimmäiset neljä riviä sisältävät tietoa kartasta
            if i >= 4:
                line = line.replace("\n", "")
                row = list(line)
                map_rows.append(row)

    height = len(map_rows)
    width = len(map_rows[0])

    # Esitetään verkko vieruslistoina ja alustetaan jokainen lista tyhjäksi
    graph = [[] for _ in range(height * width)]

    empty = "."
    occupied = "@"

    # rivin numero = y-koordinaatti (0–255)
    for i, row in enumerate(map_rows):
        # sarakkeen numero = x-koordinaatti (0–255)
        for j, column in enumerate(row):
            if column == occupied:
                continue
            node = i * width + j
            # Käydään läpi kaikki mahdolliset naapurisolmut
            for option in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                y_coord = i + option[0]
                x_coord = j + option[1]
                # Tarkistetaan, menevätkö koordinaatit reunojen yli
                if not 0 <= x_coord < width or not 0 <= y_coord < height:
                    continue
                # Viistoon voidaan liikkua vain, jos kaksi sen viereistä ruutua ovat vapaana
                if option[0] != 0 and option[1] != 0:
                    if option == (-1, -1):
                        if map_rows[i-1][j] != empty or row[j-1] != empty:
                            continue
                    elif option == (-1, 1):
                        if map_rows[i-1][j] != empty or row[j+1] != empty:
                            continue
                    elif option == (1, -1):
                        if row[j-1] != empty or map_rows[i+1][j] != empty:
                            continue
                    elif option == (1, 1):
                        if row[j+1] != empty or map_rows[i+1][j] != empty:
                            continue
                if map_rows[y_coord][x_coord] == empty:
                    # Jos liikuttiin vaaka- tai pystysuunnassa, kaaren paino on 1, muuten sqrt(2)
                    weight = 1 if option[0] == 0 or option[1] == 0 else sqrt(2)
                    endpoint = y_coord * width + x_coord
                    graph[node].append((weight, endpoint))
    return graph, map_rows
