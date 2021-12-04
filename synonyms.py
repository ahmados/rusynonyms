"""
ru_synonyms module for getting synonyms
"""

from ru_synonyms.lexica import LexicaGraph
import networkx as nx
import sys
import os

path_base = os.path.dirname(__file__)
graph_path = os.path.join(path_base, '_data', 'synonyms.adjlist')
G = nx.read_adjlist(graph_path)

class SynonymsGraph(LexicaGraph):
    def __init__(self):
        self.G = G
