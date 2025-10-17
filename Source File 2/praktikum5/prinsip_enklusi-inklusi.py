set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_c = {5, 6, 7}
total_union = len(set_a) + len(set_b) + len(set_c) \
- len(set_a.intersection(set_b)) \
- len(set_a.intersection(set_c)) \
- len(set_b.intersection(set_c)) \
+ len(set_a.intersection(set_b).intersection(set_c))
print(f"Ukuran gabungan tiga himpunan (A U B U C):{total_union}")