from heapq import heapify, heappop
from typing import NamedTuple

type WeightedGraph = dict[str, set[tuple[str, int]]]


class Edge(NamedTuple):

    weight: int
    u: str
    v: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Edge):
            return False
        return (self.weight == other.weight
                and ((self.u == other.u and self.v == other.v)
                     or (self.u == other.v and self.v == other.u)))

    def __hash__(self) -> int:
        return hash(self.weight) + hash(self.u) + hash(self.v)

def kruskal_mst(graph: WeightedGraph) -> tuple[int, WeightedGraph]:
    queue: list[Edge] = make_heap(graph)
    result: WeightedGraph = {k: set() for k in graph}
    remaining_edges: int = len(graph) - 1
    total: int = 0
    visited: set[str] = set()
    while remaining_edges:
        edge: Edge = heappop(queue)
        add_edge(result, edge)
        if (edge.u in visited
                and edge.v in visited
                and has_cycle(edge.u, result)):
            remove_edge(result, edge)
        else:
            visited.add(edge.u)
            visited.add(edge.v)
            total += edge.weight
            remaining_edges -= 1
    return (total, result)


def make_heap(graph: WeightedGraph) -> list[Edge]:
    result: set[Edge] = set()
    u: str
    neighbors: set[tuple[str, int]]
    for u, neighbors in graph.items():
        v: str
        weight: int
        for v, weight in neighbors:
            result.add(Edge(weight, u, v))
    queue: list[Edge] = list(result)
    heapify(queue)
    return queue


def add_edge(graph: WeightedGraph, edge: Edge) -> None:
    weight, u, v = edge
    graph[u].add((v, weight))
    graph[v].add((u, weight))


def remove_edge(graph: WeightedGraph, edge: Edge) -> None:
    weight, u, v = edge
    graph[u].remove((v, weight))
    graph[v].remove((u, weight))


def has_cycle(
        initial: str,
        graph: WeightedGraph,
        visited: set[str] | None = None,
        parent: str | None = None) -> bool:
    if visited is None:
        visited = set()
    visited.add(initial)
    vertex: str
    for vertex, _ in graph[initial]:
        if vertex in visited:
            if vertex != parent:
                return True
        elif has_cycle(vertex, graph, visited, initial):
            return True
    return False


if __name__ == '__main__':
    from pprint import pprint
    g1: WeightedGraph = {
        'A': {('B', 2), ('C', 6), ('D', 5)},
        'B': {('A', 2), ('C', 8), ('D', 11)},
        'C': {('A', 6), ('B', 8), ('D', 1)},
        'D': {('A', 5), ('B', 11), ('C', 1)}
    }
    g2: WeightedGraph = {
        'A': {('B', 1), ('D', 12), ('F', 6)},
        'B': {('A', 1), ('C', 15), ('D', 13), ('E', 9)},
        'C': {('B', 15), ('E', 3), ('G', 7)},
        'D': {('A', 12), ('B', 13), ('F', 14), ('G', 2)},
        'E': {('B', 9), ('C', 3), ('F', 10), ('G', 8)},
        'F': {('A', 6), ('D', 14), ('E', 10), ('G', 11), ('H', 4)},
        'G': {('C', 7), ('D', 2), ('E', 8), ('F', 11), ('H', 5)},
        'H': {('F', 4), ('G', 5)}
    }
    pprint(kruskal_mst(g1))
    pprint(kruskal_mst(g2))
