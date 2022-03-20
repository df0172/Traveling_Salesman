import matplotlib.pyplot as plt
# import required module
import networkx as nx
import random
# create object
G = nx.complete_graph(10)
for (u, v) in G.edges():
    G.edges[u,v]['weight'] = random.randint(0,1000)
    #print(u,v,G.edges[u,v])
# illustrate graph
pos = nx.spring_layout(G)
nx.draw(G, node_color = 'green',
			node_size=500, pos=pos, with_labels = True)
labels = {e: G.edges[e]['weight'] for e in G.edges}
print(labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
#plt.show()

route = []
gen_1_sol = []
for x in range(10):
    route.append(x)

"""for x in route:
    print(x)"""

for x in range(10):
    temp = random.shuffle(route)
    cost = sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(temp))
    gen_1_sol.append(temp, cost)
    print (gen_1_sol)


"""
from networkx.algorithms import approximation as approx
cycle = approx.simulated_annealing_tsp(G, "greedy", source=0, alpha=.01)
print(cycle)
cost = sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle))
print(cost)

cycle = approx.greedy_tsp(G, source=0)
print(cycle)
cost = sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle))
print(cost)
"""