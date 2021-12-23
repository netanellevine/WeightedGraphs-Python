class node_data:

    def __init__(self, id: int, pos: tuple[float, float, float]):
        self.id: int = id
        self._in_edges: dict[int, float] = {}
        self._out_edges: dict[int, float] = {}
        self._pos: tuple[float, float, float] = pos
        self._size: int = 0

    def connect(self, src: int, dest: int, weight: float):
        if not self._in_edges.get(src):
            self._in_edges[src] = weight
        elif not self._out_edges.get(dest):
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

