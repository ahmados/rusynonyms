"""
ru_synonyms abstract class
"""
from typing import List
import networkx as nx
Graph = nx.classes.graph.Graph

class LexicaGraph:
    '''
    The LexicaGraph object gives you various lexicas depending on Graph used
    :param G: LexicaGraph used for getting lexicas
    :type G: networx.Graph
    '''
    def __init__(self):
        self.G = nx.empty_graph(1)

    def get_list(self, word: str) -> List:
        '''
        Returns list of lexicas for a given word

        :param word: given word
        :type word: str

        :returns: list of words
        :rtype: List
        '''
        return self.G.neighbors(word)

    def set_graph(self, G : Graph) -> None:
        '''
        Sets Graph parameter

        :param G: LexicaGraph to be used
        :type G: networkx.Graph

        :returns: Nothing
        :rtype: None
        '''
        self.G = G

    def is_in_dictionary(self, word: str) -> bool:
        '''
        Returns whether word in a dictionary or not

        :param word: given word
        :type word: str

        :returns: whether word in a dictionary or not
        :rtype: bool
        '''
        return word in self.G

    def get_list_in_radius(self, word: str, r : int) -> List:
        '''
        Returns all words in certain radius within the Graph

        :param word: given word
        :type word: str

        :param r: radius in Graph
        :type r: int

        :returns: list of words within given radius
        :rtype: List
        '''
        assert r <= 3, "radius is too big. Max value is 3"
        return nx.ego_graph(self.G, word, radius=r, undirected=True).nodes()
