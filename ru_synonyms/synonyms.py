import networkx as nx

from pathlib import Path
from ru_synonyms.lexica import LexicalGraphInterface


class SynonymsGraph(LexicalGraphInterface):
    """
    Graph of synonyms.
    """

    def _initialize_graph(self) -> nx.Graph:
        graph_path = str(Path(__file__).parent / "_data/synonyms.adjlist")
        return nx.read_adjlist(graph_path)
