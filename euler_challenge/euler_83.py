import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import requests
import pylab

fin = open("p083_matrix.txt", "r")
M = []
N = []
G = nx.DiGraph()
for j, lines in enumerate(fin):
    temp = lines.split(',')
    a = []
    b = []
    for i, n in enumerate(temp):
        a.append(int(n))
        b.append(int(i + j * 80))
        G.add_node(int(i + j * 80))
    M.append(a)
    N.append(b)
M = np.array(M)
b = np.array(b)
N = np.array(N)

# edges moving right
for i in range(len(a) - 1):
    for j in range(len(a) - 1):
        G.add_edge(i + j * 80, i + j * 80 + 1, weight=M[i, j])

# edges moving left
for i in range(1, len(a)):
    for j in range(1, len(a)):
        G.add_edge(i + j * 80, i + j * 80 - 1, weight=M[i, j])

# edges moving down
for i in range(len(a)):
    for j in range(len(a)):
        G.add_edge(i + j * 80, i + j * 80 + 80, weight=M[i, j])

# edges moving up
for i in range(len(a)):
    for j in range(len(a)):
        G.add_edge(i + j * 80, i + j * 80 - 80, weight=M[i, j])
        print i, i + j * 80, i + j * 80 - 80


# pos = nx.graphviz_layout(B, prog='neato')
# nx.draw(G, pos, with_labels=False, arrows=False)
res = []
paths = []

result = M[-1, -1]
res_t = nx.dijkstra_path(G, 0, 80**2 - 1)
paths.append(res_t)
for k in range(len(res_t) - 1):
    result += G[res_t[k]][res_t[k + 1]]['weight']
res.append(result)

print result

# print (nx.dijkstra_path(G, 0, 80**2 - 1))
#
# res = nx.dijkstra_path(G, 0, 80**2 - 1)
# fin_result = M[-1, -1]
# for i in range(len(res) - 1):
#     fin_result += G[res[i]][res[i + 1]]['weight']
#
# print fin_result
