# Traveling Salesman Project.
# Authors: Danish Faraz, Muhammad Ahmed.

from multiprocessing.dummy import current_process
from nis import cat
from pickle import TRUE
from anyio import current_time
import networkx as nx
import matplotlib.pyplot as plt
from numpy import empty, positive
from sqlalchemy import null
import random
import time
import logging
from sympy import reduce_abs_inequalities
from zmq import THREAD_NAME_PREFIX

G = nx.complete_graph(4)

nx.draw(G, node_color = "green", node_size = 500)

plt.show()
