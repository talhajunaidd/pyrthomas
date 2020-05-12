import networkx as nx
from progressbar import progressbar

from pyrthomas.network_analyser import NetworkAnalyser

network = nx.DiGraph()

network.add_edge('NFKB', 'P13K', weight=1)
network.add_edge('NFKB', 'P53', weight=1)
network.add_edge('P13K', 'NFKB', weight=1)
network.add_edge('P13K', 'P21', weight=1)
network.add_edge('P13K', 'FOXM1', weight=1)
network.add_edge('P21', 'NFKB', weight=-1)
network.add_edge('FOXM1', 'P21', weight=-1)
network.add_edge('P53', 'FOXM1', weight=-1)
network.add_edge('P53', 'MDM2', weight=1)
network.add_edge('P53', 'CMYC', weight=-1)
network.add_edge('P53', 'P13K', weight=-1)
network.add_edge('MDM2', 'P53', weight=-1)
network.add_edge('OGT', 'CMYC', weight=1)
network.add_edge('OGT', 'P13K', weight=1)
network.add_edge('OGT', 'OGA', weight=-1)
network.add_edge('CMYC', 'OGT', weight=1)
network.add_edge('OGA', 'OGT', weight=-1)

graphs = NetworkAnalyser.get_possible_state_graphs(network)

for graph in progressbar(graphs):
    pass
