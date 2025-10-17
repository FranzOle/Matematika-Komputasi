set_a = {1,2}
set_b = {2,3}
set_c = {3,4}

original_statement = set_a.union(set_b.intersection(set_c))
dualitas_statement = set_a.intersection(set_b.union(set_c))

print(f"Pernyataan Asli: {original_statement}")
print(f"Pernyataan Dualitas: {dualitas_statement}")