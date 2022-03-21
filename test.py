from operator import ne
import matplotlib.pyplot as plt
# import required module
import networkx as nx
import random
from networkx.classes.function import path_weight
from numpy import array
# create object


G = nx.complete_graph(50)
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
        #print (intial_sol[x])
        #print (*temp)
        #print ("------------------------")

def sort_arr(array):
    x = sorted(array, key=getKey)
    #print(x)
    return x

def getKey(item):
    return item[1]

def mutation_func(parent_sol):
    deg = 3
    for x in range(deg):
        index_1 = random.randint(1,9)
        index_2 = random.randint(1,9)

        while (index_1 == index_2):
            index_2 = random.randint(1,9)

        temp = parent_sol[index_1]
        parent_sol[index_1] = parent_sol[index_2]
        parent_sol[index_2] = temp

    return parent_sol


def gen_algo(GA_arr):
    temp_GA = GA_arr[:10]
    for parent in range (10):
        for mutation in range (25):
            new_sol = mutation_func(temp_GA[parent][0])
            cost = path_weight(G, new_sol, weight="weight")
            temp_GA.append((new_sol, cost))
    return temp_GA

def control_GA():
    route = []
    intial_sol = []
    for x in range(50):
        route.append(x)
    
    intial_sample(route, intial_sol)
    intial_sol = sort_arr(intial_sol)
    new_gen_sol = gen_algo(intial_sol)
    

    text_file = open("GA_processing.txt", "w")
    for x in range (1,4):
        text_file.write("GENERATION " + str(x) + "\n")
        text_file.write("------------------------------------\n")
        new_gen_sol = sort_arr(gen_algo(new_gen_sol))
        text_file.write(str(new_gen_sol))  

    return new_gen_sol
   
# Main Function:
final = control_GA()
print("------------------------------")
print("Graph generating")
print("------------------")
print("GA optimizing the path for TSP")
print("Path: ", final[0][0])
print("Coat: ", final[0][1])
print("------------------")


