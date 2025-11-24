C = [1, 2, 3]
relasi_matriks = []
for i in C:
    row = []
    for j in C:
        if i > j:
            row.append(1)
        else:
            row.append(0)
    relasi_matriks.append(row)
print("Matriks relasi 'lebih dari':")
for row in relasi_matriks:
    print(row)