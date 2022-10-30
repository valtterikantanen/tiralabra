from math import sqrt, inf


def ida_star(graph, start, goal):
    """Määrittää lyhimmän reitin kahden solmun välillä annetussa verkossa IDA*-algoritmilla.

    Args:
        graph: Käytettävä verkko vieruslistamuodossa
        start: Aloitussolmun tunnus
        goal: Maalisolmun tunnus

    Returns:
        Tuple, jossa on lista reittiin kuuluvista solmuista
        sekä aloitussolmun ja maalisolmun välinen etäisyys.
    """

    # Jos lähtö- tai maalisolmussa on este, reittiä ei voi löytyä
    if len(graph[start]) == 0 or len(graph[goal]) == 0:
        return ([start, goal], inf)
    # Otetaan arvioksi lyhin mahdollinen etäisyys lähtösolmusta maalisolmuun
    bound = _estimate_shortest_path(start, goal, int(sqrt(len(graph))))
    path = [start]
    while True:
        # Kasvatetaan arviota joka kierroksella, kunnes maalisolmu löytyy tai sinne ei ole reittiä
        threshold = _search(graph, 0, bound, goal, path)
        # Maalisolmu löytynyt
        if threshold is True:
            return (path, bound)
        if threshold == inf:
            # Lisätään maalisolmu "reittiin", jotta käyttöliittymä näyttää myös maaliruudun
            path.append(goal)
            return (path, threshold)
        bound = threshold


def _search(graph, g_score, bound, goal, path):
    """Rekursiivinen apufunktio IDA*-algoritmille.

    Args:
        graph: Käytettävä verkko vieruslistamuodossa
        g_score: Polun nykyinen pituus (g-arvo)
        bound: Yläraja sille, minkä pituisia reittejä haetaan
        goal: Maalisolmun tunnus
        path: Lista polkuun kuuluvista solmuista

    Returns:
        True, jos reitti maaliin on löytynyt, muuten lyhimmän löydetyn reitin pituus.
    """

    # Valitaan käsiteltäväksi polun viimeinen solmu
    current_node = path[-1]
    # Uusi f-arvo on g-arvo lisättynä arviolla maalisolmun etäisyydestä
    f_score = g_score + _estimate_shortest_path(current_node, goal, int(sqrt(len(graph))))
    if f_score > bound:
        return f_score
    if current_node == goal:
        return True
    # Alustetaan minimietäisyydeksi ääretön ja käydään käsiteltävän solmun naapurit läpi
    minimum = inf
    for neighbor in graph[current_node]:
        # Vieruslistassa on paino ja naapurin tunnus
        weight, end_node = neighbor
        if end_node not in path:
            path.append(end_node)
            # Kutsutaan funktiota rekursiivisesti niin että g-arvoon lisätään naapurin etäisyys
            threshold = _search(graph, g_score+weight, bound, goal, path)
            if threshold is True:
                return True
            if threshold < minimum:
                minimum = threshold
            path.pop()
    return minimum


def _estimate_shortest_path(start, end, width):
    """Laskee arvion lyhimmän polun pituudesta parametrina annetun kahden solmun välillä. Arvio
    lasketaan niin, että ensin edetään viistoon, kunnes ollaan samalla pysty- tai vaaka-akselilla
    ja tämän jälkeen edetään pysty- tai vaakasuunnassa.

    Args:
        start: Aloitussolmun tunnus
        end: Maalisolmun tunnus
        width: Kartan leveys (ruutuina)

    Returns:
        Arvio lyhimmän polun pituudesta.
    """

    # Muutetaan ruutujen numerot x- ja y-koordinaateiksi
    x_1, y_1 = start % width, start // width
    x_2, y_2 = end % width, end // width
    x_distance = abs(x_1 - x_2)
    y_distance = abs(y_1 - y_2)
    # Vinosuuntainen siirtymä
    distance = min(x_distance, y_distance) * sqrt(2)
    # Vaaka- tai pystysuuntainen siirtymä
    distance += max(x_distance, y_distance) - min(x_distance, y_distance)
    return distance
