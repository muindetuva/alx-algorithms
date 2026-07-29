#!/usr/bin/python3
"""Breadth-first and recursive depth-first graph traversals."""

from collections import deque


GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}


def bfs(graph, start):
    """Return breadth-first visiting order from start using a queue."""
    queue = deque([start])
    visited = {start}
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbour in graph.get(vertex, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return order


def dfs(graph, start):
    """Return recursive depth-first visiting order from start."""
    visited = set()
    order = []

    def visit(vertex):
        visited.add(vertex)
        order.append(vertex)
        for neighbour in graph.get(vertex, []):
            if neighbour not in visited:
                visit(neighbour)

    visit(start)
    return order


def bfs_states(graph, start):
    """Return queue and visited snapshots after each processed vertex."""
    queue = deque([start])
    visited = {start}
    states = []

    while queue:
        vertex = queue.popleft()
        for neighbour in graph.get(vertex, []):
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
        states.append((vertex, list(queue), sorted(visited)))

    return states


def dfs_states(graph, start):
    """Return recursion-path snapshots when vertices are entered."""
    visited = set()
    states = []

    def visit(vertex, path):
        visited.add(vertex)
        current_path = path + [vertex]
        states.append((vertex, current_path, sorted(visited)))
        for neighbour in graph.get(vertex, []):
            if neighbour not in visited:
                visit(neighbour, current_path)

    visit(start, [])
    return states


if __name__ == "__main__":
    print("BFS order:", " → ".join(bfs(GRAPH, "A")))
    print("DFS order:", " → ".join(dfs(GRAPH, "A")))

    print("\nBFS queue states:")
    for vertex, queue, visited in bfs_states(GRAPH, "A"):
        print(f"after {vertex}: queue={queue}, visited={visited}")

    print("\nDFS entry paths:")
    for vertex, path, visited in dfs_states(GRAPH, "A"):
        print(f"enter {vertex}: path={path}, visited={visited}")
