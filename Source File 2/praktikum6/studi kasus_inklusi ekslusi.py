branch_a = {'Alya', 'Budi', 'Chandra'}
branch_b = {'Budi', 'Diana', 'Eka'}
branch_c = {'Alya', 'Farhan', 'Gilang'}

total_unique_customers = len(branch_a) + len(branch_b) + len(branch_c) \
- len(branch_a.intersection(branch_b)) - len(branch_a.intersection(branch_c)) \
- len(branch_b.intersection(branch_c)) + len(branch_a.intersection(branch_b).intersection(branch_c))

print(f"Jumlah pelanggan unik: {total_unique_customers}")