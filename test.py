import matplotlib.pyplot as plt
# import required module
import networkx as nx
import random
from networkx.classes.function import path_weight
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
#print(labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
#plt.show()



"""for x in route:
    print(x)"""


def intial_sample(route, intial_sol):
    for x in range(10):
        temp = random.sample(route, len(route))
        temp.append(temp[0])
        cost = path_weight(G, temp, weight="weight")
        intial_sol.append((temp, cost))
        print (intial_sol[x])
        print (*temp)
        print ("------------------------")

def sort_arr(array):
    x = sorted(array, key=getKey)
    #print(x)
    return x

def getKey(item):
    return item[1]

def gen_algo(num, GA_arr):
    temp_arr = GA_arr
    print(temp_arr)
    temp_GA = temp_arr[:5]

    print("-------------")
    print(temp_GA)

    

def control_GA():
    route = []
    intial_sol = []
    for x in range(10):
        route.append(x)
    
    intial_sample(route, intial_sol)
    GA_arr = sort_arr(intial_sol)
    gen_algo(5, GA_arr)

   


# Main Function:
control_GA()
