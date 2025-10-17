set_a = {1, 2, 3}
set_b = {2, 3, 4}
set_c = {3, 4, 5}

# Operasi gabungan
union_set = set_a.union(set_b, set_c)

# Operasi irisan
intersection_set = set_a.intersection(set_b, set_c)

# Operasi selisih
difference_set = set_a.difference(set_b.union(set_c))

print(f"Gabungan: {union_set}")
print(f"Irisan: {intersection_set}")
print(f"Selisih: {difference_set}")