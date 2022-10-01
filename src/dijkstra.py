from math import inf

from heap import Heap

def dijkstra(graph, start, end):
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
    route = [end]
    i = end
    while previous[i] is not None:
        route.insert(0, previous[i])
        i = previous[i]
    return route, visited, distances[end]
