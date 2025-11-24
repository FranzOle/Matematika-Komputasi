R1 = {(1, 2), (2, 3), (3, 4)}
R2 = {(3, 5), (4, 6)}

def gabung_relasi(relasi_satu, relasi_dua):
    hasil_gabungan = relasi_satu.union(relasi_dua)
    return hasil_gabungan

hasil = gabung_relasi(R1, R2)

print("Relasi R1:", R1)
print("Relasi R2:", R2)
print("Gabungan R1 U R2:", hasil)