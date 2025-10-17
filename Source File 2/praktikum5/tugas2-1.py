set_a = {1,2}
set_b = {2,3}
set_c = {3,4}

commutative_union = set_a.union(set_b) == set_b.union(set_a)
commutative_intersection = set_a.intersection(set_b) == set_b.intersection(set_a)
assosiative_union = set_a.union(set_b.union(set_c)) == set_a.union(set_b).union(set_c)
assosiative_intersection = set_a.intersection(set_b.intersection(set_c)) == set_a.intersection(set_b).intersection(set_c)
distibutive_union_intersection = set_a.union(set_b.intersection(set_c)) == (set_a.union(set_b)).intersection(set_a.union(set_c))

print(f"Hukum Komutatif:{commutative_union and commutative_intersection}")
print(f"Hukum Asosiatif: {assosiative_union and assosiative_intersection}")
print(f"Hukum Distributif: {distibutive_union_intersection}")