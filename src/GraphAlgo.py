import math
import heapq
import random
import time
from typing import List
import json

from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface


class Trio:
    def __init__(self, prev: int, to: int):
        self.prev: int = prev
        self.to: int = to


class Father:
    def __init__(self, prev: int, weight: float):
        self.prev: int = prev
        self.weight: float = weight


def swap(j, i, li):
    tmp = li[j]
    li[j] = li[i]
    li[i] = tmp


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: GraphInterface):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        self.graph = DiGraph()
        try:
            f = open(file_name)
            data = json.load(f)
            nodes = data["Nodes"]
            for i in nodes:
                try:
                    self.graph.add_node(i["id"], i["pos"].split(","))
                except:
                    self.graph.add_node(i["id"], (random.random(), random.random(), 0.0))
            edges = data["Edges"]
            for i in edges:
                self.graph.add_edge(i["src"], i["dest"], (i["w"]))
        except IOError:
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:
        try:
            f = open(file_name, "x")
            di = self.graph.nodes_to_json()
            f.write(di)
        except IOError:
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        di = self.djikstra_shortest(id1, id2)
        path = [id2]
        prev = di.get(id2).prev
        while path[0] != id1:
            path.insert(0, prev)
            prev = di.get(prev).prev
        return di.get(id2).weight, path

    def find_route(self, node_lst: List[int]):
        TSPath: List[int] = []
        route = set()
        copy = node_lst.copy()
        last = node_lst.pop(0)
        cost = 0
        while len(node_lst) > 1:
            node_lst.pop(0)
            id2 = node_lst[0]
            if id2 not in route:
                weight, path = self.shortest_path(last, id2)
                cost = cost + weight
                for i in path:
                    TSPath.append(i)
                    route.add(i)
                last = TSPath[-1]
        for i in copy:
            if i not in route:
                return List[int]
        return cost, TSPath

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        cities = node_lst
        if cities is None:
            return None
        f = True;
        Min = math.inf
        fin = []
        for i in range(0, len(cities)):
            copy = cities.copy()
            swap(0, i, copy)
            copy = self.find_route(copy)
            if copy is not None and len(copy) >= len(cities):
                cost = 0
                for j in range(0, len(copy)):
                    edges = self.graph.all_out_edges_of_node(j)
                    e = edges[j + 1]
                    if e is None:
                        f = False
                        break

                    else:
                        cost = cost + e.getWeight()
                    if cost < Min and f:
                        Min = cost;
                        fin = copy;

                    f = True

        return fin, Min

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
        heapq.heappush(prio, (0, Trio(src, src)))
        while len(di) < self.graph.v_size() and len(prio) > 0:
            weig, trioT = heapq.heappop(prio)
            dest = trioT.to
            if dest not in di.keys():
                self.graph.all_in_edges_of_node(dest)
                di[dest] = Father(trioT.prev, weig)
                if weig > Max:
                    Max = weig
                edges = self.graph.all_out_edges_of_node(dest)
                for i in edges.keys():
                    weight = edges.get(i) + weig
                    heapq.heappush(prio, (weight, Trio(dest, i)))
        return Max

    def djikstra_shortest(self, src: int, des: int):
        prio = []
        di: {int, Father} = {}
        heapq.heappush(prio, (0, Trio(src, src)))
        while len(di) < self.graph.v_size() and len(prio) > 0:
            weig, trioT = heapq.heappop(prio)
            dest = trioT.to
            if dest not in di.keys():
                self.graph.all_in_edges_of_node(dest)
                di[dest] = Father(trioT.prev, weig)
                edges = self.graph.all_out_edges_of_node(dest)
                if des in di:
                    return di
                for i in edges.keys():
                    weight = edges.get(i) + weig
                    heapq.heappush(prio, (weight, Trio(dest, i)))
        return None


g = DiGraph()
algo = GraphAlgo(g)
algo.load_from_json("C:/Users/yanir/PycharmProjects/Weighted_Graph_Algorithms_Py/data/Test1.json")
start_time = time.time()
print(algo.centerPoint())
print("--- %s seconds ---" % (time.time() - start_time))
