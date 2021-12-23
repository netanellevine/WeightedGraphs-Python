from src.GraphInterface import GraphInterface


# out edges <int dest,weight>
# in edges <int source,weight>
# position tuple
# weight float
from src.node_data import node_data


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
        pass

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if not self._nodes.get(node_id):
            added_node = node_data(node_id, pos)
            self._nodes[node_id] = added_node
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if not self._nodes.get(node_id):
            self._nodes.pop(node_id)
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self._nodes.get(node_id1) is not None and self._nodes.get(node_id2) is not None:
            n = self._nodes.get(node_id1)
            if n.get_out_edge(node_id2) is not None:
                n.out_edges().pop(node_id2)
                n = self._nodes.get(node_id2)
                if n.get_in_edge(node_id1) is not None:
                    n.in_edges().pop(node_id1)
                    return True
        return False
