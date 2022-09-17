from graph import make_adjacency_lists
from dijkstra import dijkstra

if __name__ == "__main__":
    graph = make_adjacency_lists("maps/Berlin_0_256.map")
    # Esimerkki, jonka pitäisi tulostaa arvo 369.44574280
    distance = dijkstra(graph, 6409, 64501)
    print(distance, 7)
