import networkx as nx
from progressbar import progressbar

from pyrthomas.network_analyser import NetworkAnalyser

network = nx.DiGraph()
# self.network.add_edge('x', 'y', weight=1)
# self.network.add_edge('x', 'x', weight=2)
# self.network.add_edge('y', 'x', weight=-1)

network.add_edge('BTK', 'MAL', weight=1)
network.add_edge('MAL', 'NFKB', weight=1)
network.add_edge('NFKB', 'INCY', weight=1)
network.add_edge('INCY', 'NFKB', weight=2)
network.add_edge('INCY', 'SOCS1', weight=1)
network.add_edge('SOCS1', 'NFKB', weight=-1)
network.add_edge('SOCS1', 'MAL', weight=-1)

graphs = NetworkAnalyser.get_possible_state_graphs(network)
possible_parameters = NetworkAnalyser.get_possible_parameters(network)


for graph in progressbar(graphs, max_value=len(possible_parameters)):
    pass

# 294912 enteris in 8:56 sec

