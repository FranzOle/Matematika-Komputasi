import matplotlib.pyplot as plt
import networkx as nx

A = {1, 2, 3}
B = {2, 4, 6}

relation = [(a, b) for a in A for b in B if b % a == 0]

G = nx.DiGraph()

G.add_nodes_from(A)
G.add_nodes_from(B)

G.add_edges_from(relation)

plt.figure(figsize=(7, 4))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, arrows=True, node_size=1200, font_size=12)

plt.title("Graf Berarah Relasi: a adalah faktor dari b")
plt.show()