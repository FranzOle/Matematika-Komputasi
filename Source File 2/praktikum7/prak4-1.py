cabang_a = {'Alya', 'Budi', 'Chandra'}
cabang_b = {'Budi', 'Diana', 'Eka'}
cabang_c = {'Alya', 'Farhan', 'Gilang'}

total_kustomer_unik = len(cabang_a) + len(cabang_b) + len(cabang_c) \
- len(cabang_a.intersection(cabang_b)) - len(cabang_a.intersection(cabang_c)) \
- len(cabang_b.intersection(cabang_c)) + len(cabang_a.intersection(cabang_b).intersection(cabang_c))

print(f"Jumlah Pelanggan Unik: {total_kustomer_unik}")