from src.DiGraph import DiGraph
import unittest
import random as rnd
from src.node_data import node_data


def rand_edges(g: DiGraph, curr: node_data, amount: int, num_of_edges: int):
    for i in range(num_of_edges):
        while not g.add_edge(curr.id(), rnd.randint(0, amount), rnd.randrange(0, 15)):
            continue


class TestDiGraph(unittest.TestCase):
    g1 = DiGraph()
    g2 = DiGraph()
    g3 = DiGraph()
    g4 = DiGraph()
    g5 = DiGraph()

    for n in range(4):
        g1.add_node(n)
    for n in range(4):
        rand_edges(g1, g1.nodes().get(n), 4, 3)

    for n in range(15):
        g2.add_node(n)
    for n in range(15):
        rand_edges(g2, g2.nodes().get(n), 15, 5)

    for n in range(100):
        g3.add_node(n)
    for n in range(100):
        rand_edges(g3, g3.nodes().get(n), 100, 10)

    for n in range(5000):
        g4.add_node(n)
    for n in range(5000):
        rand_edges(g4, g4.nodes().get(n), 5000, 15)

    for n in range(150000):
        g5.add_node(n)
    for n in range(150000):
        rand_edges(g5, g5.nodes().get(n), 150000, 20)

    def test_v_size(self):
        self.assertTrue(self.g1.v_size() == 4)
        self.assertTrue(self.g2.v_size() == 15)
        self.assertTrue(self.g3.v_size() == 100)
        self.assertTrue(self.g4.v_size() == 5000)
        self.assertTrue(self.g5.v_size() == 150000)

    def test_e_size(self):
        self.assertTrue(self.g1.e_size() == 4 * 3)  # 12
        self.assertTrue(self.g2.e_size() == 15 * 5)  # 75
        self.assertTrue(self.g3.e_size() == 100 * 10)  # 1000
        self.assertTrue(self.g4.e_size() == 5000 * 15)  # 75000
        self.assertTrue(self.g5.e_size() == 150000 * 20)  # 3000000

    def test_get_all_v(self):
        self.assertTrue(self.g1.get_all_v() == self.g1.nodes())
        self.assertTrue(self.g1.get_all_v().get(2) == self.g1.nodes()[2])

        self.assertTrue(self.g2.get_all_v() == self.g2.nodes())
        self.assertTrue(self.g2.get_all_v().get(5) == self.g2.nodes()[5])

        self.assertTrue(self.g3.get_all_v() == self.g3.nodes())
        self.assertTrue(self.g3.get_all_v().get(27) == self.g3.nodes()[27])

        self.assertTrue(self.g4.get_all_v() == self.g4.nodes())
        self.assertTrue(self.g4.get_all_v().get(1234) == self.g4.nodes()[1234])

        self.assertTrue(self.g5.get_all_v() == self.g5.nodes())
        self.assertTrue(self.g5.get_all_v().get(54321) == self.g5.nodes()[54321])

    def test_all_in_edges_of_node(self):
        self.assertTrue(self.g1.all_in_edges_of_node(2) == self.g1.nodes().get(2).in_edges())
        self.assertTrue(self.g1.all_in_edges_of_node(0).get(1) == self.g1.nodes().get(0).in_edges().get(1))

        self.assertTrue(self.g2.all_in_edges_of_node(12) == self.g2.nodes().get(12).in_edges())
        self.assertTrue(self.g2.all_in_edges_of_node(10).get(7) == self.g2.nodes().get(10).in_edges().get(7))

        self.assertTrue(self.g3.all_in_edges_of_node(29) == self.g3.nodes().get(29).in_edges())
        self.assertTrue(self.g3.all_in_edges_of_node(21).get(52) == self.g3.nodes().get(21).in_edges().get(52))

        self.assertTrue(self.g4.all_in_edges_of_node(222) == self.g4.nodes().get(222).in_edges())
        self.assertTrue(self.g4.all_in_edges_of_node(234).get(858) == self.g4.nodes().get(234).in_edges().get(858))

        self.assertTrue(self.g5.all_in_edges_of_node(21212) == self.g5.nodes().get(21212).in_edges())
        self.assertTrue(self.g5.all_in_edges_of_node(205).get(9999) == self.g5.nodes().get(205).in_edges().get(9999))

    def test_all_out_edges_of_node(self):
        self.assertTrue(self.g1.all_out_edges_of_node(2) == self.g1.nodes().get(2).out_edges())
        self.assertTrue(self.g1.all_out_edges_of_node(0).get(1) == self.g1.nodes().get(0).out_edges().get(1))

        self.assertTrue(self.g2.all_out_edges_of_node(12) == self.g2.nodes().get(12).out_edges())
        self.assertTrue(self.g2.all_out_edges_of_node(10).get(7) == self.g2.nodes().get(10).out_edges().get(7))

        self.assertTrue(self.g3.all_out_edges_of_node(29) == self.g3.nodes().get(29).out_edges())
        self.assertTrue(self.g3.all_out_edges_of_node(21).get(52) == self.g3.nodes().get(21).out_edges().get(52))

        self.assertTrue(self.g4.all_out_edges_of_node(222) == self.g4.nodes().get(222).out_edges())
        self.assertTrue(self.g4.all_out_edges_of_node(234).get(858) == self.g4.nodes().get(234).out_edges().get(858))

        self.assertTrue(self.g5.all_out_edges_of_node(21212) == self.g5.nodes().get(21212).out_edges())
        self.assertTrue(self.g5.all_out_edges_of_node(205).get(9999) == self.g5.nodes().get(205).out_edges().get(9999))

    # def test_add_edge(self):
    #
    # def test_add_node(self):
    #
    # def test_remove_node(self):
    #
    # def test_remove_edge(self):


if __name__ == '__main__':
    unittest.main()
