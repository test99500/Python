import networkx as nx
import matplotlib.pyplot as plt

G = nx.bipartite.gnmk_random_graph(3, 5, 10, seed=123)
top = nx.bipartite.sets(G)[0]
pos = nx.bipartite_layout(G, top)

nx.draw(G, pos=pos, node_color='lightgreen', node_size=500, with_labels=True, arrowstyle="->")

plt.show()