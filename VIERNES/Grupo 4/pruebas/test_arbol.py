"""Pruebas basicas del modelo P04.

Ejecutar: python pruebas/test_arbol.py   (desde la raiz del proyecto)
"""

import sys
import unittest
from pathlib import Path

import networkx as nx

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT))

import main as proyecto

EXCEL = PROJECT / "P04_Aves_humedales.xlsx"


class TestAvesHumedales(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.G = proyecto.leer_grafo(EXCEL)
        cls.T = proyecto.arbol_generador(cls.G)

    def test_grafo_conectado(self):
        self.assertTrue(nx.is_connected(self.G))

    def test_arbol_cubre_todos_los_humedales(self):
        self.assertEqual(set(self.T.nodes()), set(self.G.nodes()))

    def test_arbol_sin_ciclos(self):
        n_edges = self.T.number_of_edges()
        n_comp = nx.number_connected_components(self.T)
        self.assertEqual(n_edges, self.T.number_of_nodes() - n_comp)

    def test_validacion_4_parques(self):
        Tp = nx.minimum_spanning_tree(self.G.subgraph(proyecto.PARQUES), weight="km")
        self.assertTrue(nx.is_connected(Tp))
        self.assertEqual(Tp.number_of_edges(), Tp.number_of_nodes() - 1)
        self.assertEqual(Tp.number_of_edges(), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
