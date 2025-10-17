store_a = {'Alya', 'Deny', 'Chandra'}
store_b = {'Deny', 'Diana', 'Eka'}
store_c = {'Alya', 'Farhan', 'Gilang'}

commutative_union = store_a.union(store_b) == store_b.union(store_a)
associative_union = store_a.union(store_b.union(store_c)) == store_a.union(store_b).union(store_c)

print(f"Hukum Komutatif berlaku: {commutative_union}")
print(f"Hukum Asosiatif berlaku: {associative_union}")