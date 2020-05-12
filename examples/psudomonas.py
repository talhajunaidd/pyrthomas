import networkx as nx
from progressbar import progressbar

from pyrthomas.network_analyser import NetworkAnalyser

network = nx.DiGraph()
network.add_edge('x', 'y', weight=1)
network.add_edge('x', 'x', weight=2)
network.add_edge('y', 'x', weight=-1)

graphs = NetworkAnalyser.get_possible_state_graphs(network)
possible_parameters = NetworkAnalyser.get_possible_parameters(network)
count = 0
for p in possible_parameters:
    count += 1
print(f"{count}")

for graph in progressbar(graphs, max_value=count):
    pass
# print(f"{count}")
# 324 enteris in 0.176 sec
