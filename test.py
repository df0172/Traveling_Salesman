from networkx.readwrite.graph6 import write_graph6_file
from networkx.algorithms.boundary import node_boundary
import matplotlib.pyplot as plt
# import required module
import networkx as nx
import random
# create object
G = nx.complete_graph(10)
for (u, v) in G.edges():
    G.edges[u,v]['weight'] = random.randint(0,1000)
    print(u,v,G.edges[u,v])
# illustrate graph
pos = nx.spring_layout(G)
nx.draw(G, node_color = 'green',
			node_size=500, pos=pos, with_labels = True)
labels = {e: G.edges[e]['weight'] for e in G.edges}
print(labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

