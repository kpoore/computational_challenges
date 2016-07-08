import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import requests
import pylab

fin = open("p082_matrix.txt", "r")
M = []
N = []
G = nx.DiGraph()
for j, lines in enumerate(fin):
    temp = lines.split(',')
    a = []
    b = []
    for i, n in enumerate(temp):
        a.append(int(n))
        G.add_node(int(i + j * 80))
    M.append(a)
M = np.array(M)

# a = [131, 673, 234, 103, 18, 1]
# M = np.array([[131, 673, 234, 103, 18, 1],
#               [201, 96, 342, 965, 150, 950],
#               [603, 803, 749, 422, 111, 100],
#               [537, 699, 497, 121, 956, 500],
#               [805, 732, 524, 37, 331, 235],
#               [805, 732, 524, 37, 331, 235]])
# for i in range(36):
#     G.add_node(i)
#
# for i in range(len(a) - 1):
#     for j in range(len(a)):
#         G.add_edge(i + j * 6, i + j * 6 + 1, weight=M[j, i])
#
# # edges moving down
# for i in range(len(a) - 1):
#     for j in range(len(a) - 1):
#         G.add_edge(i + j * 6, i + j * 6 + 6, weight=M[j, i])
#
# # edges moving up
# for i in range(1, len(a) - 1):
#     for j in range(1, len(a)):
#         G.add_edge(i + j * 6, i + j * 6 - 6, weight=M[j, i])
#
# res = []
# paths = []
# # pos = nx.graphviz_layout(B, prog='neato')
# nx.draw(G, with_labels=True, arrows=False)
# plt.show()
# for i in range(0, 36, 6):
#     for j in range(5, 36, 6):
#         result = 0
#         res_t = nx.dijkstra_path(G, i, j)
#         paths.append(res_t)
#         for k in range(len(res_t) - 1):
#             result += G[res_t[k]][res_t[k + 1]]['weight']
#         res.append(result)
#
# print min(res)


# # edges moving right
for i in range(len(a) - 1):
    for j in range(len(a)):
        G.add_edge(i + j * 80, i + j * 80 + 1, weight=M[j, i])

# edges moving down
for i in range(len(a) - 1):
    for j in range(len(a) - 1):
        G.add_edge(i + j * 80, i + j * 80 + 80, weight=M[j, i])

# edges moving up
for i in range(1, len(a) - 1):
    for j in range(1, len(a)):
        G.add_edge(i + j * 80, i + j * 80 - 80, weight=M[j, i])
#
# pos = nx.graphviz_layout(B, prog='neato')
# nx.draw(G, pos, with_labels=False, arrows=False)
res = []
paths = []

for i in range(0, 6400, 80):
    for j in range(79, 6400, 80):
        result = M[j / 80, -1]
        res_t = nx.dijkstra_path(G, i, j)
        paths.append(res_t)
        for k in range(len(res_t) - 1):
            result += G[res_t[k]][res_t[k + 1]]['weight']
        res.append(result)

print res.index(min(res))

# print (nx.dijkstra_path(G, 0, 80**2 - 1))
#
# res = nx.dijkstra_path(G, 0, 80**2 - 1)
# fin_result = M[-1, -1]
# for i in range(len(res) - 1):
#     fin_result += G[res[i]][res[i + 1]]['weight']

# print fin_result
