"""
ru_synonyms module for getting antonyms
"""

from ru_synonyms.lexica import LexicaGraph
import networkx as nx
import sys
import os

path_base = os.path.dirname(__file__)
graph_path = os.path.join(path_base, '_data', 'antonyms.adjlist')
G = nx.read_adjlist(graph_path)

class AntonymsGraph(LexicaGraph):
    def __init__(self):
        self.G = G
