import json


class node_data:

    def __init__(self, id: int, pos: tuple[float, float, float]):
        self.id: int = id
        self._in_edges: dict[int, float] = {}
        self._out_edges: dict[int, float] = {}
        self._pos: tuple[float, float, float] = pos
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

    def pos(self):
        return self._pos

    def size(self):
        return self._size

    def __repr__(self) -> str:
        ans = """node_data ID: {}, pos: {},
        edges_in: {},
        edges_out: {},\n""".format(self.id, self._pos, len(self._in_edges), len(self._out_edges))
        return ans

    def in_edges_str(self):
        ans = "{"
        for src, weight in self._in_edges:
            ans += "{}: {},\n".format(src, weight)
        return ans

    def out_edges_str(self):
        ans = "{"
        for dest, weight in self._out_edges:
            ans += "{}: {},\n".format(dest, weight)
        return ans
