import networkx as nx
import matplotlib.pyplot as plt


N = 4  
G = nx.Graph()
G.add_nodes_from(range(2 * N))
edge_list = [
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 3),
    (3, 4),
    (3, 5),
    (3, 6),
    (4, 5),
    (5, 6),
    (6, 7),
]
G.add_edges_from(edge_list)

pos = nx.circular_layout(G)

nx.draw_networkx(G, node_size=300, font_color="w", pos=pos)
plt.show()