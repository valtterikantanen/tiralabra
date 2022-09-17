from math import sqrt

def make_adjacency_lists(filename: str):
    with open(filename) as file:
        map = []

        for i, line in enumerate(file):
            # Ensimmäiset neljä riviä sisältävät tietoa kartasta
            if i >= 4:
                line = line.replace("\n", "")
                row = [i for i in line]
                map.append(row)

    height = len(map)
    width = len(map[0])

    # Esitetään verkko vieruslistoina ja alustetaan jokainen lista tyhjäksi
    graph = [[] for _ in range(height * width)]

    empty = "."
    occupied = "@"

    for i, row in enumerate(map): # rivin numero = y-koordinaatti (0–255)
        for j, column in enumerate(row): # sarakkeen numero = x-koordinaatti (0–255)
            if column == occupied:
                continue
            node = i * width + j
            # Käydään läpi kaikki mahdolliset naapurisolmut
            for option in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                y_coord = i + option[0]
                x_coord = j + option[1]
                # Tarkistetaan, menevätkö koordinaatit reunojen yli
                if not (0 <= x_coord < width) or not (0 <= y_coord < height):
                    continue
                # Viistoon voidaan liikkua vain, jos kaksi sen viereistä ruutua ovat vapaana
                if option[0] != 0 and option[1] != 0:
                    if option == (-1, -1):
                        if map[i-1][j] != empty or map[i][j-1] != empty:
                            continue
                    elif option == (-1, 1):
                        if map[i-1][j] != empty or map[i][j+1] != empty:
                            continue
                    elif option == (1, -1):
                        if map[i][j-1] != empty or map[i+1][j] != empty:
                            continue
                    elif option == (1, 1):
                        if map[i][j+1] != empty or map[i+1][j] != empty:
                            continue
                if map[y_coord][x_coord] == empty:
                    # Jos liikuttiin vain vaaka- tai pystysuunnassa, kaaren paino on 1, muuten sqrt(2)
                    weight = 1 if option[0] == 0 or option[1] == 0 else sqrt(2)
                    endpoint = y_coord * width + x_coord
                    graph[node].append((weight, endpoint))
    return graph