from src.GraphInterface import GraphInterface

# out edges <int dest,weight>
# in edges <int source,weight>
# position tuple
# weight float
from src.node_data import node_data
"""

"""

class DiGraph(GraphInterface):

    def __init__(self):
        self._nodes: dict[int, node_data] = {}
        self._mc: int = 0
        self._e_size: int = 0

    def v_size(self) -> int:
        return len(self._nodes)

    def e_size(self) -> int:
        return self._e_size

    def get_all_v(self) -> dict:
        return self._nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self._nodes[id1].in_edges()

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self._nodes[id1].out_edges()

    def get_mc(self) -> int:
        return self._mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if (id1 and id2) in self._nodes:
            n1 = self._nodes.get(id1)
            n2 = self._nodes.get(id2)
            if id2 not in n1.out_edges() and id1 not in n2.in_edges():
                n1.out_edges()[id2] = weight
                n2.in_edges()[id1] = weight
                self._e_size += 1
                return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self._nodes:
            added_node = node_data(node_id, pos)
            self._nodes[node_id] = added_node
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self._nodes:
            self._nodes.pop(node_id)
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (node_id1 and node_id2) in self._nodes:
            n1 = self._nodes.get(node_id1)
            n2 = self._nodes.get(node_id2)
            if node_id1 in n2.in_edges() and node_id2 in n1.out_edges():
                n1.out_edges().pop(node_id2)
                n2.in_edges().pop(node_id1)
                self._e_size -= 1
                return True

        return False

    def __repr__(self) -> str:
        ans = """Graph: |V| = {}, |E| = {},
        nodes_data:[\n\t {}]""".format(self.v_size(), self._e_size, self._nodes)
        return ans
