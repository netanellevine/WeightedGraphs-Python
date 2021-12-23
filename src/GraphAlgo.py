import math
import heapq
from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface


class Trio:
    def __init__(self, prev: int, to: int, weight: float):
        self.prev: int = prev
        self.to: int = to
        self.weight: float = weight


class Father:
    def __init__(self, prev: int, weight: float):
        self.prev: int = prev
        self.weight: float = weight


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: GraphInterface):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        return True

    def save_to_json(self, file_name: str) -> bool:
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        di = self.djikstra_shortest(id1, id2)
        path = [id2]
        prev = di.get(id2).prev
        while path[0] != id1:
            path.insert(0, prev)
            prev = di.get(prev).prev
        return di.get(id2).weight, path

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        return None

    def centerPoint(self) -> (int, float):
        Max = math.inf
        node_id = 0
        for i in self.graph.get_all_v().keys():
            weight = self.djikstra(i)
            if weight < Max:
                Max = weight
                node_id = i
        return node_id, Max

    def plot_graph(self) -> None:
        return None

    def djikstra(self, src: int):
        prio = []
        di: {int, Father} = {}
        Max = 0
        heapq.heappush(prio, (0, Trio(src, src, 0)))
        while len(di) < self.graph.v_size() and len(prio):
            trioT = heapq.heappop(prio)
            dest = trioT[1].to
            if dest not in di.keys():
                self.graph.all_in_edges_of_node(dest)
                di[dest] = Father(trioT.prev, trioT.weight)
                if trioT.weight > Max:
                    Max = trioT.weight
                edges = self.graph.all_out_edges_of_node(dest)
                for i in edges.values():
                    weight = i[1] + trioT.weight
                    heapq.heappush(prio, (weight, Father(i[0], weight)))
        return Max

    def djikstra_shortest(self, src: int, des: int):
        prio = []
        di: {int, Father} = {}
        heapq.heappush(prio, (0, Trio(src, src, 0)))
        while len(di) < self.graph.v_size() and len(prio):
            trioT = heapq.heappop(prio)
            dest = trioT[1].to
            if dest not in di.keys():
                self.graph.all_in_edges_of_node(dest)
                di[dest] = Father(trioT[1].prev, trioT[1].weight)
                edges = self.graph.all_out_edges_of_node(dest)
                if des in di:
                    return di
                for i in edges.keys():
                    weight = edges.get(i) + trioT[1].weight
                    heapq.heappush(prio, (weight, Trio(dest, i, weight)))
        return None
