# Class for Defining Networks
from collections import defaultdict

class Graph:

    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, 
                 from_node:str, 
                 to_node:str, 
                 weight:float):
        """Adds edges to the graph

        Args:
            from_node (str): origin node.
            to_node (str): destination node.
            weight (float): distance or weight between 
                the nodes.
        """
        # Assuming edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight