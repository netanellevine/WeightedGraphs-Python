import sys
from GraphInterface import GraphInterface
from node_data import node_data
sys.path.append("..")


# out edges <int dest,weight>
# in edges <int source,weight>
# position tuple
# weight float
class DiGraph(GraphInterface):

    def __init__(self):
        self._nodes: {int, node_data} = {}
        self._mc: int = 0
        self._e_size: int = 0

    def v_size(self) -> int:
        return len(self._nodes)

    def e_size(self) -> int:
        return self._e_size

    def nodes(self):
        return self._nodes

    def get_all_v(self) -> dict:
        return self._nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self._nodes[id1].in_edges()

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self._nodes[id1].out_edges()

    def get_mc(self) -> int:
        return self._mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self._nodes and id2 in self._nodes:
            n1 = self._nodes.get(id1)
            n2 = self._nodes.get(id2)
            if id2 not in n1.out_edges() and id1 not in n2.in_edges():
                n1.out_edges()[id2] = weight
                n2.in_edges()[id1] = weight
                self._e_size += 1
                self._mc += 1
                return True
        return False

    def add_node(self, node_id: int, pos=1) -> bool:
        if node_id not in self._nodes:
            added_node = node_data(node_id, pos)
            self._nodes[node_id] = added_node
            self._mc += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self._nodes:
            self._nodes.pop(node_id)
            self._mc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 in self._nodes and node_id2 in self._nodes:
            n1 = self._nodes.get(node_id1)
            n2 = self._nodes.get(node_id2)
            if node_id1 in n2.in_edges() and node_id2 in n1.out_edges():
                n1.out_edges().pop(node_id2)
                n2.in_edges().pop(node_id1)
                self._e_size -= 1
                self._mc += 1
                return True
        return False

    def __repr__(self) -> str:
        ans = """Graph: |V|={}, |E|={},
        {}""".format(self.v_size(), self.e_size(), self.nodes())
        return ans

