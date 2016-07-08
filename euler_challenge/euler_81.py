import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import requests
import pylab
import time


fin = open("p081_matrix.txt", "r")
t0 = time.time()
M = []
# Create and generate nodes from file
G = nx.DiGraph()
for j, lines in enumerate(fin):
    temp = lines.split(',')
    a = []
    for i, n in enumerate(temp):
        a.append(int(n))
        G.add_node(int(i + j * 80))
    M.append(a)
M = np.array(M)


for i in range(len(a) - 1):
    for j in range(len(a) - 1):
        G.add_edge(i + j * 80, i + j * 80 + 1, weight=M[i, j])
for i in range(len(a)):
    for j in range(len(a)):
        G.add_edge(i + j * 80, i + j * 80 + 80, weight=M[i, j])

# Graphic representation to ensure proper network structure
# nx.draw(G, with_labels=False, arrows=False)
# print (nx.dijkstra_path(G, 0, 80**2 - 1))

res = nx.dijkstra_path(G, 0, 80**2 - 1)
fin_result = M[-1, -1]
for i in range(len(res) - 1):
    fin_result += G[res[i]][res[i + 1]]['weight']
t1 = time.time()
print fin_result, t1 - t0
