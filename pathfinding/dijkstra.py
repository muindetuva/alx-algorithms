#!/usr/bin/python3
"""Compare naive edge-greedy routing with Dijkstra's algorithm."""

import heapq
import math


GRAPH = {
    "A": [("B", 2), ("C", 5)],
    "B": [("D", 9)],
    "C": [("D", 3)],
    "D": [],
}


def dijkstra(graph, start):
    """Return shortest distances and predecessors from start."""
    distances = {vertex: math.inf for vertex in graph}
    previous = {vertex: None for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, vertex = heapq.heappop(queue)
        if current_distance != distances[vertex]:
            continue

        for neighbour, weight in graph[vertex]:
            if weight < 0:
                message = "Dijkstra's algorithm requires non-negative weights"
                raise ValueError(message)
            candidate = current_distance + weight
            if candidate < distances[neighbour]:
                distances[neighbour] = candidate
                previous[neighbour] = vertex
                heapq.heappush(queue, (candidate, neighbour))

    return distances, previous


def shortest_path(previous, start, target):
    """Reconstruct a path from start to target using predecessors."""
    path = []
    current = target

    while current is not None:
        path.append(current)
        if current == start:
            return list(reversed(path))
        current = previous.get(current)

    return []


if __name__ == "__main__":
    shortest_distances, predecessors = dijkstra(GRAPH, "A")
    route = shortest_path(predecessors, "A", "D")

    print("Shortest distances from A:", shortest_distances)
    print("Shortest path A -> D:", " -> ".join(route))
    print("Shortest distance A -> D:", shortest_distances["D"])
