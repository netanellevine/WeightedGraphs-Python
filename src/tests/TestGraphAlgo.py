import sys
sys.path.append("..")
import math
import unittest
from typing import List
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(unittest.TestCase):
    def test_get_graph(self):
        algo2 = GraphAlgo()
        g2 = algo2.get_graph()
        self.assertIsNotNone(g2)
        self.assertEqual(g2.v_size(), 0)
        self.assertEqual(g2.e_size(), 0)
        g2.add_node(5, (2, 2, 2))
        g2.add_node(6, (2, 2, 2))
        self.assertEqual(g2.v_size(), 2)
        g2.add_edge(5, 6, 7)
        self.assertEqual(g2.e_size(), 1)

    def test_shortest_path(self):
        algo1 = GraphAlgo()
        g1 = algo1.get_graph()
        for i in range(0, 100):
            g1.add_node(i, (i, i, i))
        for i in range(1, 100):
            g1.add_edge(0, i, 3)
            g1.add_edge(i, 0, 3)
        for i in range(2, 100):
            weight, path = algo1.shortest_path(0, i)
            self.assertEqual(weight, 3)
            self.assertEqual(path[0], 0)
            self.assertEqual(path[1], i)
            weight, path = algo1.shortest_path(i, i - 1)
            self.assertEqual(weight, 6)
            self.assertEqual(path[0], i)
            self.assertEqual(path[1], 0)
            self.assertEqual(path[2], i - 1)
        for i in range(0, 100):
            g1.add_edge(1, i, 2)
            g1.add_edge(i, 1, 2)
        for i in range(3, 100):
            weight, path = algo1.shortest_path(1, i)
            self.assertEqual(weight, 2)
            self.assertEqual(path[0], 1)
            self.assertEqual(path[1], i)
            weight, path = algo1.shortest_path(i, i - 1)
            self.assertEqual(weight, 4)
            self.assertEqual(path[0], i)
            self.assertEqual(path[1], 1)
            self.assertEqual(path[2], i - 1)

    def test_center(self):
        algo = GraphAlgo()
        g = algo.get_graph()
        for i in range(0, 100):
            g.add_node(i, (i, i, i))
        g.add_edge(1, 0, 2)
        for i in range(1, 100):
            self.assertEqual(algo.centerPoint(), (None, math.inf))
            g.add_edge(0, i, 3)
            g.add_edge(i, 0, 4)
        center, weight = algo.centerPoint()
        self.assertEqual(center, 0)
        self.assertEqual(weight, 3)
        for i in range(0, 100):
            g.add_edge(1, i, 2)
            g.add_edge(i, 1, 3)
        center1, weight1 = algo.centerPoint()
        self.assertEqual(center1, 1)
        self.assertEqual(weight1, 2)

    def test_tsp(self):
        algo = GraphAlgo()
        algo.load_from_json("G1.json")
        l: List[int] = [5, 3, 1, 2]
        path, weight = algo.TSP(l)
        for i in range(1, 6):
            self.assertEqual(path[i - 1], i)
        self.assertAlmostEqual(weight, 5.2, delta=0.1)
