import networkx as nx
import matplotlib.pyplot as plt

D = ["Deny", "Budi", "Cici"]
relasi_teman = [("Deny", "Budi"), ("Budi", "Cici")]
G = nx.DiGraph()
G.add_nodes_from(D)
G.add_edges_from(relasi_teman)

plt.figure(figsize=(5,5))
nx.draw(G, with_labels=True, node_color='lightgreen', font_size=10,
        font_weight='bold', arrowsize=20)

plt.title("Graf Berarah untuk Relasi 'Teman'")
plt.show()