import networkx as nx
from progressbar import progressbar

from pyrthomas.network_analyser import NetworkAnalyser

network = nx.DiGraph()

network.add_edge('TRL3', 'IFN', weight=1)
network.add_edge('IFN', 'DENV', weight=-1)
network.add_edge('DENV', 'IFN', weight=-1)
network.add_edge('DENV', 'TRL3', weight=1)
network.add_edge('DENV', 'SOCS', weight=1)
network.add_edge('SOCS', 'IFN', weight=-1)
network.add_edge('SOCS', 'TRL3', weight=-1)
network.add_edge('IFN', 'SOCS', weight=1)

graphs = NetworkAnalyser.get_possible_state_graphs(network)
possible_parameters = NetworkAnalyser.get_possible_parameters(network)


for graph in progressbar(graphs, max_value=1):
    pass

# 262144 enteris in 2:16sec

