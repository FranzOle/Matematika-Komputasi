store_a = {'Laptop', 'Mouse', 'Keyboard'}
store_b = {'Mouse', 'Printer', 'Monitor'}
store_c = {'Laptop', 'Printer', 'Mouse'}
union_products = store_a.union(store_b, store_c)
intersection_products = store_a.intersection(store_b, store_c)
print(f"Produk yang dijual oleh setidaknya satu toko: {union_products}")
print(f"Produk yang dijual oleh semua toko:{intersection_products}")