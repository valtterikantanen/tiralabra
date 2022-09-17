from heapq import heappush, heappop
from math import inf

def dijkstra(graph, start, end):
    # Alustetaan kaikki solmut käsittelemättömiksi
    visited = [False for _ in range(len(graph))]
    heap = []
    # Alustetaan aloitussolmua lukuun ottamatta kaikkien solmujen etäisyyksiksi ääretön
    distances = {node: inf for node in range(len(graph))}
    distances[start] = 0
    heappush(heap, (0, start))
    while len(heap) > 0:
        node = heappop(heap)[1]
        if visited[node]:
            continue
        visited[node] = True
        for edge in graph[node]:
            # Vieruslistan alkiot ovat muotoa (paino, tunnus)
            current_distance = distances[edge[1]]
            new_distance = distances[node] + edge[0]
            if new_distance < current_distance:
                distances[edge[1]] = new_distance
                heappush(heap, (new_distance, edge[1]))
    return distances[end]
