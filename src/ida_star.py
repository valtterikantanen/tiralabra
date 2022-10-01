from math import sqrt, inf

def ida_star(graph, start_node, goal_node):
    visited_nodes = [False for _ in range(len(graph))]
    # Otetaan arvioksi lyhin mahdollinen etäisyys lähtösolmusta maalisolmuun
    bound = _estimate_shortest_path(start_node, goal_node, int(sqrt(len(graph))))
    path = [start_node]
    while True:
        # Kasvatetaan arviota joka kierroksella, kunnes maalisolmu löytyy tai sinne ei ole reittiä
        threshold = _search(graph, path, 0, bound, goal_node, visited_nodes)
        # Maalisolmu löytynyt
        if threshold is True:
            return (path, visited_nodes, bound)
        if threshold == inf:
            return False
        bound = threshold

def _search(graph, path, g_score, bound, goal_node, visited_nodes):
    # Valitaan käsiteltäväksi polun viimeinen solmu
    current_node = path[len(path)-1]
    visited_nodes[current_node] = True
    # Uusi f-arvo on g-arvo lisättynä arviolla maalisolmun etäisyydestä
    f_score = g_score + _estimate_shortest_path(current_node, goal_node, int(sqrt(len(graph))))
    if f_score > bound:
        return f_score
    if current_node == goal_node:
        return True
    # Alustetaan minimietäisyydeksi ääretön ja käydään käsiteltävän solmun naapurit läpi
    minimum = inf
    for neighbor in graph[current_node]:
        # Vieruslistassa on paino ja naapurin tunnus
        weight, end_node = neighbor
        if end_node not in path:
            path.append(end_node)
            # Kutsutaan funktiota rekursiivisesti niin että g-arvoon lisätään naapurin etäisyys
            threshold = _search(graph, path, g_score+weight, bound, goal_node, visited_nodes)
            if threshold is True:
                return True
            if threshold < minimum:
                minimum = threshold
            path.pop()
    return minimum

def _estimate_shortest_path(start_node, end_node, width):
    # Muutetaan ruutujen numerot x- ja y-koordinaateiksi
    x_1, y_1 = start_node % width, start_node // width
    x_2, y_2 = end_node % width, end_node // width
    x_distance = abs(x_1 - x_2)
    y_distance = abs(y_1 - y_2)
    # Vinosuuntainen siirtymä
    distance = min(x_distance, y_distance) * sqrt(2)
    # Vaaka- tai pystysuuntainen siirtymä
    distance += max(x_distance, y_distance) - min(x_distance, y_distance)
    return distance
