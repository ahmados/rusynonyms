import networkx as nx

from pathlib import Path
from ru_synonyms.lexica import LexicalGraphInterface


class AntonymsGraph(LexicalGraphInterface):
    """
    Graph of antonyms.
    """

    def _initialize_graph(self) -> nx.Graph:
        graph_path = str(Path(__file__).parent / "_data/antonyms.adjlist")
        return nx.read_adjlist(graph_path)
