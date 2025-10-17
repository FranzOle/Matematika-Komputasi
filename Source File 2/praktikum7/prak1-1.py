matkom_class = {'Alya', 'Budi', 'Chandra', 'Diana'}
strukdat_class = {'Budi', 'Diana', 'Eka', 'Farhan'}
alpro_class = {'Alya', 'Farhan', 'Gilang'}

union_class = matkom_class.union(strukdat_class.union(alpro_class))
intersection_class = matkom_class.intersection(strukdat_class.intersection(alpro_class))
difference_class = alpro_class.difference(strukdat_class.union(matkom_class))

print(f"Gabungan Mahasiswa dari seluruh kelas:{union_class}")
print(f"Mahasiswa yang hadir di ketiga kelas:{intersection_class}")
print(f"Mahasiswa yang hanya hadir di kelas Algoritma dan Pemrograman:{difference_class}")