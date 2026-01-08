import networkx as nx

class SocialGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_relation(self, a, b):
        if a and b:
            self.graph.add_edge(a, b)

    def stats(self):
        return {
            "nodes": self.graph.number_of_nodes(),
            "edges": self.graph.number_of_edges(),
            "top_accounts": sorted(
                self.graph.degree, key=lambda x: x[1], reverse=True
            )[:5]
        }
