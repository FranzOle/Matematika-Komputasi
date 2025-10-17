kelas_musik = {"Andi", "Bima", "Clara", "Dian", "Gilang"}
kelas_olahraga = {"Clara", "Dian", "Rangga", "Sari", "Toni"}

himpunan_semesta = kelas_musik.union(kelas_olahraga)
# Operasi gabungan (union)
gabungan = kelas_musik.union(kelas_olahraga)
print("Gabungan:", gabungan)
# Operasi irisan (intersection)
irisan = kelas_musik.intersection(kelas_olahraga)
print("Irisan:", irisan)
# Operasi selisih (difference)
selisih = kelas_musik.difference(kelas_olahraga)
print("Selisih (kelas_musik - kelas_olahraga):", selisih)

komplemen_musik = himpunan_semesta.difference(kelas_musik)
komplemen_olahraga = himpunan_semesta.difference(kelas_olahraga)
print(f"Komplemen kelas_musik: {komplemen_musik}")
print(f"Komplemen kelas_olahraga: {komplemen_olahraga}")