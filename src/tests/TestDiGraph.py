from src.DiGraph import DiGraph
import unittest
import random as rnd


def rand_edges(g: DiGraph, curr: int, amount: int, num_of_edges: int):
    for i in range(amount):
        g.add_edge(curr, rnd.randint(0, num_of_edges - 1), rnd.randrange(0, 15))


class TestDiGraph(unittest.TestCase):
    g1 = DiGraph()
    g2 = DiGraph()
    g3 = DiGraph()
    g4 = DiGraph()
    g5 = DiGraph()

    for n in range(4):
        g1.add_node(n)
        rand_edges(g1, g1.nodes().get(n), 4, 3)

    for n in range(15):
        g2.add_node(n)
        rand_edges(g2, g2.nodes().get(n), 15, 5)

    for n in range(100):
        g3.add_node(n)
        rand_edges(g3, g3.nodes().get(n), 100, 10)

    for n in range(5000):
        g4.add_node(n)
        rand_edges(g4, g4.nodes().get(n), 5000, 5)

    for n in range(150000):
        g5.add_node(n)
        # rand_edges(g5, g5.nodes().get(n), 15000, 10)

    def test_v_size(self):
        self.assertTrue(self.g1.v_size() == 4)
        self.assertTrue(self.g2.v_size() == 15)
        self.assertTrue(self.g3.v_size() == 100)
        self.assertTrue(self.g4.v_size() == 5000)
        self.assertTrue(self.g5.v_size() == 150000)

    # def test_e_size(self):
    #
    # def test_get_all_v(self):
    #
    # def test_all_in_edges_of_node(self):
    #
    # def test_all_out_edges_of_node(self):
    #
    # def test_get_mc(self):
    #
    # def test_add_edge(self):
    #
    # def test_add_node(self):
    #
    # def test_remove_node(self):
    #
    # def test_remove_edge(self):


if __name__ == '__main__':
    unittest.main()
