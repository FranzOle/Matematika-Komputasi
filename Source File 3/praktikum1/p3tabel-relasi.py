B = [1, 2, 4]
tabel_relasi = []
for i in B:
    row = []
    for j in B:
        if j % i == 0:
            row.append(1)
        else:
            row.append(0)
    tabel_relasi.append(row)
print("Tabel relasi kelipatan:")
for row in tabel_relasi:
    print(row)