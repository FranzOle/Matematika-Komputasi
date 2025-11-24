relasi_R = [(1, 2), (2, 3)]
relasi_S = [(2, 3), (3, 4)]
komposisi_relasi = [(a, d) for (a, b) in relasi_R for (c, d) in relasi_S if b == c]
print("Relasi R:", relasi_R)
print("Relasi S:", relasi_S)
print("Komposisi Ro S:", komposisi_relasi)