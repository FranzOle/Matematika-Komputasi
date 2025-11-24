import networkx as nx
import matplotlib.pyplot as plt

def gambar_graf_relasi(A, B, R):
    G = nx.DiGraph()

    G.add_nodes_from(A)
    G.add_nodes_from(B)

    for a, b in R:
        G.add_edge(a, b)

    pos = nx.spring_layout(G)
    
    plt.figure(figsize=(7, 5))
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=1500, font_size=12, arrowsize=20)
    
    plt.title("Graf Berarah untuk Relasi R")
    plt.show()

A = [1, 2, 3, 4]
B = [2, 4, 6, 8]
R = {(1, 2), (2, 4), (3, 6), (4, 8)}

gambar_graf_relasi(A, B, R)