import numpy as np

A = {1, 2, 3}
R = [(1, 2), (2, 3)]

ukuran = len(A)
matriks_adj = np.zeros((ukuran, ukuran), dtype=int)
indeks_map = {val: idx for idx, val in enumerate(A)}

for a, b in R:
    matriks_adj[indeks_map[a]][indeks_map[b]] = 1

for k in range(ukuran):
    for i in range(ukuran):
        for j in range(ukuran):
            matriks_adj[i][j] = matriks_adj[i][j] or (matriks_adj[i][k] and matriks_adj[k][j])

print("Matriks Klosur Transitif:\n", matriks_adj)