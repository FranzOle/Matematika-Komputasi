import numpy as np
A = {1, 2, 3}
B = {2, 4, 6}

relation = {(a, b) for a in A for b in B if b % a == 0}

def create_relation_matrix(set_a, set_b, relation):
    matrix = [[1 if (a, b) in relation else 0 for b in set_b] for a in set_a]
    return np.array(matrix)

matrix = create_relation_matrix(A, B, relation)
print("Matriks Relasi:\n", matrix)