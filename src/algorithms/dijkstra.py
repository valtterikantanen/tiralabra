from math import inf

from util.heap import Heap


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
    heap = Heap()
    # Alustetaan aloitussolmua lukuun ottamatta kaikkien solmujen etäisyyksiksi ääretön
    # Sanakirjaan lisätään tuplena tieto solmun etäisyydestä aloitussolmuun sekä sen edeltäjä
    distances = {node: (inf, None) for node in range(len(graph))}
    distances[start] = (0, None)
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
            current_distance = distances[edge[1]][0]
            new_distance = distances[node][0] + edge[0]
            if new_distance < current_distance:
                distances[edge[1]] = (new_distance, node)
                heap.insert((new_distance, edge[1]))
    route = _create_route(distances, end)

    return route, visited, distances[end][0]


def _create_route(distances, end_node):
    """Muodostaa polun maalisolmusta aloitussolmuun.

    Args:
        distances: Sanakirja, jonka avaimina ovat solmujen tunnukset ja arvoina tuplet, joissa on
        etäisyys aloitussolmusta sekä tieto solmun edeltäjästä
        end_node: Maalisolmun tunnus

    Returns:
        Löydetty reitti listana.
    """

    route = [end_node]
    previous_node = distances[end_node][1]
    while previous_node is not None:
        route.insert(0, previous_node)
        previous_node = distances[previous_node][1]

    return route
