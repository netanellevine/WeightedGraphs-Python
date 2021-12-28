import random as rnd


class node_data:

    def __init__(self, id: int, pos=1):
        if pos != 1:
            self._pos: tuple[float, float, float] = pos
        else:
            self._pos: tuple[float, float, float] = (rnd.randint(0, 10), rnd.randint(0, 10), 0.0)
        self._id: int = id
        self._in_edges: dict[int, float] = {}
        self._out_edges: dict[int, float] = {}
        self._size: int = 0

    def connect(self, src: int, dest: int, weight: float):
        if src in self._in_edges:
            self._in_edges[src] = weight
        elif dest in self._out_edges:
            self._out_edges[dest] = weight
        self._size += 1

    def get_in_edge(self, src: int):
        return self._in_edges.get(src)

    def get_out_edge(self, dest: int):
        return self._out_edges.get(dest)

    def get_edge(self, src: int, dest: int):
        if self.get_in_edge(src):
            return self.get_in_edge(src), 1
        elif self.get_out_edge(dest):
            return self.get_out_edge(dest), -1
        else:
            return -2

    def in_edges(self):
        return self._in_edges

    def out_edges(self):
        return self._out_edges

    def get_pos(self):
        return self._pos

    def size(self):
        return self._size

    def id(self):
        return self._id

    # def __repr__(self) -> str:
    #     ans = """node_data ID: {}, pos: {},
    #     edges_in: {},
    #     edges_out: {},\n\t""".format(self._id, self._pos, len(self._in_edges), len(self._out_edges))
    #     return ans
    def __repr__(self) -> str:
        ans = """ID-{}: |edges_out|={}, |edges_in|={}""".format(self._id, len(self._out_edges), len(self._in_edges))
        return ans
