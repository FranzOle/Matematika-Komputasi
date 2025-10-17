toko_a = {'Laptop', 'Mouse', 'Keyboard'}
toko_b = {'Mouse', 'Printer', 'Monitor'}
toko_c = {'Laptop', 'Printer', 'Mouse'}
gabungan_produk = toko_a.union(toko_b, toko_c)
irisan_produk = toko_a.intersection(toko_b, toko_c)

print(f"Produk yang dijual oleh semua toko:{gabungan_produk}")
print(f"Produk yang dijual setidaknya satu toko:{irisan_produk}")
print(f"Dualitas Produk yang dijual oleh setidaknya satu toko: {gabungan_produk}")
print(f"Dualitas Produk yang dijual oleh semua toko:{irisan_produk}")