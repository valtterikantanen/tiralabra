import time

import pygame

from graph import make_adjacency_lists
from dijkstra import dijkstra

WIDTH = 768
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Dijkstra")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def draw(win, grid, width, route):
    win.fill(WHITE)

    gap = width // len(grid)

    # Ruudun nro = rivin nro (0-255) * 256 + sarakkeen_nro (0-255)

    for i, row in enumerate(grid):
        for j, spot in enumerate(row):
            if spot == ".":
                if 256*i + j in route:
                    color = RED
                else:
                    color = WHITE
            elif spot == "@":
                color = BLACK
            pygame.draw.rect(win, color, (gap*j, gap*i, width, width))

    pygame.display.update()

def main(win, width, map_rows, route):
    grid = map_rows

    running = True
    while running:
        draw(win, grid, width, route)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

start = time.time()
graph, map_rows = make_adjacency_lists("src/maps/Berlin_0_256.map")
# Esimerkki, jonka pitäisi tulostaa arvo 369.44574280
route, distance = dijkstra(graph, 6409, 64501)
print(f"Etäisyys on {distance}.")
print(f"Reitti kulki {len(route)} ruudun kautta.")
print(f"Reitin löytämiseen kului {time.time() - start} sekuntia")

main(WIN, WIDTH, map_rows, route)
