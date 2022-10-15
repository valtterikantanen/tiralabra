from math import inf

from heap import Heap


def dijkstra(graph, start, end):
    """Määrittää lyhimmän reitin kahden solmun välillä annetussa verkossa.

    Args:
        graph: Käytettävä verkko vieruslistamuodossa
        start: Aloitussolmun tunnus
        end: Maalisolmun tunnus

    Returns:
        Tuple, jossa on lista reittiin kuuluvista solmuista, lista siitä, onko kussakin verkon
        solmussa vierailtu vai ei sekä aloitussolmun ja maalisolmun välinen etäisyys.
    """

    # Alustetaan kaikki solmut käsittelemättömiksi
    visited = [False for _ in range(len(graph))]
    previous = [None for _ in range(len(graph))]
    heap = Heap()
    # Alustetaan aloitussolmua lukuun ottamatta kaikkien solmujen etäisyyksiksi ääretön
    distances = {node: inf for node in range(len(graph))}
    distances[start] = 0
    heap.insert((0, start))
    while not heap.is_empty():
        node = heap.extract()[1]
        if visited[node]:
            continue
        if node == end:
            break
        visited[node] = True
        for edge in graph[node]:
            # Vieruslistan alkiot ovat muotoa (paino, tunnus)
            current_distance = distances[edge[1]]
            new_distance = distances[node] + edge[0]
            if new_distance < current_distance:
                previous[edge[1]] = node
                distances[edge[1]] = new_distance
                heap.insert((new_distance, edge[1]))
    route = _create_route(previous, end)

    return route, visited, distances[end]


def _create_route(previous_nodes, end_node):
    """Muodostaa polun maalisolmusta aloitussolmuun.

    Args:
        previous_nodes: Lista, jossa on tieto kunkin solmun edeltäjästä
        end_node: Maalisolmun tunnus

    Returns:
        Löydetty reitti listana.
    """

    route = [end_node]
    i = end_node
    while previous_nodes[i] is not None:
        route.insert(0, previous_nodes[i])
        i = previous_nodes[i]

    return route
