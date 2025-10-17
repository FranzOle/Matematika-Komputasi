toko_a = {'Alya', 'Budi', 'Chandra'}
toko_b = {'Budi', 'Diana', 'Eka'}
toko_c = {'Alya', 'Farhan', 'Gilang'}

commutative_union = toko_a.union(toko_b) == toko_b.union(toko_a)

assosiative_union = toko_a.union(toko_b.union(toko_c)) == toko_a.union(toko_b).union(toko_c)

print(f"Verifikasi Hukum Komutatif:{commutative_union}")
print(f"Verifikasi Hukum Asosiatif:{assosiative_union}")